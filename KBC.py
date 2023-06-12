print("Welcome to KBC!")
lst=["What is the national bird of India?","How many states are there in India?","Entomology is the science that studies..","Garampani sanctuary is located at..","For which of the following displines is Nobel Prize awarded?"]
lst2=["d","a","c","b","d"]
a=1
i=0
cs=0
for i in range(5):
    print("Question:",a)
    print(lst[i])
    match a:
        case 1:
            print("a.Piegon\tb.Parrot\nc.Sparrow\td.Peacock")
            m=input("Choose the correct option:")
            if(m==lst2[i]):
              print("It's a correct answer!")
              cs=1000
              a=a+1
              print("Your cash amount is:",cs)
              print("-------------------------------------------")
            else:
                print("Sorry.")
                print("Wrong Answer!")
                break
        case 2:
            print("a.28\tb.27\nc.29\td.25")
            m=input("Choose the correct option:")
            if(m==lst2[i]):
                print("It's a correct answer!")
                cs=2000
                a=a+1
                print("Your cash amount is:",cs)
                print("-------------------------------------------")
            else:
                print("Sorry.")
                print("Wrong Answer!")
                break
        case 3:
            print("a.Human Beings\tb.History\nc.Insects\td.Rocks")
            m=input("Choose the correct option:")
            if(m==lst2[i]):
                print("It's a correct answer!")
                cs=3000
                a=a+1
                print("Your cash amount is:",cs)
                print("-------------------------------------------")
            else:
                print("Sorry.")
                print("Wrong Answer!")
                break
        case 4:
            print("a.Gujarat\tb.Assam\nc.Nagaland\td.Sikkim")
            m=input("Choose the correct option:")
            if(m==lst2[3]):
                print("It's a correct answer!")
                cs=4000
                a=a+1
                print("Your cash amount is:",cs)
                print("-------------------------------------------")
            else:
                print("Sorry.")
                print("Wrong Answer!")
                break
        case 5:
            print("a.Physics\tb.Chemistry\nc.Literature\td.All the above")
            m=input("Choose the correct option:")
            if(m==lst2[4]):
                print("It's a correct answer!")
                cs=5000
                a=a+1
                print("-------------------------------------------")
            else:
                print("Sorry.")
                print("Wrong Answer!")
                break
if(cs==5000):
    print("Congratulation!")
    print("Your cash amount is:",cs)
else:
    print("Your cash amount is:",cs)