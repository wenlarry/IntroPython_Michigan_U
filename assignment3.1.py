hrs = input ("Enter Hours:")
h = float(hrs)
rate = input("Enter the pay rate:")
r = float(rate)
if h>40:
    cost = ((h-40)*r*1.50) + (40*r)
else:
    cost = (h*r)
print (cost)
