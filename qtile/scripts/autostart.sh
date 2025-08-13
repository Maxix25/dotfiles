#!/usr/bin/env bash
# ---
# Use "run program" to run it only if it is not already running
# Use "program &" to run it regardless
# ---
# NOTE: This script runs with every restart of AwesomeWM
# TODO: run_once


function run {
    if ! pgrep $1 > /dev/null ;
    then
        $@&
    fi
}

run discord &
run brave &
xrandr --output VGA-0 --off --output VGA-1 --off --output HDMI-0 --mode 1360x768 --pos 1920x180 --rotate normal --output DVI-D-0 --primary --mode 1920x1080 --pos 0x0 --rotate normal
run nitrogen --restore &
run xfce4-clipman
run xfce4-power-manager
