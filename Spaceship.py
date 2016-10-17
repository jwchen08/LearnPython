#coding=uft-8
import time
shipName="USSA"
captain="cjw"
location="Earth"
password="password"
pAttempt=raw_input("Enter the password:")
while pAttempt!=password:
    print "Password is incorrect!"
    pAttempt=raw_input("Enter the password:")
print "Password correct. Welcome to the "+shipName
print ""
print "The spaceship "+shipName+" is currently visiting "+location+"."
choice=""
while choice!="/exit":
    print "What would you like to do, "+captain+"?"
    print ""
    print "a. Travel to another planet"
    print "b. Fire cannons"
    print "c. Open the airlock"
    print "d. Self-destruct"
    print "/exit to exit"
    print ""
    choice=raw_input("Enter your choice: ")
    if choice=="a":
        print "Leaving "+location
        print "Travelling to Mars"
    elif choice=="b":
        print "Fire cannons"
    elif choice=="c":
        print "Opening airlock"
    elif choice=="d":
        confirm=raw_input("Are you sure you want the ship to self-destruct?(y/n)")
        if confirm=="y":
            print "Ship will self-destruct in"
            print "3"
            time.sleep(1)
            print "2"
            time.sleep(1)
            print "1"
            time.sleep(1)
            print "Goodbye"
            print "BOOM!!!"
            choice="/exit"
    elif choice=="/exit":
        print "Goodbye"
    else:
        print "Invalid input. Please select a, b, c, or d. /exit to exit"
