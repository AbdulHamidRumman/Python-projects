from os import system as sys
from time import sleep
import random

runs = 30   # Number of iterations tells how many times will the code run

for r in range(runs):
    start = 31
    stop = 60
    no_grp = 6
    section = 'B' # 'A' or 'B'  Group Names will be like A1, A2, ... or B1, B2, ...

    std_lst = list(range(start,stop+1))
    no_per_grp = int(len(std_lst)/no_grp)
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