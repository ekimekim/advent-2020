#!/bin/jq -Rsf

rtrimstr("\n") |
split("\n") |
map(
	(.|length) as $len |
	(.[:$len/2] | explode) as $left |
	.[$len/2:] |
	explode |
	.[] |
	select([.]|inside($left)|not) |
	if . >= 97 then
		. - 97
	else
		. - 41
	end
) |
add
