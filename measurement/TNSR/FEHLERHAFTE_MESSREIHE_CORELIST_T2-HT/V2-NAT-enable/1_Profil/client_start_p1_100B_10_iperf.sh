#!/bin/bash

cd /home/ubuntu

ssh node5 "cd; ./log-cpu-net-2.1.py" > /dev/null &

./log-cpu-net-2.1.py > /dev/null &

ping -w65 -D 172.22.24.10 > latency.txt &

#iperf3 -c 172.22.24.10   -w 300k -t60   -M 100 -A  16,16 -p 4998  -Z -b 7G &
#iperf3 -c 172.22.24.10   -w 300k -t60   -M 100 -A  17,17 -p 4999  -Z -b 7G &
#iperf3 -c 172.22.24.10   -w 300k -t60   -M 100 -A  18,18 -p 5000  -Z -b 7G &
#iperf3 -c 172.22.24.10   -w 300k -t60   -M 100 -A  19,19 -p 5001  -Z -b 7G &
#iperf3 -c 172.22.24.10   -w 300k -t60   -M 100 -A  20,20 -p 5002  -Z -b 7G &
#iperf3 -c 172.22.24.10   -w 300k -t60   -M 100 -A  21,21 -p 5003  -Z -b 7G &
iperf3 -c 172.22.24.10   -w 300k -t60   -M 100 -A  22,22 -p 5004  -Z -b 7G &
iperf3 -c 172.22.24.10   -w 300k -t60   -M 100 -A  23,23 -p 5005  -Z -b 7G &

iperf3 -c 172.22.24.10   -w 300k -t60   -M 100 -A  24,24 -p 5006  -Z -b 7G &
iperf3 -c 172.22.24.10   -w 300k -t60   -M 100 -A  25,25 -p 5007  -Z -b 7G &
iperf3 -c 172.22.24.10   -w 300k -t60   -M 100 -A  26,26 -p 5008  -Z -b 7G &
iperf3 -c 172.22.24.10   -w 300k -t60   -M 100 -A  27,27 -p 5009  -Z -b 7G &
iperf3 -c 172.22.24.10   -w 300k -t60   -M 100 -A  28,28 -p 5010  -Z -b 7G &
iperf3 -c 172.22.24.10   -w 300k -t60   -M 100 -A  29,29 -p 5011  -Z -b 7G &
iperf3 -c 172.22.24.10   -w 300k -t60   -M 100 -A  30,30 -p 5012  -Z -b 7G &
iperf3 -c 172.22.24.10   -w 300k -t60   -M 100 -A  31,31 -p 5013  -Z -b 7G &
