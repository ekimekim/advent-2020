fn main() -> Result<(), String> {
	println!("{}", day1()?);
	Ok(())
}

fn day1() -> Result<usize, String> {
	std::io::stdin().lines()
		.enumerate()
		.map(|(n, result)| match result {
			Ok(line) => match line.parse::<usize>() {
				Ok(module_mass) => Ok(
					std::iter::successors(Some(module_mass),
						|mass| (mass / 3).checked_sub(2)
					).skip(1).sum::<usize>()
				),
				Err(e) => Err(format!("Line {n} parse error: {e}")),
			},
			Err(e) => Err(format!("Line {n} IO error: {e}")),
		})
		.sum()
}
