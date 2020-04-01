import time
import os

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

while True:
    os.system("cls")
    
    time_left = str(hours).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2)
    print(time_left)
    
    time.sleep(1)
    
    if minutes == 0  and seconds == 0 and hours >= 1:
        hours -= 1
        minutes = 59

    if seconds == 0 and minutes >= 1:
        minutes -= 1
        seconds = 59

    seconds -= 1

    if seconds < 0 and minutes == 0 and hours == 0:
        print("time's up")
        break
    
    os.system("cls")


# Go again, new clock or exit





# Could be cool to make this a SBG themed clock with motivational quotes from SBG athletes

# Create presets