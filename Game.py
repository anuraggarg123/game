import random
list=['r','R','p','P','s','S']
print("LET'S PLAY ROCK-PAPER-SCISSOR GAME")
print('r or R for Rock')
print('p or P for Paper')
print('s or S for Scissor')
print()
name=input('Enter Your Name = ')
print()
num_chance=int(input('Enter number of chances you want to play = '))
user_chance=1
comp_count=0
user_count=0
while(user_chance<=num_chance):
    text=input('Enter b/w R or r, P or p, S or s= ')
    random_num=random.choice(list)

    if(text==random_num):
        print(f'you choosed {text} and computer choosed {random_num}\n')
        print('Game Draw\n')
    elif((text=='r' or text=='R') and (random_num=='p' or random_num=='P')):
        comp_count+=1
        print(f'you choosed {text} and computer choosed {random_num}\n')
        print('computer got 1 point\n')

    elif ((text == 'r' or text == 'R') and (random_num == 's' or random_num == 'S')):
        user_count+=1
        print(f'you choosed {text} and computer choosed {random_num}\n')
        print(f'{name} got 1 point\n')

    elif ((text == 'p' or text == 'P') and (random_num == 'r' or random_num == 'R')):
        user_count += 1
        print(f'you choosed {text} and computer choosed {random_num}\n')
        print(f'{name} got 1 point\n')

    elif ((text == 'p' or text == 'P') and (random_num == 's' or random_num == 'S')):
        comp_count += 1
        print(f'you choosed {text} and computer choosed {random_num}\n')
        print('computer got 1 point]\n')

    elif ((text == 's' or text == 'S') and (random_num == 'r' or random_num == 'R')):
        comp_count += 1
        print(f'you choosed {text} and computer choosed {random_num}\n')
        print('computer got 1 point\n')

    elif ((text == 's' or text == 'S') and (random_num == 'p' or random_num == 'P')):
        user_count += 1
        print(f'you choosed {text} and computer choosed {random_num}\n')
        print(f'{name} got 1 point\n')

    else:
        print(f'{name} please give right input\n')
    print(f'{num_chance - user_chance} chances left\n')
    user_chance+=1
print('chances completed\n')

 # Calculation of Scores

print('Lets see who won\n')
if(user_count==comp_count):
    print('Both have same score so match tie')
elif(user_count>comp_count):
    print(f'{name} Won and got {user_count} points')
elif(user_count<comp_count):
    print(f'computer Won and got {comp_count} points')