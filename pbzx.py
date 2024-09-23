import argparse
import lzma
import struct
import sys
import os

XBSZ = 4 * 1024
ZBSZ = 1024 * XBSZ
VERSION = "1.0.2"


class Stream:
    def __init__(self, file=None):
        self.file = file

    def read(self, size):
        if self.file:
            return self.file.read(size)
        return sys.stdin.read(size)

    def read64(self):
        data = self.read(8)
        if len(data) != 8:
            raise ValueError("Failed to read 64-bit integer")
        return struct.unpack('>Q', data)[0]  # Big-endian 64-bit integer

    def close(self):
        if self.file:
            self.file.close()


def parse_args():
    parser = argparse.ArgumentParser(
        description=f'pbzx v{VERSION} stream parser')
    parser.add_argument('-v', '--version', action='store_true', help='Print version and exit.')
    parser.add_argument('-n', '--noxar', action='store_true', help='The input data is not a XAR archive but the pbzx Payload.')
    parser.add_argument('filename', nargs='?', help='File to process (or stdin if not provided)')
    return parser.parse_args()


def main():
    args = parse_args()

    # Handle version output
    if args.version:
        print(f"pbzx v{VERSION}")
        return

    # Open the file or stdin
    if args.filename:
        stream = Stream(open(args.filename, 'rb'))
    else:
        stream = Stream()

    # Read initial pbzx header
    header = stream.read(4)

    # Debugging: Print the header value read
    print(f"Header read: {header}")

    # Check if the header matches 'pbzx'
    if header != b'pbzx':
        print(f"Invalid stream header: {header}, expected 'pbzx'", file=sys.stderr)
        return 1

    flags = stream.read64()

    # Initialize LZMA stream
    while flags & (1 << 24):
        flags = stream.read64()
        length = stream.read64()

        plain = length == 0x1000000
        chunk = stream.read(min(XBSZ, length))

        if not plain:
            # Only check the header if it is expected to be LZMA compressed
            if chunk[:6] != b'\xfd7zXZ':
                print("Not an LZMA compressed chunk, skipping header check.", file=sys.stderr)
            else:
                print("Valid LZMA chunk header found.")

        # Decompress or output the plain data
        decompressor = None if plain else lzma.LZMADecompressor()

        while length > 0:
            if plain:
                sys.stdout.buffer.write(chunk[:min(XBSZ, length)])
            else:
                chunk_size = min(XBSZ, length)
                try:
                    decompressed = decompressor.decompress(chunk[:chunk_size])
                    sys.stdout.buffer.write(decompressed)
                except lzma.LZMAError:
                    print("LZMA failure", file=sys.stderr)
                    return 1

            length -= min(XBSZ, length)
            if length > 0:
                chunk = stream.read(min(XBSZ, length))

        # Check footer for non-plain data
        if not plain and chunk[-2:] != b'YZ':
            print("Footer is not YZ, but skipping for non-plain data.", file=sys.stderr)

    stream.close()


if __name__ == "__main__":
    main()
