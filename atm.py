#!/usr/bin/python
from random import randint

# mutable vs immutable

# 200TL, 100TL, 50TL, 20TL
# banknot_miktarlari = [10, 5, 8, 50]
banknot_miktarlari = {"20" : 700, "50" : 500, "100" : 350, "200" : 190}

def print_sozluk(sozluk):
    for key in sozluk.keys():
        print(key, " => ", sozluk[key])

def randomize(sozluk):
    for key in sozluk.keys():
        sozluk[key] = randint(0,201)
        


"""
banknot miktarlarini ve cekilmek istenen para miktarini alan
sonrasinda o para miktarini nasil verilecegine karar veren bir fonksiyon/algoritma
"""

def give_money(money, banknot_miktarlari):
    print("calculating for....", money)
    verilecek_banknot_miktarlari = {"20" : 0, "50" : 0, "100" : 0, "200" : 0}
    while money >= 20:
        if money >= 200:
            money = money - 200
            banknot_miktarlari["200"] = banknot_miktarlari["200"] - 1
            verilecek_banknot_miktarlari["200"] += 1
            
        elif money >= 100:
            money = money - 100
            banknot_miktarlari["100"] = banknot_miktarlari["100"] - 1
            verilecek_banknot_miktarlari["100"] += 1
            
        elif money >= 50:
            money = money - 50
            banknot_miktarlari["50"] = banknot_miktarlari["50"] - 1
            verilecek_banknot_miktarlari["50"] += 1
            
        elif money >= 20:
            money = money - 20
            banknot_miktarlari["20"] = banknot_miktarlari["20"] - 1
            verilecek_banknot_miktarlari["20"] += 1
            
    if money < 20 and money > 0:
        print("ERROR 401")
        
    elif money == 0:
        print("Thank you for choosing us!")
    
    return verilecek_banknot_miktarlari
    
    
def moneyamountmaker():
    x = randint(400, 1000)
    x = x - (x % 10)
    return x
    
    
randomize(banknot_miktarlari)
print_sozluk(banknot_miktarlari)
print(give_money(moneyamountmaker(), banknot_miktarlari))