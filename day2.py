
# Cut ededler
# n = int(input("ededlerin sayini verin: "))

# for i in range(n):
#     eded = int(input("ededi daxil edin: "))
#     if eded % 2 == 0:
#         print("Eded cutdur")
#     else:
#         print("Eded tekdir")

# factorial
# n = int(input("Ededi daxil edin: "))
# factorial = 1
# for i in range(1, n+1):
#     factorial *= i
# print(factorial)

# Fibonacci
# birinci = 1
# ikinci = 1
# n = int(input("Ededi daxil edin: "))

# for i in range(3, n + 1):
#     elave_stekan = ikinci
#     ikinci = birinci + ikinci
#     birinci = elave_stekan

# print(ikinci)

# 1: Balans necedir?
# 2: Pul medaxil et: mebleg
# 3: Pul cixart: mebleg
# 4: Emeliyyati bitir

# ATM
# balance = 100

# while True:
#     n = int(input("Operator nomresini daxil edin 1,2 ve ya 3:"))
#     if n == 1:
#         print(balance)
#     if n == 2:
#         mebleg = int(input("Meblegi daxil edin: "))
#         balance += mebleg
#     if n == 3:
#         mebleg = int(input("Meblegi daxil edin: "))
#         if mebleg > balance:
#             print("Emeliyyati etmek mumkun deyil")
#         else:
#             balance -= mebleg
#     if n == 4:
#         break

# 3 ededin maximumu
# a = int(input("ededi daxil edin: "))
# b = int(input("ededi daxil edin: "))
# c = int(input("ededi daxil edin: "))

# if a >= b and a >= c:
#     print(a)
# elif b >= c:
#     print(b)
# else:
#     print(c)


# maximum
# from math import inf as musbet_sonsuzluq

# n = int(input("ededlerin sayini daxil edin: "))
# maximum = -musbet_sonsuzluq

# for i in range(n):
#     eded = int(input("ededi daxil edin: "))
#     if eded > maximum:
#         maximum = eded

# print(maximum)

# Prime numbers
# import math
# eded = int(input("ededi daxil edin: "))

# is_prime = True

# for i in range(2, math.sqrt(eded)+1):
#     if eded % i == 0:
#         is_prime = False
#         break

# if is_prime:
#     print("eded sadedir")
# else:
#     print("eded sade deyil")

# Sum of digits

eded = int(input())
reqemleri_cemi = 0

while eded > 0:
    reqemleri_cemi += eded % 10
    eded //= 10

print(reqemleri_cemi)
