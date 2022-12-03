#!/bin/jq -Rsf

rtrimstr("\n") |
split("\n") |
map(
	explode |
	(.[0] - 65) as $theirs |
	(.[2] - 88) as $result |
	($theirs + $result + 2) % 3 |
	1 + . + 3 * $result
) |
add
