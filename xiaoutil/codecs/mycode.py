# -*- coding: utf-8 -*-
# 指定编码方式，是告诉系统，按照什么编码来读取这个py文件的
__author__ = 'BaoQiang'


def encode_decode():
    s = '小包'

    str_uni = s.encode("unicode-escape").decode("unicode-escape")
    str_raw = str(s.encode("unicode-escape")).lstrip('b\'').rstrip('\'').replace('\\\\', '\\')
    # str_raw = s.encode("unicode-escape").decode("unicode-escape").replace("\\","\\\\")
    str_utf8 = s.encode('utf-8').decode('utf-8')
    str_gbk = s.encode("gbk").decode("gbk")
    # str_raw = r'\u5c0f\u5305'
    # str_uni = u'\u5c0f\u5305'

    byte_utf8 = s.encode('utf-8')
    byte_gbk = s.encode('gbk')
    byte_uni = s.encode('unicode-escape')
    # byte_utf8 = b'\xe5\xb0\x8f\xe5\x8c\x85'
    # byte_gbk = b'\xd0\xa1\xb0\xfc'
    # byte_uni = b'\\u5c0f\\u5305'

    uni_bin = ' '.join([bin(int(item, base=16)).replace('0b', '') if item else '' for item in
                        str(byte_uni).lstrip('b\'\\u').rstrip('\'').split('\\\\u')])
    utf8_bin = ' '.join([bin(int(item, base=16)).replace('0b', '') if item else '' for item in
                         str(byte_utf8).replace('\\x', '\\\\x').lstrip('b\'\\x').rstrip('\'').split('\\\\x')])
    gbk_bin = ' '.join([bin(int(item, base=16)).replace('0b', '') if item else '' for item in
                        str(byte_gbk).replace('\\x', '\\\\x').lstrip('b\'\\x').rstrip('\'').split('\\\\x')])

    # uni_bin = '0101 1100 0000 1111 0101 0011 0000 0101'
    # utf8_bin = '11100101 10110000 10001111 11100101 10001100 10000101'
    # gbk_bin = '11010000 10100001 10110000 11111100'

    unicode_use_uni_to_byte = str_uni.encode("unicode-escape")
    unicode_use_utf8_to_byte = str_utf8.encode("utf-8")
    unicode_use_gbk_to_byte = str_gbk.encode("gbk")

    byte_in_uni_format_to_unicode = byte_uni.decode("unicode-escape")
    byte_in_utf8_format_to_unicode = byte_utf8.decode("utf-8")
    byte_in_gbk_format_to_unicode = byte_gbk.decode("gbk")

    print()

    print(
            'i am {{{}}}. my unicode is: {{{}}}, i am equal to it.\nmy binary code is {{{}}}.'
            'i am just 0,1 bits in memory, this is my actual look.'.format(
                    str_uni, str_raw, uni_bin))
    # print('use unicode to print, i am {{{}}}. use utf8 to print, i am {{{}}}. use gbk to print, i am {{{}}}.'.format(
    #         str_uni, str_utf8, str_gbk))
    # print('so for human readable, i have to be interpreted to specific format. just like utf8, gbk.'.format(
    #                 uni_bin))

    print()

    print('in unicode format, i am {{{}}} and {{{}}} in binary'.format(byte_uni, uni_bin))
    print('in utf-8 format, i am {{{}}} and {{{}}} in binary'.format(byte_utf8, utf8_bin))
    print('in gbk format, i am {{{}}} and {{{}}} in binary'.format(byte_gbk, gbk_bin))

    print()

    print('as a binary, so when i am in utf8 bin format, if someone use gbk to interpret me, i will be messy.')

    print()

    print(
            'i am unicode {{{}}}. if i want to be transferred in network or saved one disk, i should be 0&1 format as byte array for saving space.\n'
            'i will be : {{{}}} using unicode-escape to interpret; i will be : {{{}}} using utf8 to interpret;\n'
            'i will be : {{{}}} using gbk to interpret.'.format(
                    str_raw, unicode_use_uni_to_byte, unicode_use_utf8_to_byte, unicode_use_gbk_to_byte))

    print()

    print(
        'i am bytes {{{}}} in unicode-escape format; i am bytes {{{}}} in utf8 format; i am bytes {{{}}} in gbk format.\n'
        'in memory, we must be transformed to unicode format so that we could be understood, for both machine and human.\n'
        'use different encoding format to decode, we will be in uniform unicode format: {{{}}}'
        ''.format(byte_uni, byte_utf8, byte_gbk, byte_in_uni_format_to_unicode))

    print()

    print('for human readable, 小包 used space in bin format!')


def my_decode():
    f_in = open("C:\\Users\\BaoQiang\\Desktop\\out.txt", "r")
    fw = open("C:\\Users\\BaoQiang\\Desktop\\out2.txt", "w")

    data = f_in.read().decode("unicode_escape")

    fw.write(data.encode("utf-8"))


def test():
    # for s in "小包":
    #     print(hex(ord(s)))
    # print(bin(ord(s)))

    # l = r'\xe5\xb0\x8f\xe5\x8c\x85'
    # l = r'\xd0\xa1\xb0\xfc'
    # l = r'\u5c0f\u5305'
    #
    # for s in l.split('\\u'):
    #     if s:
    #         print(bin(int(s,base=16)).replace(r'0b',''),end=' ')

    # print(r'\xe5\xb0\x8f\xe5\x8c\x85'.split('\\x'))

    # s = '128'
    # print(bin(int(s,base=10)))
    # byte_utf8 = b'\xe5\xb0\x8f\xe5\x8c\x85'
    # uni_bin = ' '.join([bin(int(item,base=16)).replace('0b','') if item else '' for item in str(byte_utf8).replace('\\x','\\\\x').lstrip('b\'\\x').rstrip('\'').split('\\\\x')])
    # print(uni_bin)

    # print(str(byte_utf8).replace('\\x','\\\\x').lstrip('b\'\\x').rstrip('\'').split('\\\\x'))

    s = b'\x40\x41'
    print(s)
    s = b'\x00\x01'
    print(s)


if __name__ == "__main__":
    encode_decode()
    # test()
    pass
