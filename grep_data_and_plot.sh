#!/bin/bash

# This script takes all log-files and configs from the iperf test nodes
# at first it wills store in the Folder Dropzone,
# if the data valid it will copied in the right result folder.


Profil=3

TESTNAME="BASISMESSUNG_P${Profil}"

# shellcheck disable=SC1068
latency_file="latency-${TESTNAME}.txt"
client_file="client-${TESTNAME}.txt"
server_file="server-${TESTNAME}.txt"


scp node4:/home/ubuntu/latency.txt ./DROPZONE/$latency_file
python3 plot-latency.py ./DROPZONE/$latency_file &

scp node4:/home/ubuntu/client-iperf3-cpu-net-data.txt ./DROPZONE/$client_file
python3 plot-cpu-net-log-2.2.py ./DROPZONE/$client_file &

scp node5:/home/ubuntu/server-iperf3-cpu-net-data.txt ./DROPZONE/$server_file
python3 plot-cpu-net-log-2.2.py ./DROPZONE/$server_file &

scp node4:/home/ubuntu/setup_p${Profil}* ./DROPZONE/client_setup_p${Profil}.sh
scp node4:/home/ubuntu/start_p${Profil}* ./DROPZONE/client_start_p${Profil}.sh
scp node5:/home/ubuntu/setup_p${Profil}* ./DROPZONE/server_setup_p${Profil}.sh
scp node5:/home/ubuntu/start_p${Profil}* ./DROPZONE/server_start_p${Profil}.sh