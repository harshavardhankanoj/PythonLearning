Secret_code="Harsha"
Guess=""
guess_count=0
guess_limit=3
out_of_guesses=False
while Guess!=Secret_code and not(out_of_guesses):
	 if guess_count<guess_limit:
	 	Guess=input("Enter the code:")
	 	guess_count+=1
	 else:
	 	out_of_guesses=True
if out_of_guesses:
	print ("you lose")
else:
	print ("you won!")