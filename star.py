from os import system
pause = lambda:system("pause")

n=int(input("enter number:"))
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()
pause()
