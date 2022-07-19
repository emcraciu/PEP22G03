
prime = 97
base = 7
local1 = 64
local2 = 37

x = pow(base, local1) % prime

print(x)

y = pow(base, local2) % prime

print(y)

print(pow(y, local1) % prime)
print(pow(x, local2) % prime)