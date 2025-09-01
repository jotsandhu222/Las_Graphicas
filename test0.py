import time

def calculate_area():
    print("hello")
    time.sleep(5)
    print("world")
    som = int(input("enter the radius: "))
    if som < 5:
        question = som * 10
        
    if som > 5:
        question = som * 100
        
    else:
        question = som * 100000
    #circle_area = 2 * 3.14 * r * r
    #rectangle_area = l * b
    return question

count = 0
while True:
    print(count)
    count += 1
    time.sleep(5)

    
