import time
import os

def menu():

    inTime = [0,0,0,0]

    # Choose how many rounds
    while True:
        try:
            inTime[0] = input("Number of rounds: ")
            break
        except:
            print("Input numbers only")
            print("---")

    # Choose duration
    while True:
        try:
            inTime[1] = input("Hours: ")
            break
        except:
            print("Input numbers only")
            print("---")

    while True:
        try:
            inTime[2] = input("Minutes: ")
            break
        except:
            print("Input numbers only")
            print("---")

    while True:
        try:
            inTime[3] = input("Seconds: ")
            break
        except:
            print("Input numbers only")
            print("---")

    print(inTime)

    with open("gym-timer/saveFile.txt","w") as saveFile:
        saveFile.writelines("%s\n" % number for number in inTime)

    saveFile.close()
    
    print(inTime)

# Choose rest, rest must be > 3 sec so that it can rest -= 3


def clock():

    menu()

    with open("gym-timer/saveFile.txt","r") as saveFile:
        curTime = saveFile.read()

    saveFile.close()

    print(f"curTime: {curTime}")

    curTime = list(map(int, curTime))

    round_num = curTime[0]
    hours = curTime[0]
    minutes = curTime[1]
    seconds = curTime[2]
    restHours = curTime[3]
    restMinutes = curTime[4]
    restSeconds = curTime[5]

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

        if seconds < 0 and minutes == 0 and hours == 0 and round_num == 0:
            print("time's up")
            break

clock()

# Go again, new clock or exit

# Could be cool to make this a SBG themed clock with motivational quotes from SBG athletes

# Create presets