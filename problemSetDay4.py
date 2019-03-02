# file name: problemSetDay4.py
mysterynumber=10
guess=int(input("guess my number!?"))
while(guess != mysterynumber):
    guess=int(input("try again!!"))
if guess== mysterynumber:
    print("you got it!")
print("i will say how strong you are")
stregnth=5
while stregnth<10:
    stregnth+=1
    print(stregnth)
    print("now you are THAT strong^^")
if stregnth==10:
    print("you are too strong for me")
    print("i bow to you. you have LEVELED UP")
n=int
m=int
print(n**m)
