import random

num = random.randrange(1000, 10000)

n = int(input("Guess the 4 digit number:"))

if(n == num):
    print("Great! You guessed the number in just 1 try! You're a Mastermind!")
else:
    
    ctr = 0

    while(n != num):
        
        ctr += 1
        count = 0
        n = str(n)
        num = str(num)
        correct = []

        for i in range(0, 4):
           
            if(n[i] == num[i]):
               
                count += 1
               
                correct.append(n[i])
            else:
                continue

        
        if (count < 4) and (count != 0):
            print("Not quite the number. But you did get ",
                  count, " digit(s) correct!")
            print("Also these numbers in your input were correct.")

            for k in correct:
                print(k, end=' ')
            print('\n')
            print('\n')
            n = int(input("Enter your next choice of numbers: "))

        
        elif(count == 0):
            print("None of the numbers in your input match.")
            n = int(input("Enter your next choice of numbers: "))

    if n == num:
        print("You've become a Mastermind!")
        print("It took you only", ctr, "tries.")
              
        

