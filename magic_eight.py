def ask_8_ball():
	isNotQ = 1
	while isNotQ:
		question = input("What's your Y/N question?")
		if question != "quit":
			if question[-1] == "?":
				isNotQ = 0
				print (question)
			else:
				print("I’m sorry, I can only answer questions.")
		else:
			break

	if isNotQ == 0:
		number=randrange(1,11,1)
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
from random import randrange
ask_8_ball()