#!/usr/bin/env python
# coding: utf-8

import subprocess
import re
from distutils.spawn import find_executable
import sys

adb_path = find_executable("adb")

if not adb_path:
    print('adb path not found.')
    exit(-1)


def sadb():
    # for line in (proc.stdout.readline, ''):
    #     print line.rstrip()
    # while((line=proc.stdout.readline) != ''):
    devices, outputs = read_devices()
    args = read_args()
    device_count = len(devices)
    if (len(args) == 0):
        print('just use sadb as an alias for adb')
        exit(-1)
    if (args[0] == 'devices'):
        cmd = [adb_path]
        cmd += args
        subprocess.call(cmd)
        exit(0)

    if device_count > 1:
        nums = select_devices(devices)
        for seq in nums:
            exec_adb_cmd_on_device(devices[seq], args)
    elif device_count == 1:
        exec_adb_cmd_on_device(devices[0], args)
    else:
        print("No device found")
        exit(-1)


# 选择设备
def select_devices(devices):
    device_count = len(devices)
    print("Device list:")
    print("0) All devices")
    for i, d in enumerate(devices):
        print("%d) %s\t%s" % (i + 1, d['serial'], d['model']))
    str = input("\nselect: ")
    splits = re.split(r'[\s+,]', str)
    if str == '0':
        nums = range(0, device_count)
    else:
        nums = []
        for i in splits:
            try:
                seq = int(i) - 1
            except ValueError:
                print("error input: %s, retry again\n" % i)
                return select_devices(devices)
            if 0 <= seq < device_count:
                nums.append(seq)
            else:
                print("error input: %s, retry again\n" % i)
                return select_devices(devices)
    return nums


# 读取参数
def read_args():
    args = []
    for a in sys.argv[1:]:
        args.append(a)
    return args


# 读取设备列表
def read_devices():
    devices = []
    outputs = []
    proc = subprocess.Popen([adb_path, 'devices', '-l'], stdout=subprocess.PIPE)
    while True:
        line = proc.stdout.readline().decode('utf-8')
        outputs.append(line)
        if line != '':
            if re.match(r'^[0-9a-zA-Z_]+\s+device', line):
                d = re.split(r'\s+', line)
                devices.append({
                    'serial': d[0],
                    'model': d[-2]
                })
        else:
            break
    return devices, outputs


# 执行adb命令
def exec_adb_cmd_on_device(device, args):
    cmd = [adb_path, "-s", device['serial']]
    cmd += args
    print(("\n[%s]exec: " + ' '.join(cmd)) % device['model'])
    subprocess.call(cmd)

# just for debug.
def dd(obj):
    print(obj)
    exit(0)