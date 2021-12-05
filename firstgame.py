print("welcome to the game!")
name = input("pls enter your name: ")
age = int(input("enter your age: "))
# print("hello",name,"you are",age,"years old")

if age >= 18:
    print("you are old enough to play")
    ques = input("do you want to play? (yes/no) ").lower()

    if ques == "yes":
        print("lets play!")
        health = 120
        print("you have",health,"health")

        ques = input("first choice, left or right? (left/right) ")
        if ques == "left":
            print("nice, you followed the path and reached a lake")
            ques = input("would you like to swim across or go around? (across/around) ")
            if ques == "around":
                print("you went around and reached the other side of the lake")
            elif ques == "across":
                print("you got across, but were bit by a fish. lost 5 health")
                health -= 5
                ques = input("you see a house and a river, which one do you go to? (river/house) ")
                if ques == "house":
                    print("you got hit by a guy at the house, lost 5 health")
                    health -= 5
                    if health <= 0:
                        print("you have 0 health and so you lose the game")
                    else:
                        print("you have survived, you win!")

                else:
                    print("you fell in the river and lost")

            else:
                print("you lost")
        else:
            print("you chose the wrong path and lost ;)")    
    else:
        print("thankyou for coming!")
else:
    print("sorry, you cannot play")
