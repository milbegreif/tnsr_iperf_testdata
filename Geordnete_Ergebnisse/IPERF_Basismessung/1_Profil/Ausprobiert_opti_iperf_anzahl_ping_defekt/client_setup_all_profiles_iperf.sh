#!/bin/bash

sudo cpufreq-set -r -g performance

sudo ethtool mlx-swp29s0 rx off tx off

sudo ip addr add 172.22.24.11/24 dev mlx-swp29s0
#sudo ip route add 172.22.24.0/24 via 172.22.25.1 dev mlx-swp29s0

