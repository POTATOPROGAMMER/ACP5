base = int(input("enter the base : "))
exp = int(input("enter the exponent : "))
res = 1
for i in range(exp):
    res=res*base
print(f"{base}^{exp}={res}")