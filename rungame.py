import time
mydict = {
    'time_left' : 60,
    'letters_typed' : 0,
    'username' : " ",
    'total_letters_typed' : 0,
    }
mydict['username'] = input("Enter Your Name: ")
print("type 10 letters at a time")
time.sleep(3)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("TYPE!")
while mydict['time_left'] > 0:
    mydict['letters_typed'] = len(input("input: "))
    if mydict['letters_typed'] == 10:
        mydict['total_letters_typed'] += mydict['letters_typed']
        print("valid")
        print("Loading...")
        time.sleep(5)
        mydict['time_left'] -=5
    else:
        print("you lose. game over.")
        break
    
print("TOTAL LETTERS TYPED:  ")
print(mydict["total_letters_typed"])
print("good job %s"  %mydict["username"])
    
    
    
