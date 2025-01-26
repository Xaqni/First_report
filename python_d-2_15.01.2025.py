
# number = 3
# amount = 3.99

# print(number+5)
# print(type(number))
# print(dir(amount))
# print(dir(number))
 

# number1=10
# number2=5

# toplama = number1 + number2
# vurma =  number1 * number2
# cixma = number1 - number2
# bolme = number1 / number2

# print(type(toplama), toplama)
# print(type(vurma), vurma)
# print(type(cixma), cixma)
# print(type(bolme),bolme)


# stringler

# name = "Hello"
# name2 = 'Test'
# name3 = """
# This is also string

# test 1234
# """

# print(name)
# print(name2)
# print(name3)

 
# Formatting

# name_4 = "Hello {1}, {0}" .format("Word", "test")
# # name_5 = "Hello {name}, {surname}" .format(name_5 = "Word", name_5 = "test")
# name_5 = "Hello {name}, {surname}".format(name = "Word", surname = "test")

# example = {"name": "test"}
# name_6 = f"format {example} 5"


# # print(name_4)
# # print(name_5)
# print(name_6)


# String methods

# value = "example string"

# for method in dir(value):
#     # if not "__" in method:

#         print(method)

# value = "the quick fox test fox test foxe"

# # print(value.replace("t", "$"))
# result =""
# count = 0
# for index, caracter in enumerate(value):
#     if caracter =="t":
#         count +=1
#         if count ==2:
#             result += "$"
#         else:
#             result == caracter
#     else:
#         result += caracter

# print("Netice: ", result)



#     if index == 14:
#         result += "$"
#     else:
#         result +=caracter
# print("Netice: ", result)

# index =value.index("t", 14)
# print(index)

# number = 0 
# for caracter in value:
#     print(caracter, number)
#     # number = number +1
#     number +=1
   
# find_index_test = value.find("test")
# print(find_index_test)

# ikinci_index_test = value.find("test", find_index_test+1)
# print(ikinci_index_test)

# print("Birinci hisse: ", value[:ikinci_index_test])
# # print("Ikinci hisse: ", value[ikinci_index_test :])



# # number = 0 
# # for caracter in value:
# #     if caracter =="t":
# #         print(caracter, number)
# #     number +=1
   
# # for index, caracter in enumerate(value):
# #     if caracter == "t":
# #         print(index, caracter)

# # index =value.index("t", 1)
# # print(index)


# # Task 3.
# # Siyahinin içərisindən axtarış edən funksiya yaradın. 
# # 2 arqumenti olsun. array, word. Əgər verilmiş söz siyahıda varsa o zaman Boolean True qaytarsın yoxdursa onda False.

# # Input:
# # find_in_list([5, 6, 7, 2, 4], 2) # True
# # find_in_list([5, 6, 7, 2, 4], 9) # False
# # find_in_list(['alma', 'armud'], 'armud') # True
# # find_in_list(['alma', 'armud'], 'nar') # False


# def find_in_list(array, word):
    
#     return word in array
# print(find_in_list([5, 6, 7, 2, 4], 2)) # True
# find_in_list([5, 6, 7, 2, 4], 2) # True

# print(find_in_list([5, 6, 7, 2, 4], 9)) # False 
# find_in_list([5, 6, 7, 2, 4], 9) # False

# print(find_in_list(['alma', 'armud'], 'armud')) # True  
# find_in_list(['alma', 'armud'], 'armud') # True

# print(find_in_list(['alma', 'armud'], 'nar')) # False
# find_in_list(['alma', 'armud'], 'nar') # False

# print(find_in_list(["gilas", "ciyelek"], "qarpiz")) # False


# Task 4. 
# Funksiya siyahının içərisindəki hər bir ədədləri qüvvətə yüksəltsin və sonda alınan nəticəni toplasın. bir arqumenti olacaq. məsələn
# Input:
# pow_the_list_and_find_maximum([1,2,9,4,5,6]) # 163
# pow_the_list_and_find_maximum([6,23,235,74,36,14]) # 62758
# pow_the_list_and_find_maximum([5,26,223,76,634]) # 458162

# İzahı: [1,2,9,4,5,6] hər bir elementi qüvvətə yüksəldən zaman sondaki nəticə belə olacaq [1, 4, 81, 16, 25, 36] və toplayan zaman 1 + 4 + 81 + 16 + 25 + 36 = 163

def pow_the_list_and_find_maximum(numbers):
    kvadrat =[x**2 for x in numbers]
    return sum(kvadrat)
try:
    n=int(input("Enter the number: "))
    numers=[]
    for i in range(n):
        element = int(input(f"Siyahinin {i+1} -ci elementini daxil edin: "))
        numers.append(element)
    result = pow_the_list_and_find_maximum(numers)
    print(result)
except ValueError:
    print("Duzgun eded daxil edirn")