#!/usr/bin/python3
'''UTF-8 validation'''


def validUTF8(data):
    def get_num_bytes(byte):
        if byte & 0x80 == 0:
            return 1
        elif byte & 0xE0 == 0xC0:
            return 2
        elif byte & 0xF0 == 0xE0:
            return 3
        elif byte & 0xF8 == 0xF0:
            return 4
        else:
            return 0

    index = 0
    while index < len(data):
        num_bytes = get_num_bytes(data[index])

        if num_bytes == 0:
            return False

        index += 1
        for _ in range(num_bytes - 1):
            if index >= len(data) or data[index] & 0xC0 != 0x80:
                return False
            index += 1

    return True
