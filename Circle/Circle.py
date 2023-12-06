from math import*

from random import*

# # #10 Exercice

# #1
# t = 0
# for x in range(1,16):
#     A = float(input("Input number: "))
#     if A % 1 == 0:
#         t += 1

# print(t)

# # 2
# summa=0
# A=int(input("Input A: "))
# for x in range(1,A+1,1):
#     summa+=x
#     print("Summa: {0}".format(summa))


# 3
p=1
Lause=""
for x in range(8):
    A=float(input("{0}. samm\nInput A: ".format(x+1)))
    if A>0:
        p=A
        Lause = Lause + str(p) + "*"
print(Lause[:-1],"=",p,end="")


# #12
# n = randint(2,10)
# m = randint(1,10)
# summa = 0
# print("Chislo kosilok: ", n)
# print("Chislo kosilok: ", m)
# for t in range(n - 1):
#     m = (m/6) * 7
#     summa += m
#     print(m)
# print("Kokku misinad tootasid", summa, "tn")








# #15
# for y in range(10):
#     for x in range(10):
#         print(x,end="")
#     print()
    

# #29
# for i in range(9):
#     for x in range(9):
#         if x==0 or i==x:
#             print("x",end="")
#         else:
#             print("0",end="")
#     print() 








# for x in range(10):
#     R=float(input("{0} R: ").format(x+1))
#     if R>0:
#         S=pi*R**2
#     else:
#         S="R peab> kui 0 olema"
#     print("S={0}".format(S))
    

# x=0

# while True:
#     x+=1
#     R=float(input("{0} R: ").format(x+1))
#     if R>0:
#         S=pi*R**2
#     else:
#         S="R peab> kui 0 olema"
#     print("S={0}".format(S))
#     if x==10:
#         break
    

# #10 R
# x=0
# while x<10:
#     x+=1
#     R=float(input("{0} R: ").format(x+1))
#     if R>0:
#         S=pi*R**2
#     else:
#         S="R peab> kui 0 olema"
#     print("S={0}".format(S))
    

# #10 
# x=0
# while x<10:
#     R=float(input("{0} R: ").format(x+1))
#     if R>0:
#         S=pi*R**2
#         x+=1
#     else:
#         S="R peab> kui 0 olema"
#     print("S={0}".format(S))


