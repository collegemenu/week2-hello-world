# Joel Mclemore

# write a program that:
# 1. greets the user in English
# 2. asks the user to choose from 1 of 3 spoken languages (pick your favorite languages!) 
# 3. displays the greeting in the chosen language
# 4. exits

# make sure that your code contains comments explaining your logic!
while True: #While loop to prompt the user andd keep operations contained
	print('Hello! Enter Language type -- EN, DE, RU') #3 language types to choose from
	lang = input()
	if lang == 'EN, DE, RU':
			continue  #continue with the loop
	if lang == "EN": #statement for english users
	  print('Please type your name')
	  name = input()
	  print('Hello,',name ) #To be honest prof. Alfaro, I remember C# having a similar functionality and got lucky this time.
	  break
	if lang == "DE":
	  print('Bitte dein namen schreiben')
	  name = input()
	  print('Hallo,',name ) #c/p from line 9-11, auf Deutsch
	  break
	if lang == "RU":
	  print('Пожалуйста писать ваше имя')
	  name = input()
	  print('Привет,',name ) #c/p from 9-11, Pyccknñ
	  break
	exit