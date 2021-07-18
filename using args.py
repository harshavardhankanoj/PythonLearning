def check(*args):
	for x in args:
		if not(isinstance(x,(int,float))):
			return False
		return True
print(check(1,"r56"))