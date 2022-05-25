from __future__ import division

def int_div(a,b):
    print(a // b)
    
def div(a,b):
    print(a / b)

if __name__ == '__main__':
    a = int(input("a: "))
    b = int(input("b: "))
    int_div(a,b)
    div(a,b)