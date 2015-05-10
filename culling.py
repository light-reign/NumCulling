def main():
	input_file = open('data.txt', 'r')
	if not input_file.closed:
		lines = input_file.readlines()
		input_file.close()
		num_arr = []

		for idx in range(0, len(lines)):
			nums = lines[idx].split()
			for num in nums:
				num_arr.append(int(num))	
		if len(num_arr) > 0:
			num_arr.sort()
			last = num_arr[0]
			print last,

			for idx in range(1, len(num_arr)):
				if num_arr[idx] != last:
					last = num_arr[idx]
					print last,
	

main()
