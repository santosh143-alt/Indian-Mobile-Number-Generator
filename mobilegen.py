from random import *
def phonenum():
    num=str(randint(6,9))
    for i in range(9):
        x=str(randint(0,9))
        num=num+x
    print('+91'+num)
phonenum()