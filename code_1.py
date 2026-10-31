#Rock Paper Scissor Game
import random
item_list=["Rock","Scissor","Paper"]
user_choice = input("Enter your choice: ")
comp_choice=random.choice(item_list)
print(f"Use Choice={user_choice} , Computer Choice={comp_choice}")
if (user_choice==comp_choice):
    print("Math Tie")
elif (user_choice == "Rock"):
    if(comp_choice=="Paper"):
        print("Paper covers,COMP WINS!!")
    else:
        print("Rock smashed Scissor,YOU WON!!")
elif(user_choice=="Paper"):
    if(comp_choice=="Scissor"):
        print("Scissor cuts Paper,COMP WINS!!") 
    else:
        print("Paper covers Rock,YOU WON!!")
elif(user_choice=="Scissor"): 
    if(comp_choice=="Rock"):
        print("ROck smashed Scissor,COMP WINS!!")   
    else:
        print("Scissor cuts Paper,YOU WON!!")


  
  
























