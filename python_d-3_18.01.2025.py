# def tofiq(lst,n):
#     mylist=[]
    

#     for i in range (1 , n+1):
#         if i not in lst:
#             mylist.append(i)

#     return mylist
# emrah=[1,2,3,4,5,7,9]
# mirze=9 


# name = "Xaqani"
# print(name)

# def funksiya():
#     """
#     Bu strunk cap eden funksiyadir
#     """
#     # return "Hello word"
# name = "Hello world"
# print(name) 

# price_1 = 5
# price_2 = 10
# print(price_1 ,price_2)

# def process(numer):
# #     return None, numer
# #  # _, a =process(10)
# # _, result=process(10)

#    return numer, None 
# result,_=process(10)

# print(result)

# name =input("Adinizi daxil edin: ")  

# age = int(input("Yasinizi daxil edin: "))

# if age>=18:
#     print(name)
# else:
#     print("Icaze yoxdur")

# # print(name, age)

# from random import randint


# print(randint(1, 10))

import random
guess = random.randint(1,5)
chanse =5

while True:
    for i in range(1,chanse+1):        
        guess_number = int(input(f"{i}. Reqem daxil edin: ")) 

        if guess==guess_number:
            print("Tebrikler duz tapdiniz")
            break
        else:
            print("Bir daha yoxlayin")

    ask_user =input("Oyuna yeniden baslamaq isteyirsinizmi (hə/yox)? ")
    if ask_user == "hə":
        guess = random.randint(1, 5)
    else:
        game_cantinue = False
        print("bye")
        break
        





# while True:

























