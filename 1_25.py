a=int(input("Enter a : "))
b=int(input("Enter b : "))

#swaping without thired variable.

a,b=b,a

print(f"a:{a} b:{b}")

#swaping with thired variable.

a,b=b,a

temp=b
b=a
a=temp

print(f"a:{a} b:{b}")