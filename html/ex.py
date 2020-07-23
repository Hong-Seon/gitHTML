import random

A = [3,2,4,3]
F = 2
M = 4

def return_f(F,result):
    number = [1,2,3,4,5,6]
    choiceList = []
    while(len(choiceList) == 0):
        choice = [random.choice(number) for i in range(F)]
        if(choice == result):
            choiceList.append(choice) 
    return choiceList

    

def function(A,F,M):
    role = len(A) + F
    result = M*role - sum(A)
    return_f(F,result)

print(function(A,F,M))