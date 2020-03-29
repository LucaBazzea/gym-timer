import time
import os

hours = int(0) 
minutes = int(0)
seconds = int(0)

# Choose how many rounds
while True:
    try:
        round_num = int(input("Number of rounds: "))
        break
    except:
        print("Input numbers only")
        print("---")

# Choose duration
while True:
    try:
        hours = int(input("Hours: "))
        break
    except:
        print("Input numbers only")
        print("---")

while True:
    try:
        minutes = int(input("Minutes: "))
        break
    except:
        print("Input numbers only")
        print("---")

while True:
    try:
        seconds = int(input("Seconds: "))
        break
    except:
        print("Input numbers only")
        print("---")

# Choose rest, rest must be > 3 sec so that it can rest -= 3

'''for i in range(seconds):
    print("seconds: " + str(seconds - i))
    time.sleep(1)'''

while seconds > -1:
    os.system("cls")
    time_left = str(hours).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2)
    print(time_left)
    
    if seconds < 1 and minutes >= 1:
        minutes -= 1
        seconds = 59

    if minutes < 1 and hours >= 1:
        hours -= 1
        minutes = 59

    time.sleep(1)
    seconds -= 1
    os.system("cls")


# Go again, new clock or exit





# Could be cool to make this a SBG themed clock with motivational quotes from SBG athletes

# Create presets