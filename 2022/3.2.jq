#!/bin/jq -Rsf

rtrimstr("\n") |
split("\n") |
. as $input |
[range(0; length; 3)] |
map(
	# for each group of 3
	$input[.:.+3] |
	# unique each one, then put them all together
	map(
		explode |
		unique
	) |
	add |
	# filter to only items with exactly 3 occurances
	group_by(.) |
	.[] |
	select(length == 3) |
	.[0] |
	# convert to priority
	if . >= 97 then
		1 + . - 97
	else
		27 + . - 65
	end
) |
add
