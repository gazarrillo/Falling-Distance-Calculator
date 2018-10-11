#Intro
print('This program tells you how far an object will fall in a number of seconds.')
#Input
time = int(input('Enter the falling time in seconds: '))
#Defining Function
def fallingDistance(time):
    gravity = 9.8
    distance = 1 / 2 * gravity * time**2
    return round(distance, 1)
#Loop
while time > 0:
    print('The distance the object will fall in', time, 'seconds is:', fallingDistance(time), '\n')
    time = int(input('Enter the falling time in seconds: '))
