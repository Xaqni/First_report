# Task 2. İstifadəçidən aylıq gəlirini və xərclərini (məsələn, kirayə, ərzaq və nəqliyyat) soruşun. Xərclərdən sonra qalan qalıqlarını hesablayın və göstərin. məsələn
# # Input: gelir = 5000, kiraye = 1500, magaza = 1000, ictimai_neqiliyyat = 500
# # Output: qaliq = 2000
 
# gelir=int(input("ayliq gelirinizi daxil edin: "))
# kiraye=int(input("ayliq kirayenizi daxil edin: "))
# erzag=int(input("ayliq erzagizi daxil edin: "))
# yanacaq=int(input("ayliq yanacaginizi daxil edin: "))

# xecler=kiraye+erzag+yanacaq
# qaliq=gelir-xecler
# print(f"qaliq mebleg: {qaliq}")


# Task 3. İstifadəçidən yaşını və növbəti doğum gününə neçə ay qaldığını soruşun. 
# Onların ad gününə qalan günlərin sayını hesablayın və göstərin (sadəlik üçün ayı 30 gün qəbul edin).
# Input: yas = 25, nece_ay_qalib = 5
# # Output: Ad gunune 150 gun qaldi

# yas=int(input("yasi daxil et: "))
# ay=int(input("ayi daxi et: "))
# qalan_gun=ay*30
# print(f"sizin novbeti dogum gununuze {qalan_gun} gwn qalib")


# Task 5. İstifadəçinin 1-dən 10-a qədər gizli nömrəni təxmin etməyə çalışdığı proqram yaradın.
# Hər təxmindən sonra onların çox yüksək, çox aşağı və ya düzgün olduğunu bildirin. İstifadəçi düzgün təxmin etdikdə oyun bitməlidir.
# # Secret number: 7
# # Input: 4, 9, 7
# # Output: "Çox aşağı", "Çox yüksək", "Təbriklər qazandınız düzdü"

# secret_nuber=7
# while True:
#     istifadeci=int(input("1-den 10 qeder reqem texmin edin: "))
#     if istifadeci > secret_nuber:
#         print("verdiyiniz reqem ywksekdir: ")
#     elif istifadeci < secret_nuber:
#         print("verdiyiniz reqem kicikdir: ")
#     else:
#         print("tebrikler duz tapdiz: ")
#         break

# dogum_ili=int(input("Doguldugunilini daxil et: "))
# cari_il=2025
# indiki_yas=cari_il-dogum_ili
# if indiki_yas >= 18:
#     print("siz yetgivsiz")
# else:
#     print("siz hele usaqsiz")

# while True:
#     try:
#         il=int(input("doğulduğun ili daxil edin-"))
#     except ValueError:
#         print("reqem daxil edin ")
#         break

#     yas= abs(il-2025)

#     if yas > 18:
#         print("yetiskinsen halaldi")
#     else:
#         print("maladoysan ")

from datetime import datetime
birthday = input("Doguldugunuz tarixi (il-ay-gun) formasinda daxil edin: ")
birthday_h = datetime.strptime(birthday, "%Y-%m-%d")
now = datetime.now()
ferq = now - birthday_h
il = ferq.days // 365
ay = (ferq.days % 365) // 30
gun = (ferq.days % 365) % 30

print(f"Doguldugunuzdan bu gune {il} il, {ay} ay, {gun} gun yasamisiz")

