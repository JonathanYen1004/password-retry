password = '1004'
i = 3
while i > 0:
	i = i - 1
	pwd = input('please enter your password: ')	
	if pwd == password:
	    print('login successfully') 
	    break
	else:
		
		print('wrong password' )
		if i > 0:
			print( i, 'more chance')
		else:
			print('delete all data')
		
			

