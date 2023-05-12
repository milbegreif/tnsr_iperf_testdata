#!/bin/bash

cd /home/ubuntu

ssh node5 "cd; ./log-cpu-net-2.1.py" > /dev/null &

./log-cpu-net-2.1.py  > /dev/null &

ping -w65 -D 100.64.0.24 > latency.txt &

iperf3 -c 100.64.0.24 -w 300k -t60  -M 540 -A   24,24 -p 4998  -Z -b 20G  &
iperf3 -c 100.64.0.24 -w 300k -t60  -M 540 -A   25,25 -p 4999  -Z -b 20G  &
iperf3 -c 100.64.0.24 -w 300k -t60  -M 540 -A   26,26 -p 5000  -Z -b 20G  &
iperf3 -c 100.64.0.24 -w 300k -t60  -M 540 -A   27,27 -p 5001  -Z -b 20G  &
iperf3 -c 100.64.0.24 -w 300k -t60  -M 540 -A   28,28 -p 5002  -Z -b 20G  &
iperf3 -c 100.64.0.24 -w 300k -t60  -M 540 -A   29,29 -p 5003  -Z -b 20G  &
iperf3 -c 100.64.0.24 -w 300k -t60  -M 540 -A   30,30 -p 5004  -Z -b 20G  &
iperf3 -c 100.64.0.24 -w 300k -t60  -M 540 -A   31,31 -p 5005  -Z -b 20G  &
