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
