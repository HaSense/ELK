# This is a sample Python script.

import psutil
import os

def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

if __name__ == '__main__':
    print_hi('PyCharm')
    from cpuinfo import get_cpu_info

    # for key, value in get_cpu_info().items():
    #     print("{0}: {1}".format(key, value))

    print(psutil.cpu_percent(percpu=True))  # cpu 코어별 퍼센트
    print(psutil.cpu_percent()) #cpu 현재 사용량 100분ㄹㄹ
    #print(psutil.cpu_stats())
    cpufreq = psutil.cpu_freq()
    print(str(cpufreq.current) + 'GHz')  # cpu 성능

    #process = psutil.Process()
    #print(process.io_counters())
    print(len(psutil.pids()))   #프로세스 개수

    # print(psutil.Process()) #스레드 개수

    mem = psutil.virtual_memory()
    # usingMem = (mem.used / mem.total) * 100
    # print(f'{usingMem:.1f}') #메모리 사용량

    print(mem.percent) #메모리 사용량
