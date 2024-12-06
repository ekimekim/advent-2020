fn main() -> Result<(), String> {
	println!("{}", day1()?);
	Ok(())
}

fn day1() -> Result<usize, String> {
	std::io::stdin().lines()
		.enumerate()
		.map(|(n, result)| match result {
			Ok(line) => match line.parse::<usize>() {
				Ok(fuel) => Ok(fuel / 3 - 2),
				Err(e) => Err(format!("Line {n} parse error: {e}")),
			},
			Err(e) => Err(format!("Line {n} IO error: {e}")),
		})
		.sum()
}
