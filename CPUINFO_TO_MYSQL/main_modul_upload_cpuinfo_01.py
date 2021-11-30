# This is a sample Python script.

import psutil
import threading
import mysql.connector  #conda install -c anaconda mysql-connector-python

def mysql_connect_action():
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="ai123",
        database="iot_db"
    )
    return mydb

def upload_mysql_cpuinfo():

    mydb = mysql_connect_action()
    mycursor = mydb.cursor()

    #[CPU 사용률 정보]
    cpu_percent_value = psutil.cpu_percent(interval=1)
    print(cpu_percent_value)  # cpu 현재 사용량 100분
    print(type(cpu_percent_value))

    #[CPU 현재 속도]
    cpufreq = psutil.cpu_freq()
    print(str(cpufreq.current))  # cpu 성능, GHz
    print(type(cpufreq.current))

    #[CPU 프로세스 개수]
    print(int(len(psutil.pids())))   #프로세스 개수
    print(type(int(len(psutil.pids()))))

    #[시스템 메모리 사용률]
    mem = psutil.virtual_memory()
    print(mem.percent) #메모리 사용량
    print(type(mem.percent))

    sql = "INSERT INTO cpu_sensing (ptime, cpu_percent, cpu_speed, process_cnt, mem_used) VALUES (now(), %s, %s, %s, %s)"
    val = (cpu_percent_value, cpufreq.current, len(psutil.pids()), mem.percent)
    #val = (100.1, 100.1, 100, 100.5)

    mycursor.execute(sql, val)
    mydb.commit()

    print(mycursor.rowcount, cpufreq.current, len(psutil.pids()), mem.percent)


if __name__ == '__main__':
    while 1:
    #t = threading.Thread(target=upload_mysql_cpuinfo)
        t=threading.Timer(1, upload_mysql_cpuinfo)
        t.start()
        t.join()

    print("Main Thread")
