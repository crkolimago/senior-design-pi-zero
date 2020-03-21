#!/bin/sh
#https://raspberrypi.stackexchange.com/questions/50496/automatically-accept-bluetooth-pairings
sudo bluetoothctl <<EOF
power on
discoverable on
pairable on
agent NoInputNoOutput
default-agent
EOF
