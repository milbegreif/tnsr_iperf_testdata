#!/bin/bash 

cd /home/ubuntu

ssh node5 "cd; ./log-cpu-net-2.1.py" > /dev/null &

./log-cpu-net-2.1.py > /dev/null &

ping -w65 -D 172.22.24.10 > latency.txt &

iperf3 -c 172.22.24.10 -t60  -A 28,28 -p 5002  -Z  -b 25G &
iperf3 -c 172.22.24.10 -t60  -A 29,29 -p 5003  -Z  -b 25G &
iperf3 -c 172.22.24.10 -t60  -A 30,30 -p 5004  -Z  -b 25G &
iperf3 -c 172.22.24.10 -t60  -A 31,31 -p 5005  -Z  -b 25G &

