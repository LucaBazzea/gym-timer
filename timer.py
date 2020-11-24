import time

# input time, rounds and rest
# Add some Try Except
# Convert minutes to seconds
ti = int(input("Enter the time in seconds: "))
ro = int(input("How many rounds would you like?: "))
re = int(input("How long do you want the rest to be?: "))

def countdown(t): 
    
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1
  
while ro >= 1:

    countdown(ti)
    print("--Round Over--\n")

    if re >= 1 and ro >= 2:
        countdown(re)
        print("--Rest Over--\n")

    ro -= 1