import random
snake=['gun','water','snake']
gun=['snake','water','gun']
water=['snake','gun','water']
c=0
u=0
user='snake'
print("Welcome to Snake,Gun,Water game")
print("-------------------------------------------")
while(user=='snake' or user=='gun'or user=='water'):
    user=input("Enter from the given choices:\n1.Snake\n2.Gun\n3.water\n4.Exit\n>>")
    if(user=='snake'):
        computer=random.choice(snake)
        print("\nuser->",user)
        print("Computer->",computer)
        if(computer=='gun'):
            print("Computer wins!\n")
            c=c+1
            print("Computer\tUser\n")
            print(c,"\t\t",u)
        elif(computer=='water'):
            print("User wins!\n")
            u=u+1
            print("Computer\tUser\n")
            print(c,"\t\t",u)
        else:
            print("Draw")
            print("Computer\tUser\n")
            print(c,"\t\t",u)
    elif(user=='gun'):
        computer=random.choice(gun)
        print("\nuser->",user)
        print("Computer->",computer)
        if(computer=='water'):
            print("Computer wins!\n")
            c=c+1
            print("Computer\tUser\n")
            print(c,"\t\t",u)
        elif(computer=='snake'):
            print("User wins!\n")
            u=u+1
            print("Computer\tUser\n")
            print(c,"\t\t",u)
        else:
            print("Draw")
            print("Computer\tUser\n")
            print(c,"\t\t",u)
    elif(user=='water'):
        computer=random.choice(gun)
        print("\nuser->",user)
        print("Computer->",computer)
        if(computer=='snake'):
            print("Computer wins!\n")
            c=c+1
            print("Computer\tUser\n")
            print(c,"\t\t",u)
        elif(computer=='gun'):
            print("User wins!\n")
            u=u+1
            print("Computer\tUser\n")
            print(c,"\t\t",u)
        else:
            print("Draw")
            print("Computer\tUser\n")
            print(c,"\t\t",u)
print("Computer\tUser\n")
print(c,"\t\t",u)
print("Congratulations!")
if(c>u):
    print("Computer wins!")
elif(u>c):
    print("User wins!")
else:
    print("Draw!")