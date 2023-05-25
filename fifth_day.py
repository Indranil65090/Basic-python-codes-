# n=int(input("Enter the number of rows:"))
# for i in range(0,n):
#     for j in range(0,i+1):
#         print("* ",end="")
#     print("\r")

# n=int(input("Enter the number of rows:"))
# for i in range(n+1):
#     for j in range(i):
#         print(i,end=" ")
#     print("\n")   

rows = 5
num = rows
# reverse for loop
for i in range(rows, 0, -1):
    for j in range(0, i):
        print(num, end=' ')
    print("\r") 

