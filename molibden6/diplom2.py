#! /usr/bin/env python
# coding: utf-8

import sys
import glob
import serial
import codecs
import numpy as np
import struct
from time import  time

def reception(s, z):
    buff = []
    size = 0
    basic_date = []
    time_start_function = time()
    while 1:
        if time() - time_start_function > 10:
            return 'Time is out'
        res = s.read()
        buff.append(ord(res))
        if len(buff) == 10:
            #print(buff)
            size = buff[8:10]
            size = bytearray(size)
            size = struct.unpack("h", size)[0]
        if size == 0:
            if len(buff) == 14:
                break
        else:
            if len(buff) == 18 + size:
                break
    buff_1 = buff[:10]
    buff_2 = buff[10:14]
    if size != 0:
        basic_date = buff[14:-4]
        basic_date_CRC = buff[-4:]
        if bytearray(basic_date_CRC) != check_sum(basic_date):
            print('сумма в гл части левая')

    #print('buff_2',buff_2)
    #print('buff_1',check_sum(buff_1))

    if bytearray(buff_2) != check_sum(buff_1):
        print('сумма в заголовке левая')
    if z == 1 or z == 2 or z == 3:
        basic_date = basic_date[1:]
        try:
            return struct.unpack("f", bytes(basic_date))
        except:
            return "error"
    # if z == 4:
    #     basic_date = basic_date[1:]
    #     for i in basic_date:
    #         i = codecs.decode(bytes(i), 'UTF-8')
    #print(basic_date)

    #print(buff)
    #return buff


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

def ping(s):
    byte_array = [255, 255, 255, 1, 1, 1, 4, 1, 0, 0]
    k = check_sum(byte_array)
    for i in k:
        byte_array.append(i)
    byte_array = bytearray(byte_array)
    s.write(byte_array)

def med(s):
    byte_array = [255, 255, 255, 1, 1, 1, 6, 25, 0, 1]
    k = check_sum(byte_array)
    for i in k:
        byte_array.append(i)
    byte_array = bytearray(byte_array)
    array = [34]
    k = check_sum(array)
    for i in k:
        array.append(i)
    for i in array:
        byte_array.append(i)
    s.write(byte_array)

def speed_1(s):
    byte_array = [255, 255, 255, 1, 1, 1, 6, 25, 0, 1]
    k = check_sum(byte_array)
    for i in k:
        byte_array.append(i)
    byte_array = bytearray(byte_array)
    array = [44]
    k = check_sum(array)
    for i in k:
        array.append(i)
    for i in array:
        byte_array.append(i)
    s.write(byte_array)

def speed_2(s):
    byte_array = [255, 255, 255, 1, 1, 1, 6, 25, 0, 1]
    k = check_sum(byte_array)
    for i in k:
        byte_array.append(i)
    byte_array = bytearray(byte_array)
    array = [49]
    k = check_sum(array)
    for i in k:
        array.append(i)
    for i in array:
        byte_array.append(i)
    s.write(byte_array)


def measure():
    str = 'COM13'
    s = serial.Serial(str)
    result_data_meas = {}
    ping(s)
    result_data_meas['ping'] = reception(s, 0)
    med(s)
    result_data_meas['med'] = reception(s, 1)
    # reception(s, 1)
    speed_1(s)
    result_data_meas['speed'] = reception(s, 2)
    # reception(s, 2)
    speed_2(s)
    result_data_meas['speed_2'] = reception(s, 3)
    # reception(s, 3)
    return  result_data_meas


if __name__ == '__main__':
    print(measure())


# byte_array = [255, 255, 255, 1, 1, 1, 6, 29, 0, 1]
# k = check_sum(byte_array)
# for i in k:
#     byte_array.append(i)
# byte_array = bytearray(byte_array)
# array = [30]
# k = check_sum(array)
# for i in k:
#     array.append(i)
# for i in array:
#     byte_array.append(i)
# s.write(byte_array)
# reception(s, 4)






