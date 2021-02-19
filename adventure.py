import time 

print("Welcome to my first game!")

hp = 10

print("This is an adventure game, please enter the following:")

name = input("Enter your name: ").lower()
age = int(input("Enter your age: "))
gender = input("Enter your gender (male/female): ")    

print("Your name is", name,",", "your age is" , age , ",", "and you are ",gender )
time.sleep(2)

time.sleep(2)
print("You will begin the game with",hp,"health points")
time.sleep(2)
  
cont_inue = input("Would you like to continue? (yes/no) ").lower()

if cont_inue == "yes":
  print("Let's play a game then...")
  time.sleep(3)

  print("It is a cold winter day in The Yester Region, you were traveling south towards The Spirit Forest when you stumbled into an Empire ambush. You were caught along with a squad of rebels and took a blow to the head.....")
  time.sleep(1)
  print("You lose 2 health")
  hp -= 2
  time.sleep(2)

  progress = input("Type yes to continue (yes): ")
  if progress == "no":
      print("GAME OVER...... GOODBYE!")
  elif progress == "yes":
      print(" Brunaulf: You're finally awake....")
      time.sleep(3)

      print(" Brunaulf: You took a mighty blow to the head.")
      time.sleep(3)

      print(" You: What? Who are you?")
      time.sleep(3)

      print(" Brunaulf: My name is Brunaulf. My men and i rescued you from the Empire's clutches. ")
      time.sleep(4)

      print(" Brunaulf: whats your name son? ")
      time.sleep(3)

      print("*low groan* I'm ", name)
      time.sleep(3)
        #maybe add some other dialogue here
      print("A volley of arrows come down from the sky and kill a couple of the rebels around you. Brunaulf yells Let's go",name)
      time.sleep(5)

      ans = input("Do you follow Brunaulf or run off on your own? (follow/run)")
        
      if ans == "follow":
            print("You chose to follow Brunaulf and escape to the mountains in the Yester Region.....")
            time.sleep(5)
            print("Once in the mountains, you walk up a winding heavily wooded pass to a secret rebel camp.")
            time.sleep(5)
            print("Once there Brunaulf takes you to the General's tent to meet him......")
            time.sleep(5)
            print("as you enter the tent you see a rather tall man, with a dark beard.")
            time.sleep(5)
            print("Brunaulf: General Stonn, this is",name,"he fell into an ambush along with our other squad at the border sir....")
            time.sleep(5)
            print("General Stonn: Well then, how old are you",name,"?")
            time.sleep(3)
            print("You: I'm",age,"sir.")
            time.sleep(3)
            print("General Stonn: Lets talk about what occured at the border over a few drinks shall we?")
            time.sleep(10)
            print(
                "After you and the General's conversation is over, he tells Brunaulf to take you to mess hall and then to the barracks to sleep."
            )
            time.sleep(3)
            print(
                "You eat a hearty meal of pork and beans and head to the barracks to go to sleep...."
            )
            time.sleep(3)
            print("You awake at dawn feeling refreshed!")
            time.sleep(1)
            print("Your health is restored to full!")
            hp += 2
            time.sleep(5)
            print("You walk out of the barracks and are greeted by Brunaulf!")
            time.sleep(3)
            print("Brunaulf: Good morning", name,
                  "The General wants to speak with you.")
            time.sleep(3)
            print("You go to the General's tent. ")
            time.sleep(3)
            print(
                "When you arrive the general already has a drink poured for the both of you."
            )
            time.sleep(3)
            print(
                "General Stonn: Sit down, i have something id like to ask you."
            )
            time.sleep(3)
            ans = input(
                "I would like to recruit you to fight for the cause against the empire. What do you say? (Yes/no)"
            )
            if ans == "yes":
                print(
                    "I knew you'd say yes! Now for your fist assignment, i want you to go with Brunaulf on a scouting mission around the border or Spirit forest."
                )
                time.sleep(5)
                print(
                    "You, Brunaulf and several others travel back to the border of the spirit forst where you were captured."
                )
                time.sleep(3)
                print("You arrive at the edge of a cliff.")
                ans = input(
                    "Do you rapel down or find another way down? (rapel/another way)"
                )
                if ans == "rapel":
                    print(
                        "You rapel down, but halfway down your rope breaks and you fall 10 feet...."
                    )
                    time.sleep(1)
                    print("You lost 5 health")
                    hp -= 5
                    time.sleep(1)
                    print("You now have ", hp, "health")
                elif ans == "another way":
                    print(
                        "You found a path hidden in some brush to make your way down."
                    )
                time.sleep(5)
                print("You have reached the bottom of the cliff as nightfall aproaches.")
                ans = input("Would you like to set up camp or continue to the border? (camp/continue): ")
                if ans == "camp":
                    print("You set up camp, eat a nice hot meal and go to sleep....")
                    hp += 5
                    print("You wake up feeling refreshed!")
                    time.sleep(2)
                    print("Your health has been restored to Full!")
                    time.sleep(3)
                    print("You continue to the border after cleaning up camp with Brunaulf and the others...")
                elif ans == "continue":
                    print("You, Brunaulf and the other continue through the night to the border...")
                time.sleep(3)
                print("You, Brunaulf and the others arrive at the border of the spirit forest and see an empire encampment... ")
                time.sleep(3)
                ans = input("Would you like to attempt to sneak around or would you like to charge in? (sneak/charge)")
                if ans == "sneak":
                    print("You successfully sneak past the empire encampent!")
                    time.sleep(3)
                    print("Brunaulf: We should report back to the General about this encampment!")
                    time.sleep(3)
                    print("You travel back to the encampment and debrief with General Stonn...")
                    time.sleep(3)
                    print("Tahnk you for playing my first game! I know it is not much, but it took me 8 hours to code all of this.")
                elif ans == "charge":
                    print("You Charge into battle! But you are struck from behind and lose 5 health!")
                    
                    if hp <= 0:
                        print("You have no health remaining and die from your injuries!")
                        print("Game over!")
                    elif hp >= 1:
                        print("You have survived the battle!")
                        print("Brunaulf: You fought hard",name,"Now we shall return to the base to report in to General Stonn....")
                        time.sleep(3)
                        print("You travel back to the encampment and debrief with General Stonn...")
                        time.sleep(3)
                        print("Thank you for playing my first game! I know it is not much, but it took me 8 hours to code all of this.")
                


            else:
                print("I'm sorry to hear that, you already know too much....")
                time.sleep(5)
                print(
                    "*General Stonn nods* You are struck down from behind and die...."
                )
                time.sleep(3)
                print("GAME OVER!")

            
                       
             
              
      else:
          print("You take off in the other direction... and are pursued by several Empire soldiers..... as you are running you trip over some roots and a struck down by the soldiers....")
          time.sleep(5)
          print("YOU DIED")
          print("GAME OVER")
    



else:
  print("Sorry to hear that, goodbye!") 
    