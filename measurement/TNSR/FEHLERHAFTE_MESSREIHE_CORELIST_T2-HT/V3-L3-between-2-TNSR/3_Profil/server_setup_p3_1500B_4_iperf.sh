#!/bin/bash

sudo cpufreq-set -r -g performance

sudo killall irqbalance

sudo ./set_irq_affinity.sh 12-15 mlx-swp31s0

sudo ethtool -U mlx-swp31s0 flow-type tcp4 dst-port 5002 action 12
sudo ethtool -U mlx-swp31s0 flow-type tcp4 dst-port 5003 action 13
sudo ethtool -U mlx-swp31s0 flow-type tcp4 dst-port 5004 action 14
sudo ethtool -U mlx-swp31s0 flow-type tcp4 dst-port 5005 action 15

sudo ip addr add 172.22.24.10/24 dev mlx-swp31s0
sudo ip route add 172.22.25.0/24 via 172.22.24.1  dev mlx-swp31s0
