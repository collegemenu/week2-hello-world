# Joel Mclemore

# write a program that:
# 1. greets the user in English
# 2. asks the user to choose from 1 of 3 spoken languages (pick your favorite languages!) 
# 3. displays the greeting in the chosen language
# 4. exits

# make sure that your code contains comments explaining your logic!
while True: #While loop to prompt the user andd keep operations contained
	print('Hello! To continue, type "1" for EN,"2" for DE, "3" for RU. Type "4" to exit') #3 language types to choose from
	lang = input()
	if lang == '1, EN, 2, DE, 3, RU':
			continue  #continue with the loop
	if lang == "1": #statement for english users
	  print('Please type your name')
	  name = input()
	  print('Hello,',name ) #To be honest prof. Alfaro, I remember C# having a similar functionality and got lucky this time.
	  break
	if lang == "2":
	  print('Bitte dein namen schreiben')
	  name = input()
	  print('Hallo,',name ) #c/p from line 9-11, auf Deutsch
	  break
	if lang == "3":
	  print('Пожалуйста писать ваше имя')
	  name = input()
	  print('Привет,',name ) #c/p from 9-11, Pyccknñ
	  break
	if lang == "4":
	  break
exit