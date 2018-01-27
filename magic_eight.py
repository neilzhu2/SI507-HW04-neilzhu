def ask_8_ball():
  isNotQ = 1

  while isNotQ:	
    question = input("What's your Y/N question?")

    if question != "quit":
    	if question[-1] == "?":
    		isNotQ = 0
    		return question
    	else:
    		print("I’m sorry, I can only answer questions.")

    else:
    	break

  if isNotQ == 0:
		number=randrange(1,21,1)
		if(number == 11):
			print("Reply hazy try again")
		elif(number == 12):
			print("Ask again later")
		elif(number == 13):
			print("Better not tell you now")
		elif(number == 14):
			print("Cannot predict now")
		elif(number == 15):
			print("Concentrate and ask again")
		elif(number == 16):
			print("Don't count on it")
		elif(number == 17):
			print("My reply is no")
		elif(number == 18):
			print("My sources say no")
		elif(number == 19):
			print("Outlook not so good")
		elif(number == 20):
			print("Very doubtfu")

