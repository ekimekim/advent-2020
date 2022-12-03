#!/bin/jq -Rsf

rtrimstr("\n") |
split("\n") |
map(
	explode |
	(.[0] - 65) as $theirs |
	(.[2] - 88) as $ours |
	(4 + $ours - $theirs) % 3 |
	1 + $ours + 3 * .
) |
add
