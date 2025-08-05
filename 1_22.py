# program for simple intrest and cumulative intrest.

p=float(input("Enter the principle : "))
t=float(input("Enter the time : "))
r=float(input("Enter the rate : "))
a=p*(1+r/100)**t

simple_intrest=(p*t*r)/100

cumulative_intrest=a-p

print(f"the simple intrest is {simple_intrest} and the cumulative intrest is {cumulative_intrest}")

