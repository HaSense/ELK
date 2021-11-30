# This is a sample Python script.

import psutil

if __name__ == '__main__':

    #print(psutil.cpu_percent(percpu=True, interval=1))
    print(psutil.cpu_percent(interval=1))  # cpu 현재 사용량 100분

    cpufreq = psutil.cpu_freq()
    print(str(cpufreq.current))  # cpu 성능, GHz
    print(len(psutil.pids()))   #프로세스 개수

    mem = psutil.virtual_memory()
    print(mem.percent) #메모리 사용량


