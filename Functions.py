from turtle import *
def greeting(name):
    print('Hello' ,name)
    
n = input('Enter your name: ')
greeting(n)
greeting('Dave')

def price(flavour):
    if flavour == 'chocolate':
        cost = 1.99
    else:
        cost = 2.49
    return cost

print(price('banana'))
print(price('chocolate'))
print(price('vanilla'))


def draw_triangle(size):
    for n in range(3):
        forward(size)
        right(120)
 

draw_triangle(50)