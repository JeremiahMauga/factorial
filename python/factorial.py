def factorial(num):
	
	list = 1
	
	if type(num) == str:
		return "Please input a number"
	
	if num <= -1:
		return "Please input a non negative integer"

	for number in range(num):
		list = list * (number + 1)
	return list
