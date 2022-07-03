from os import system as sys
from time import sleep
import random

start = int(input("Enter Starting Roll No.: "))
stop = int(input("Enter Ending Roll No.: "))
no_grp = int(input("Enter Number of Groups: "))
section = input("Enter Section (A or B): ")         # 'A' or 'B'  Group Names will be like A1, A2, ... or B1, B2, ...
runs = int(input("Enter Number of Iterations: "))   # Number of iterations tells how many times will the code run

for r in range(runs):
    std_lst = list(range(start,stop+1))
    no_per_grp = int(len(std_lst)/no_grp)
    random.shuffle(std_lst)
    grps = {}
    i=1 
    while len(std_lst):
        try: 
            grp = random.sample(std_lst,no_per_grp)
            grps[section+str(i)] = grp
            i = i+1
            std_lst = list(set(std_lst)-set(grp))
        except ValueError:
            rem = len(std_lst)
            grp_sample = random.sample(list(grps.keys()),rem)
            for k in range(rem):
                grps[grp_sample[k]].append(std_lst[k])
            std_lst.clear()
    sleep(10/runs)
    sys('cls') 
    for grp in grps.items():
        print(grp)