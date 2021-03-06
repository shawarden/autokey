#!/bin/bash

keyNum=$1

while :;
do
	if for id in $(
		xinput list | \
		grep -v "pointer\|master" | \
		grep keyboard | \
		awk -F'id=' '{print $2}' | \
		awk '{print $1}'
		)
	do
		xinput query-state $id
	done | grep down | grep ${keyNum} &>/dev/null
	then
		break
	fi
done
