#!/bin/jq -Rsf

split("\n\n") |
map(
	split("\n") |
	map(
		select(. != "") |
		tonumber
	) |
	add
) |
max
