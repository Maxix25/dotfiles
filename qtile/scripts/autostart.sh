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

run xinput set-prop 9 342 1
run xinput set-prop 9 297 1
run xinput set-prop 9 324 1
run picom -CGb &
run discord &
run brave &
run nitrogen --restore & 
run xfce4-clipman
run xfce4-power-manager
