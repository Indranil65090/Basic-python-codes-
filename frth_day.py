a=int(input("Enter a number:"))
temp=a
r=0
while temp>0:
    d=temp%10
    r=(r*10)+d
    temp=temp//10
if(a==r):
    print("It's a Pallindrome Number")
else:
    print("Not it's not a Pallindrome number")        