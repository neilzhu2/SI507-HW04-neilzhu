def ask_8_ball():
    question = input("What's your Y/N question?")
	number=randrange(1,21,1)
	if(number == 1):
		print("It is certain")
	elif(number == 2):
		print("It is decidedly so")
	elif(number == 3):
		print("Without a doubt")
	elif(number == 4):
		print("Yes definitely")
	elif(number == 5):
		print("You may rely on it")
	elif(number == 6):
		print("As I see it, yes")
	elif(number == 7):
		print("Most likely")
	elif(number == 8):
		print("Outlook good")
	elif(number == 9):
		print("Yes")
	elif(number == 10):
		print("Signs point to yes")