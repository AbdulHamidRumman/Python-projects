import itertools
import random

lst1 = ["18-19"]
sec = ["Section A"]
ques = ["1","2","3","4"]
ls = [lst1,sec,ques]

out = list(itertools.product(*ls))
random.shuffle(out)
print(out)