import itertools


def compute():
	triangle = 0
	for i in itertools.count(1):
		triangle += i  
		if num_divisors(triangle) > 500:
			return str(triangle)



def num_divisors(n):
	end = int(pow(n,0.5))
	result = sum(2
		for i in range(1, end + 1)
		if n % i == 0)
	if end**2 == n:
		result -= 1
	return result


if __name__ == "__main__":
	print(compute())
