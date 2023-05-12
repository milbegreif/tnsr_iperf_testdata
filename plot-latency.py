import argparse

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import re
from pandas import Series

parser = argparse.ArgumentParser(description='Plot data from JSON file')
parser.add_argument('filename', type=str, help='Path to the JSON file')
args = parser.parse_args()
filename = args.filename

txt_data_file = filename
png_plot_file = filename.replace('txt', 'png')

time = []

# Lese Datei ein
with open(txt_data_file, "r") as f:
    for line in f:
        match = re.search(r"time=(\d+\.\d+)", line)
        if match:
            time.append(float(match.group(1)))
latency: Series = pd.Series(time)

# Berechne max, min, avg und Jitter
latency_max = latency.max()
latency_min = latency.min()
latency_avg = latency.mean()
latency_jitter = latency.std()

# Erstelle eine Figure und ein Axes Objekt
fig, ax = plt.subplots()

# x-Achse erstellen
x = np.arange(0, len(latency), 1)

# Plotte die Latenzzeiten als Linie
ax.plot(x, latency, label="Latency")

# Plotte die Linien für min, max, avg und Jitter
ax.axhline(latency_min, color="r", linestyle="--", label="Min")
ax.axhline(latency_max, color="g", linestyle="--", label="Max")
ax.axhline(latency_avg, color="b", linestyle="--", label="Avg")
ax.axhline(latency_avg + latency_jitter, color="m", linestyle="--", label="Jitter")

# Füge eine Legende hinzu
ax.legend()

# Setze die Titel und Achsenbeschriftungen
ax.set_title("Latency")
ax.set_xlabel("Zeit")
ax.set_ylabel("Latenz (ms)")

ax.set_ylim([0, latency.max() * 1.1])

# Speichere Plot als PNG
plt.savefig(png_plot_file)
