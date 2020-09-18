from itertools import *

def maker(x):	
	m = open("wordlist.txt","w")	
	for i in range(longm,longx + 1):
		for a in product(x,repeat = i):
			b = "".join(a)
			m.write(b+"\n")
	m.close()

def search(x):
	a = ""
	for i in x:
		if i in a:
			continue
		else:
			a += i
	return a

def bos():
	q = 0
	for i in range(longm,longx + 1):
		t = 1
		for h in range(0,i):
			t *= len(b)
		q += t 
	print("\n{} of them may take some time to print".format(q))

print(""" 
***************************
 __          __           _ _ _     _                   _             
 \ \        / /          | | (_)   | |                 | |            
  \ \  /\  / /__  _ __ __| | |_ ___| |_ _ __ ___   __ _| | _____ _ __ 
   \ \/  \/ / _ \| '__/ _` | | / __| __| '_ ` _ \ / _` | |/ / _ \ '__|
    \  /\  / (_) | | | (_| | | \__ \ |_| | | | | | (_| |   <  __/ |   
     \/  \/ \___/|_|  \__,_|_|_|___/\__|_| |_| |_|\__,_|_|\_\___|_|   
                                                                      
                       coded by cihanSrb                                                

***************************
	""")

character = input("Enter the characters you want to include: ")
longm = int(input("Enter the min length you want: "))
longx = int(input("Enter the min length you want: "))

b = ""
b = search(character)

if longx < longm :
	print("Min value greater than max value.")

else:
	bos()
	print("\nplease wait...")
	maker(b)















































