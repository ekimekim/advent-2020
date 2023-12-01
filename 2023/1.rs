use std::io::{stdin, Read};

const DIGITS: [&[u8]; 9] = [b"one", b"two", b"three", b"four", b"five", b"six", b"seven", b"eight", b"nine"];

fn main() {
	let mut input: Vec<u8> = Vec::new();
	let mut buf = stdin().lock();
	buf.read_to_end(&mut input).unwrap();
	
	let result: usize = input.as_slice().split(|c| *c as char == '\n').filter(|line| line.len() > 0).map(|line| {
		let mut first: Option<usize> = None;
		'first: for (i, c) in line.iter().enumerate() {
			let as_digit: u8 = c - ('0' as u8);
			if as_digit < 10 {
				first = Some(as_digit.into());
				break;
			}
			let slice = &line[i..];
			for (n, word) in DIGITS.into_iter().enumerate() {
				if slice.starts_with(word) {
					first = Some(n+1);
					break 'first;
				}
			}
		}

		let mut last: Option<usize> = None;
		'last: for (i, c) in line.iter().enumerate().rev() {
			let as_digit: u8 = c - ('0' as u8);
			if as_digit < 10 {
				last = Some(as_digit.into());
				break;
			}
			let slice = &line[..=i];
			for (n, word) in DIGITS.into_iter().enumerate() {
				if slice.ends_with(word) {
					last = Some(n+1);
					break 'last;
				}
			}
		}

		10 * first.unwrap() + last.unwrap()
	}).sum();
	println!("{}", result)
}
