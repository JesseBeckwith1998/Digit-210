import time 


def character():

    print("Please comeplete the following questions!")

    name = input("Please enter your name!: ")
    age = int(input("Please enter your age!: "))
    gender = input("Please enter your gender!: ")
    if gender == "male":
        stealth = 2
        strength = 8
        intellegence = 6
        charisma = 6
        hp = 10
        print("Your stats for this game will be the following:",stealth,":stealth, ",strength,":strength,",intellegence,":intellegence, ",charisma,":charisma. and your name is: ",name)

    elif gender == "female":
        stealth = 8
        strength = 2
        intellegence = 7
        charisma = 7
        hp = 5
        print("Your stats for this game will be the following:",stealth,":stealth",strength,":strength, ",intellegence,":intellegence,  ",charisma,":charisma. and your name is:",name)
    else:
        print("You have no stats! Good Luck!")
    if age >= 21:
        print("You are of legal drinking and smoking age in the state of Pennsylvania!")
    else:
        print("You are not of Legal drinking and smoking age in the state of Pennsylvania!")
    

    char_info(name,age,gender,stealth,strength,intellegence,charisma,hp)
   

#add loop in case user wants to re create character


def char_info(name,age,gender,stealth,stregnth,intellegence,charisma,hp):

    print("Your name is:",name,", Your age is:",age,", Your gender is:",gender,"and your stats are:",stealth,"Stealth:"
,stregnth,"Strength:",intellegence,"Imtellegence:",charisma,"Charisma and",hp,"health!")


character()