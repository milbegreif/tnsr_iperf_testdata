import argparse

import matplotlib.pyplot as plt
import numpy as np

parser = argparse.ArgumentParser(description='Plot data from JSON file')
parser.add_argument('filename', type=str, help='Path to the JSON file')
args = parser.parse_args()
filename = args.filename

#filename = "server-tnsr_v6_two_tnsr_with_s2s_wgh_HyperT.txt"

txt_data_file = filename
png_plot_file = filename.replace('txt', 'png')

# Daten aus Datei lesen
with open(txt_data_file, 'r') as f:
    data = f.readlines()

# CPU-Auslastungen, Bytes gesendet und Bytes empfangen in separate Listen speichern
cpu_percent_list = []
bits_sent_list = []
bits_recv_list = []
pps_sent_list = []
pps_recv_list = []
for line in data:
    value_cnt = len(line.strip().split(','))

    cpu_percent_str = line.strip().split(',')[:(value_cnt - 4)]  # ersten 16 CPU-Auslastungen extrahieren
    cpu_percent = [float(x) for x in cpu_percent_str]  # CPU-Auslastungen in Liste von Gleitkommazahlen konvertieren
    cpu_percent_list.append(cpu_percent)

    bits_sent = line.strip().split(',')[(value_cnt - 4)]
    bits_recv = line.strip().split(',')[(value_cnt - 3)]
    pps_sent = line.strip().split(',')[(value_cnt - 2)]
    pps_recv = line.strip().split(',')[(value_cnt - 1)]

    bits_sent_list.append(int(float(bits_sent)))
    bits_recv_list.append(int(float(bits_recv)))
    pps_sent_list.append(int(float(pps_sent)))
    pps_recv_list.append(int(float(pps_recv)))

# Figure und Axes erstellen
fig, (ax_nics, ax_pps, ax_cpu) = plt.subplots(3, figsize=(9, 9))

# X-Achsen Datenpunkte bestimmen
num_points = len(bits_recv_list)  # Anzahl der Datenpunkte
time_interval = 1  # Sekunden
end_time = num_points * time_interval  # Endzeit in Sekunden

# x-Achse erstellen
x = np.arange(0, end_time, time_interval)

# Linienplot erstellen
line_bits_sent = ax_nics.plot(x, bits_sent_list, label="Gesendete Bits/s")
line_bits_recv = ax_nics.plot(x, bits_recv_list, label="Empfangene Bits/s")

line_pps_sent = ax_pps.plot(x, pps_sent_list, label="Gesendete Pakete pro Sekunde")
line_pps_recv = ax_pps.plot(x, pps_recv_list, label="empfange Pakete pro Sekunde")

line_CPU = ax_cpu.plot(x, cpu_percent_list, label="CPU Utilization")

# Erstellen des Plot fuer Datendurchsatz
ax_nics.set_title('Netzwerkstatistik')
ax_nics.set_ylabel('Durchsatz (GBit/s)')
ax_nics.set_xlabel('Zeit (s)')

# Legende erstellen
legend_nics = ax_nics.legend(loc='upper right', fontsize='small')
for line in legend_nics.get_lines():
    line.set_linewidth(4.0)

# Farben und Werte in der Legende setzen
legend_nics.get_texts()[0].set_text('Gesendete Bits/s')
legend_nics.get_texts()[1].set_text('Empfangene Bits/s')

# Erstellen der PPS
ax_pps.set_title('Pakete pro Sekunde')
ax_pps.set_ylabel('Pakete pro Sekunde (pps)')
ax_pps.set_xlabel('Zeit (s)')

# Legende erstellen fuer PPS
legend_pps = ax_pps.legend(loc='upper right', fontsize='small')
for line in legend_pps.get_lines():
    line.set_linewidth(4.0)

# Farben und Werte in der Legende setzen
legend_pps.get_texts()[0].set_text('Gesendete PPS')
legend_pps.get_texts()[1].set_text('Empfangene PPS')

# Erstellen der CPU-Auslastung
ax_cpu.set_title('CPU-Auslastung')
ax_cpu.set_xlabel('Zeit (s)')
ax_cpu.set_ylabel('CPU-Utilization (%)')

ax_nics.set_ylim([0, 120])
ax_cpu.set_ylim([0, 120])

# Das Plotten einer Legende mit 32 Kernen macht keinen Sinn, dass es nicht in den Graphen vernueftig passt.
# legend_cpu = ax_cpu.legend(loc='lower right', fontsize='small')
# for line in legend_cpu.get_lines():
#   line.set_linewidth(4.0)

# Farben und Werte in der Legende setzen
# legend_cpu.get_texts()[0].set_text('CPU Util %')

plt.tight_layout()
# plt.show()
plt.savefig(png_plot_file)
