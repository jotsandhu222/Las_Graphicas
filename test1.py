import time
def area():
    x = input(" c for circle, r for rectangle ")
    
    if x == "c":
        r = int(input(" radius: "))
        answer = 3.14 * r * r
        print(answer)
    
    if x == "r":
        l = int(input("l "))
        b = int(input("b "))
        answer = l * b
        print(answer)
    
    else:
        print("not valid entry")
    return answer
count = 7

for i in range(count):
    print("hello")



