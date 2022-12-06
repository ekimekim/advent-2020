#!/bin/jq -Rsf

rtrimstr("\n") |
split("\n") |
map(
	(.|length) as $len |
	(.[:$len/2] | explode) as $left |
	.[$len/2:] |
	explode |
	unique |
	.[] |
	select([.]|inside($left)) |
	if . >= 97 then
		1 + . - 97
	else
		27 + . - 65
	end
) |
add
