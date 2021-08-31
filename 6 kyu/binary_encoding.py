"""

Unicode Transformation Format – 8-bit
As the name suggests UTF-8 was designed to encode data in a stream of bytes.

It works by splitting the bits up in multiples of eight. This is achieved by inserting headers to mark in how many bytes the bits were split. If the bits need to be split in two, the header 110 is added as prefix leaving five bits of the byte for the rest of the data. Followed by a continuation byte.

A continuation byte always start with 10 leaving six bits for data. For a three-way split: the header 1110 is added with two continuation bytes and for four: 11110 with three continuation bytes. The number of ones at the start of the first byte denotes the number of bytes the data was split in.

Task
Your task is to write two functions:

to_utf8_binary: which encodes a string to a bitstring using UTF-8 encoding.
from_utf8_binary: which does the reverse.
Layout of UTF-8 byte sequences:

"""
def to_utf8_binary(string: str) -> str:
    return ''.join(bin(char)[2:].rjust(8,'0') for char in string.encode('utf8'))


def from_utf8_binary(binary: str) -> str:
    return bytearray(int(binary[i*8:(i+1)*8], 2) for i in range(len(binary) // 8)).decode('utf8')