from os import system as sys
from time import sleep
import random

start = int(input("Enter Starting Roll No.: "))
stop = int(input("Enter Ending Roll No.: "))
no_grp = int(input("Enter Number of Groups: "))
section = input("Enter Section (A or B): ")         # 'A' or 'B'  Group Names will be like A1, A2, ... or B1, B2, ...
runs = int(input("Enter Number of Iterations: "))   # Number of iterations tells how many times will the code run

std_lst = list(range(start,stop+1))
no_per_grp = int(len(std_lst)/no_grp)

for r in range(runs):
    random.shuffle(std_lst)
    grps = {}

    for i in range(no_grp):
        grp = random.sample(std_lst,no_per_grp)
        grps[section+str(i+1)] = grp
        std_lst = list(set(std_lst)-set(grp))
    sleep(10/runs)
    sys('cls') 
    for grp in grps.items():
        print(grp)