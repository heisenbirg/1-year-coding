ONES = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
TENS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
def english(n):
	if 0 <= n < 20:
		return ONES[n]
	elif 20 <= n < 100:
		return TENS[n // 10] + (ONES[n % 10] if (n % 10 != 0) else "")
	elif 100 <= n < 1000:
		return ONES[n // 100] + "hundred" + (("and" + english(n % 100)) if (n % 100 != 0) else "")
	elif 1000 <= n < 1000000:
		return english(n // 1000) + "thousand" + (english(n % 1000) if (n % 1000 != 0) else "")
	else:
		raise ValueError()


ans = sum(len(english(i)) for i in range(1, 1001))
print(ans)
