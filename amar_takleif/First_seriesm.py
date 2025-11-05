#soheil nouri
#inja esmam ro  comment neweshtam shayad jelu tar ham comment benevisam ai nist khodam am U+1F383


import random

a = int(input("enter n :"))
count_A=0 #1
count_B=0 #2
count_C=0 #3
#inja tedad partab dace ha ro wared mikonim
for i in range (a):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)

    if dice1+dice2==5:
        count_A+=1
        

    if dice1==dice2:
        count_B+=1
    
    if dice1>dice2:
        count_C+=1

print(f" N={a}\n prob_A = {count_A/a}\n prob_B = {count_B/a}\n prob_C = {count_C/a}")