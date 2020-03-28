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
        minutes = int(input("Minutes: "))
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
    print(f"H:{hours}M:{minutes}S:{seconds}")
    time.sleep(1)
    seconds -= 1
    os.system("cls")


# Go again or new clock





# Could be cool to make this a SBG themed clock with motivational quotes from SBG athletes

# Create presets