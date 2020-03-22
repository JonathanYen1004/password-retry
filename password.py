password = '1004'
i = 3
while True:
	pwd = input('please enter your password: ')	
	if pwd == password:
	    print('login successfully') 
	    break
	else:
		i = i - 1
		print('wrong password' , i, 'more chance' )
		if i == 0:
			break

