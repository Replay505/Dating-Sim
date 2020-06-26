#print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
#print("█                            █")
#print("█                            █")
#print("█                            █")
#print("█                            █")
#print("█                            █")
#print("█                            █")
#print("█                            █")
#print("█                            █")
#print("█                            █")
#print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")

import keyboard
import time

print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
print("█                            █")
print("█                            █")
print("█                            █")
print("█                            █")
print("█         WELCOME TO:        █")
print("█       [ Date Night ]       █")
print("█                            █")
print("█                            █")
print("█      Press 1 to Start      █")
print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")

def game():
	#creating variables
	feeling = "normal"
	feelingCount = 0
	ending = 0
	turnCount = 1
	eyes = "▄  ▄"
	mouth = "▄▄▄▄"

	#ingame variable checks
	weatherTopic = False
	dayTopic = False

	while turnCount <= 5:

		if feelingCount >= 3 and feelingCount <= 4:
			eyes = "^  ^"
			mouth = "▀▄▄▀"
			feeling = "delighted"
		if feelingCount >= 1 and feelingCount <= 2:
			eyes = "^  ^"
			mouth = "▄▄▄▄"
			feeling = "comfortable"
		if feelingCount == 0:
			eyes = "▄  ▄"
			mouth = "▄▄▄▄"
			feeling = "normal"
		if feelingCount <= -1 and feelingCount >= -2:
			eyes = "┬  ┬"
			mouth = "▄▄▄▄"
			feeling = "bored"
		if feelingCount <= -3 and feelingCount >= -4:
			eyes = "┬  ┬"
			mouth = "▄▀▀▄"
			feeling = "upset"

		print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
		print("█                            █")
		print("█                            █")
		print("█           ▄▀▀▀▀▄           █")
		print("█          █", eyes, "█          █")
		print("█         █ ", mouth, " █         █")
		print("█          ▀▄▄▄▄▄▄▀          █")
		print("█        ▄▀▀░▀▄▄▀░▀▀▄        █")
		print("█       █░░░░░░░░░░░░█       █")
		print("█    ▄▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▄    █")
		print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
		print("Your partner looks", feeling, ".")
		if (feelingCount >= 5): print("They're ecstatic to be here!")
		if (feelingCount <= -5): print("They're hating this date so far...")
		print("------------------------------")
		if turnCount == 5:
			print("The waiter brings your food out to you.")
			print("How would you like to eat it?")
			print("1: Like a normal person. 2: With your hands. 3: Share it with your partner.")

			x = str(input())
			clearScreen()
			print("You take a bite...")
			time.sleep(1)
			print("...")
			time.sleep(1)
			print("...")
			time.sleep(1)
			turnCount = 6

		if turnCount == 4:
			print("The waiter comes back to you to take your order.")
			print("What would you like to order?")
			print("1: Burger. 2: Fish. 3: Salad")

			x = str(input())
			if x == "1":
				clearScreen()
				print("You ordered the burger, but it turns out your partner is vegan...")
				print("I mean, who knew? They definitely disliked that though. They order some fish.")
				feelingCount -= 2
				turnCount += 1
			elif x == "2":
				clearScreen()
				print("You ordered some fried fish, and your partner orders it as well!")
				print("You both mutually agree on your love for cooked sealife! Like two peas in a pod!")
				feelingCount += 2
				turnCount += 1
			elif x == "3":
				clearScreen()
				print("I guess this is ok. Salads are ok.")
				print("Your partner orders a fish and thinks nothing of your meal choice.")
				turnCount += 1
			else: 
				clearScreen()
				print("Uhhhh... thats not an option...")

		if turnCount == 3:
			print("The waiter comes up to the table to ask for what drinks you want.")
			print("What would you like to drink?")
			print("1: Water. 2: Soda. 3: Wine")

			x = str(input())
			if x == "1":
				clearScreen()
				print("You decided to drink water. Its safe... a little too safe.")
				print("Feeling pressured into ordering water also, your partner does the same. You're no fun.")
				feelingCount -= 1
				turnCount += 1
			elif x == "2":
				clearScreen()
				print("You ordered some soda! AW YEAH!")
				print("Who doesn't love some good ol' soda? Your partner orders soda, too!")
				print("You bond over a common love for carbonated sugar beverages!")
				feelingCount += 2
				turnCount += 1
			elif x == "3":
				clearScreen()
				print("Wine? For your first date? Who do you think you are")
				print("You must be stupid. Your partner orders water and gives you some stink eye.")
				feelingCount -= 2
				turnCount += 1
			else: 
				clearScreen()
				print("Uhhhh... thats not an option...")

		if turnCount == 1 or turnCount == 2:
			if turnCount == 1: print("The night has just started. You both are sitting at the table, so lets get going.")
			print("Well? What would you like to talk about?")
			print("1: The weather. 2: How their day has been. 3: Screw that, let's order.")
	
			x = str(input())
			if x == "1":
				clearScreen()
				if weatherTopic == True:
					print("You've already talk about this topic...")
				else:
					weatherTopic = True
					print("Wow. Super original. I mean, I guess its a good start?")
					print("You talk with your partner about the weather. Its so cliche and the conversation\n",
						"ends in two or three sentences... Nice job.")
					feelingCount -= 1
					turnCount += 1
			elif x == "2": 
				clearScreen()
				if dayTopic == True:
					print("You've already talk about this topic...")
				else:
					dayTopic = True
					print("Your partner talks about how they got fired from their job today. Yikes")
					print("They didn't restock the printer with paper, and sent their boss over the edge...")
					print("What do you say to that?")
					print("1: Console your partner. 2: Say derogatory things about the boss that fired them.")
				
					y = str(input())
					if y == "1":
						clearScreen()
						print("They liked that. Like a lot! Well thats good to hear!")
						feelingCount += 2
					if y == "2":
						clearScreen()
						print("Turns out their boss is also their dad... \n Nice job. You cussed out your partner's dad.")
						feelingCount -= 2
					turnCount += 1
			elif x == "3":
				clearScreen()
				print("Wait don't you want to talk to your new partner?")
				print("1: Yes 2: No")

				y = str(input())
				if y == "2":
					clearScreen()
					print("Your partner REALLY didn't like that and leaves the table. \nWere you just here for the food from the beginning?")
					ending = 1
					endScreen(ending)
			else:
				clearScreen()
				print("Uhhhh... thats not an option...")

	if turnCount == 6:
		print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
		print("█                            █")
		print("█                            █")
		print("█           ▄████▄           █")
		print("█          ██o█████          █")
		print("█         ██████o███         █")
		print("█          ▀██████▀          █")
		print("█        ▄▀▀░▀▄▄▀░▀▀▄        █")
		print("█       █░░░░░░░░░░░░█       █")
		print("█    ▄▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▄    █")
		print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
		print("'Hello friend.'")
		time.sleep(3)
		if feelingCount >= 0:
			print("'I've been enjoying our time thus far...'")
			time.sleep(1)
			print("'Have you?'")
			print("1: Whats going on? 2: Where are we?")

			x = str(input())

			print("'S")
			for y in range(5):
				time.sleep(.5)
				print("h")
			print(".'")
			time.sleep(1)
			print("'Just keep treating me right.'")
			time.sleep(3)

			clearScreen()
			print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
			print("█                            █")
			print("█                            █")
			print("█           ▄████▄           █")
			print("█          ██o█████          █")
			print("█         ██████o███         █")
			print("█          ▀██████▀          █")
			print("█        ▄▀▀░▀▄▄▀░▀▀▄        █")
			print("█       █░░░░░░░░░░░░█       █")
			print("█    ▄▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▄    █")
			print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
			print("'Here. Let me give you a hint, honey.'")
			time.sleep(1.5)
			print("'1593'")
			time.sleep(1.5)
			print("'Get on my bad side, and when you can ask who I am, type this in...'")
			time.sleep(4)
			print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
			print("█                            █")
			print("█                            █")
			print("█           ▄████▄           █")
			print("█          ██o█████          █")
			print("█         ██▀███o███         █")
			print("█          ▀█▄▄███▀          █")
			print("█        ▄▀▀░▀▄▄▀░▀▀▄        █")
			print("█       █░░░░░░░░░░░░█       █")
			print("█    ▄▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▄    █")
			print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
			print("'I'll see you on the other side, honey.")
			ending = 3
			endScreen(ending)

		else:
			print("'This sure has been fun'")
			time.sleep(1)
			print("'But I'm quite fed up with you.'")
			print("1: Who are you? 2: What just happened?")

			x = str(input())
			if x == "1593":
				turnCount = 7
			else:
				print("No more questions.")
				time.sleep(2)
				print("No more choices.")
				time.sleep(3)
				clearScreen()
				print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
				print("█                            █")
				print("█                            █")
				print("█           ▄████▄           █")
				print("█          ██o█████          █")
				print("█         ███ ██o███         █")
				print("█          ▀████ █▀          █")
				print("█        ▄▀▀░▀▄▄▀░▀▀▄        █")
				print("█       █░░░░░░░░░░░░█       █")
				print("█    ▄▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▄    █")
				print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
				print("What matters is that I never see you again.")
				time.sleep(3)
				ending = 2
				clearScreen()
				endScreen(ending)

	if  turnCount == 7:
		print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
		print("█                            █")
		print("█                            █")
		print("█           ▄████▄           █")
		print("█          ██o█████          █")
		print("█         ██████o███         █")
		print("█          ▀██▄███▀          █")
		print("█        ▄▀▀░▀▄▄▀░▀▀▄        █")
		print("█       █░░░░░░░░░░░░█       █")
		print("█    ▄▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▄    █")
		print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
		print("'Oh...?'")
		time.sleep(3)
		print("'So... you know me, don't you...'")
		time.sleep(3)
		clearScreen()
		print("'That...'")
		time.sleep(3)

		clearScreen()
		print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
		print("█                            █")
		print("█                            █")
		print("█           ▄▀▀▀▀▄           █")
		print("█          █ ╭  ╮ █          █")
		print("█         █   ╰╯   █         █")
		print("█          ▀▄▄▄▄▄▄▀          █")
		print("█        ▄▀▀░▀▄▄▀░▀▀▄        █")
		print("█       █░░░░░░░░░░░░█       █")
		print("█    ▄▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▄    █")
		print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
		print("'That makes me quite happy!'")
		time.sleep(3)
		print("'You spent all that time just to see who I really am!'")
		time.sleep(1)
		print("'Thank you!'")
		time.sleep(3)
		ending = 4
		clearScreen()
		endScreen(ending)

def endScreen(endingEnd):
	if endingEnd == 1:
		print("You literally just ate dinner by yourself... Nice job, I guess...")
		print("YOU GOT: Ending 1 out of 4: Dinner Alone")
	if endingEnd == 2:
		print("YOU GOT: Ending 2 out of 4: It wasn't working out, I guess...")
	if endingEnd == 3:
		print("You made a new friend! Nice!")
		print("YOU GOT: Ending 3 out of 4: 1593")
	if endingEnd == 4:
		print("YOU GOT: Ending 4 out of 4: True Ending")

	print("\nPlay again?")
	print("1: Yes 2: No")

	x = str(input())
	if x == "1":
		clearScreen()
		ending = 0
		game()
	else: exit()

def clearScreen():
	x = 0
	while x != 11:
		print("")
		x += 1

x = str(input())
if x == "1":
	clearScreen()
	game()