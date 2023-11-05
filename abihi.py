def timer_logo():
    import time
    def countdown(t):
    
        while t:
           mins, secs = divmod(t, 60)
           timer = '{:02d}:{:02d}'.format(mins, secs)
           print(timer, end="\r")
           time.sleep(1)
           t -= 1
      
    print('time out!!')
  
  
# input time in seconds
    t = input("Enter the time in seconds: ")
  
# function call
    countdown(int(t))
timer_logo()


print("enter no of project you need to go\n")
while 1:
    print("1 for timer \n2 for insta \n3 for guess game \n4 for exit ")
    x=int("enter the choice")
    if x==1:
        timer_logo()
    elif x==2:
        instagram_logo()
    elif x==3:
        guess_game()
    elif x==4:
        quit()
    else:
        print("enter valid choice")


        