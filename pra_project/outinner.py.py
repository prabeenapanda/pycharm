def outer():
	def inner():
		return 10
	return inner

print(outer()())
