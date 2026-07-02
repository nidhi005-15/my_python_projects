import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
list1=[rock,paper,scissors]
print("WE WILL PLAY ROCK PAPER SCISSORS")
user_choice=int(input(" Enter 0 to choose rock , 1 for paper , 2 for scissors: "))
print(list1[user_choice])
print("computer chose")
computer_choice=random.randint(0,2)
print(list1[computer_choice])
if user_choice>2 and computer_choice<0:
    print("invalid choice,enter 0,1 or 2")
elif user_choice==computer_choice:
    print("you draw")
elif user_choice==0 and computer_choice==2:
    print("you win")
elif user_choice==1 and computer_choice==0:
    print("you win!")
elif computer_choice>user_choice:
    print("you lose!")
elif computer_choice<user_choice:
    print("you win!")