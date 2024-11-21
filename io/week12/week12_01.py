# for i in range(5,0,-1):
#     for j in range(5-i):
#         print(" ",end="")
#     for j in range(2*i-1):
#         print("*",end="")
#     print()

num = abs(int(input("Enter a number: ")))
for i in range(5,0,-1):
    print(" "*(5-i),end="")
    print("*"*(2*i-1), end="")
    print()