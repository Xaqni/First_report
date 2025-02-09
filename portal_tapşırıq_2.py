#________________________________________________ Tapırıq - 1

# Istifadeciden 2 reqem sorushsun, 3-cude operasiyani sorushsun eger `topla` dirsa toplasin, `cix` dirsa cixsin, 
# `bolme` dirsa bolsun, `vurma` bu isharedirse reqemleri bir birine vursun. neticeni sonda ekrana cap elesin.

# İstifadəçidən iki rəqəm daxil etməsini istəyirik

# ----------Həlli----------

# reqem1 = float(input("Birinci rəqəmi daxil edin: "))
# reqem2 = float(input("İkinci rəqəmi daxil edin: "))

# emeliyyat = input("Əməliyyatı seçin: ").strip().lower()

# if emeliyyat == "+":
#     netice = reqem1 + reqem2
# elif emeliyyat == "-":
#     netice = reqem1 - reqem2
# elif emeliyyat == "*":
#     netice = reqem1 * reqem2
# elif emeliyyat == "/":
#     if reqem2 != 0:
#         netice = reqem1 / reqem2
#     else:
#         netice = "Sıfıra bölmək olmur!"
# else:
#     netice = "Səhv əməliyyat seçimi!"

# print("Nəticə:", netice)


#________________________________________________ Tapırıq - 2.1

# Şərtlər (if-elif-else) Tapşırığı
# 1 xal
# Tapşırıq:
# İstifadəçidən yaşını daxil etməsini istəyin və aşağıdakı qaydalara əsasən ona mesaj verin:

# ----------Həlli----------

# 0-12 yaş: "Uşaqsan"
# 13-19 yaş: "Gəncsən"
# 20-64 yaş: "Böyüksən"
# 65 və yuxarı: "Yaşlısan"

# yas = int(input("Yaşınızı daxil edin: "))

# if 0 <= yas <= 12:
#     cavab = "Uşaqsan"
# elif 13 <= yas <= 19:
#     cavab = "Gəncsən"
# elif 20 <= yas <= 64:
#     cavab = "Böyüksən"
# elif yas >= 65:
#     cavab = "Yaşlısan"
# else:
#     cavab = "Düzgün yaş daxil edin!"

# print(cavab)


#________________________________________________ Tapırıq - 2.2

# Döngülər (For Loop) Tapşırığı
# 1 xal
# Tapşırıq:
# 1-dən 10-a qədər olan cüt ədədləri çap edən bir döngü yazın.

# ----------Həlli----------

# for eded in range(2, 11, 2):
#     print(eded)

#________________________________________________ Tapırıq - 2.3

# Dictionary Tapşırığı
# 1 xal
# Tapşırıq:
# Bir tələbənin imtahan nəticələri verilmişdir. Aşağıdakı dictionary-də fənlər və onların qiymətləri saxlanılır.

# Tələbənin orta qiymətini hesablayın və nəticəni çap edin.

# Riyaziyyat  85, Fizika 78, Kimya 90, İngilis dili  88, Tarix 76

# ----------Həlli----------

qiymetler = {
    "Riyaziyyat": 85,
    "Fizika": 78,
    "Kimya": 90,
    "İngilis dili": 88,
    "Tarix": 76
}

cem = sum(qiymetler.values())

fen_sayi = len(qiymetler)

orta_qiymet = cem / fen_sayi

print(f"Tələbənin orta qiyməti: {orta_qiymet:}")