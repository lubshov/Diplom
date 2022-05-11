#! /usr/bin/env python
# coding: utf-8

import sys
import glob
import serial
import codecs
import numpy as np
import struct

def check_sum( byte_array ):
    if type(byte_array) == 'byres':
        byte_array = [ord(i) for i in byte_array]
    s_byte = [np.uint16(byte_array[i]) for i in range(len(byte_array))]
    CRC = np.uint32(0)
    j = np.int16(0)
    j = np.uint16(np.uint16(len(byte_array)) & 1)
    if j != 0:
        CRC = s_byte[0]
    else:
        CRC = 0
    for i in range(j, np.uint16(len(byte_array)), 2):
        CRC = np.uint32((CRC << 5)) + np.uint32((CRC >> 27))
        CRC ^= np.uint32(((s_byte[i] << 8) + s_byte[i + 1]))
    CRC = int(CRC)
    ou_t = (CRC).to_bytes(4, byteorder='little', signed=False)
    return ou_t

def reception():
    buff = []
    size = 0
    while 1:
        res = s.read()
        buff.append(ord(res))
        if len(buff) == 9:
            size = buff[7:9]
            size = bytearray(size)
            size = struct.unpack("h", size)[0]
        if len(buff) == 14 + size:
            break
    buff_1 = buff[:10]
    buff_2 = buff[10:14]
    if size != 0:
        basic_date = buff[14:-4]
        basic_date_CRC = buff[-4:]
        if bytearray(basic_date_CRC) != check_sum(basic_date):
            print('сумма в гл части левая')

    print('buff_2',buff_2)
    print('buff_1',check_sum(buff_1))

    if bytearray(buff_2) != check_sum(buff_1):
        print('сумма в заголовке левая')
    return buff

def ping():
    byte_array = [255, 255, 255, 1, 1, 1, 8, 25, 0, 5, 113]
    k = check_sum(byte_array)
    for i in k:
        byte_array.append(i)
    value = 1.34
    ba = bytearray(struct.pack("f", value))
    byte_array = bytearray(byte_array)
    str = 'COM13'
    s = serial.Serial(str)
    s.write(a)


#[255, 255, 255, 1, 1, 1, 4, 1, 0, 0]






#a = [255, 255, 255, 1, 1, 1, 4, 1, 0, 0]
#k = check_sum(a)
#for i in k:
    #a.append(i)
#a = bytearray(a)

#print(a)
#s.write(a)
#print(reception())

str = 'COM13'
s = serial.Serial(str)

ping()
while 1:
    res = s.read()
    print(res)





