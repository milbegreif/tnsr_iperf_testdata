#!/bin/python3

import psutil
import time
import signal
import sys

# Prefix for server and client logs
prefix = 'client-'
#prefix = 'server-'

test_parameter = 'iperf3-'
source_log_infix = 'cpu-net-data.'

txt_data_file = prefix + test_parameter + source_log_infix + "txt"

# Anzahl der Sekunden zwischen den Aufzeichnungen
interval = 1

# time to run
max_time_to_run = 65

# Name des Netzwerkinterfaces
interface_name = 'mlx-swp29s0'

# Signal-Handler fuer Abbruch
def sigint_handler(signum, frame):
    print('Aufzeichnung abgebrochen.')
    sys.exit(0)


# Signal-Handler fuer Abbruch registrieren
signal.signal(signal.SIGINT, sigint_handler)

# Aufzeichnung von CPU-Auslastungen und Netzwerkstatistiken
with open(txt_data_file, 'w') as f:

    net_io_counters = psutil.net_io_counters(pernic=True).get(interface_name)
    prev_bytes_sent = net_io_counters.bytes_sent / 1024 ** 3
    prev_bytes_recv = net_io_counters.bytes_recv / 1024 ** 3
    prev_pakets_sent = net_io_counters.packets_sent
    prev_pakets_recv = net_io_counters.packets_recv
    while max_time_to_run > 0:
        # CPU-Auslastung aufzeichnen
        cpu_percent_list = psutil.cpu_percent(percpu=True)
        cpu_percent = ','.join([str(x) for x in cpu_percent_list])

        # Netzwerkstatistiken aufzeichnen
        net_io_counters = psutil.net_io_counters(pernic=True).get(interface_name)

        # Netzwerkinterface abrufen
        bytes_sent = net_io_counters.bytes_sent / 1024 ** 3
        bytes_recv = net_io_counters.bytes_recv / 1024 ** 3
        pakets_sent = net_io_counters.packets_sent
        pakets_recv = net_io_counters.packets_recv

        # Deltas errechnen zwischen Messpunkten
        throughput_sent = (bytes_sent - prev_bytes_sent)  * 8 / interval
        throughput_recv = (bytes_recv - prev_bytes_recv)  * 8 / interval
        pps_sent = pakets_sent - prev_pakets_sent
        pps_recv = pakets_recv - prev_pakets_recv

        # Messpunkt X mit X+1 ueberschreiben
        prev_bytes_sent = bytes_sent
        prev_bytes_recv = bytes_recv
        prev_pakets_sent = pakets_sent
        prev_pakets_recv = pakets_recv

        # Daten in Datei schreiben
        f.write(f'{cpu_percent},{throughput_sent},{throughput_recv},{pps_sent},{pps_recv}\n')

        # Live-Ausgabe
        print(f'Aufzeichnung: CPU-Auslastung = {cpu_percent_list}%,'
              f'Durchsatz gesendet = {throughput_sent:.2f} Gbit/s,'
              f'Durchsatz empfangen = {throughput_recv:.2f} Gbit/s,'
              f'PPS gesendet = {pps_sent} pps,'
              f'PPS recv = {pps_recv} pps')
        try:
            time.sleep(interval)
            max_time_to_run -= 1
        except KeyboardInterrupt:
            sigint_handler(signal.SIGINT, None)

