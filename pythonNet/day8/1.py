# a = {"name":"jack","age":'30'}
# lst = [k + "=" + v for k,v in a.items()]
# print(lst)
# print(''''C:Programe FilesPython3'.split()''')
import time
def timer(func):
	def deco():
		start = time.time()
		func()
		stop = time.time()
		print(stop-start)
	return deco

@timer
def test():
	time.sleep(2)
	print("test is running!")

# test = timer(test)

test()
