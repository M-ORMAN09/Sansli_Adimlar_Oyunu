import time
import random

kullanici1_konum = 0
kullanici2_konum = 0

print("""\033[033m
***************************************      
           ŞANSLI ADIMLAR 
***************************************          
""")

while(True):
    kullanici1 = input("\033[034m1. KULLANICI KOD ADI..? : \033[0m").strip().upper()
    if (kullanici1.isalpha() == True):
        if(len(kullanici1) >= 3):
            print("\033[032m1.KULLANICI KAYDEDİLDİ.")
            break
        else:
            print("\033[031mKOD AD EN AZ 3 HARFTEN OLUŞMALI..!")
    else:
        print("\033[031mKOD AD SADECE HARFLERDEN OLUŞMALI..!")
        
while(True):      
    kullanici2 = input("\033[034m2. KULLANICI KOD ADI..? : \033[0m").strip().upper()
    if (kullanici2.isalpha() == True):
        if(len(kullanici2) < 3):
            print("\033[031mKOD AD EN AZ 3 HARFTEN OLUŞMALI..!")
        elif(kullanici1 == kullanici2):
            print("\033[031mKOD ADLAR FARKLI OLMALI..!")
        else:
            print("\033[032m2.KULLANICI KAYDEDİLDİ.")
            break
    else:
        print("\033[031mKOD AD SADECE HARFLERDEN OLUŞMALI..!")
        
bir = [ "       * * * * * * *",
        "       *     •     *",
        "       *  •  •     *",
        "       *     •     *",
        "       *     •     *",
        "       *  • • • •  *",       
        "       * * * * * * *"]

iki = [ "       * * * * * * *",
        "       *  • • • •  *",
        "       *        •  *",
        "       *  • • • •  *",
        "       *  •        *",
        "       *  • • • •  *",       
        "       * * * * * * *"]

uc =  [ "       * * * * * * *",
        "       *  • • • •  *",
        "       *        •  *",
        "       *    • • •  *",
        "       *        •  *",
        "       *  • • • •  *",       
        "       * * * * * * *"]

dort = ["       * * * * * * *",
        "       *  •     •  *",
        "       *  •     •  *",
        "       *  • • • •  *",
        "       *        •  *",
        "       *        •  *",       
        "       * * * * * * *"]

bes = [ "       * * * * * * *",
        "       *  • • • •  *",
        "       *  •        *",
        "       *  • • • •  *",
        "       *        •  *",
        "       *  • • • •  *",       
        "       * * * * * * *"]

alti = ["       * * * * * * *",
        "       *  • • • •  *",
        "       *  •        *",
        "       *  • • • •  *",
        "       *  •     •  *",
        "       *  • • • •  *",       
        "       * * * * * * *"]

zar1 = [bir, iki, uc, dort, bes, alti]

topla =["       * * * * * * *",
        "       *     •     *",
        "       *     •     *",
        "       * • • • • • *",
        "       *     •     *",
        "       *     •     *",       
        "       * * * * * * *"]

cikar =["       * * * * * * *",
        "       *           *",
        "       *           *",
        "       * • • • • • *",
        "       *           *",
        "       *           *",       
        "       * * * * * * *"]

zar2 = [topla, cikar]

while(True):
    mesafe = int(input("\033[034mYARIŞ PİSTİNİN UZUNLUĞU..? : \033[0m"))
    if (mesafe < 10):
        print("\033[031mPİST UZUNLUĞU 10' DEN BÜYÜK OLMALI..!")
    elif(mesafe > 50):
        print("\033[031mPİST UZUNLUĞU 50' DEN KÜÇÜK OLMALI..!")
    else:
        print("\033[032mPİST UZUNLUĞU KAYDEDİLDİ.")
        break
        
print("\033[030m\t\n   OYUN BAŞLIYOR\033[0m",end='')

for i in range(3):
    print(".",end='',flush=True)
    time.sleep(1)
    
print("""\n\033[033m
******************************************************************
  MEVCUT KONUMLAR:  [{} : {}] , [{} : {}] 
******************************************************************     
""".format(kullanici1,kullanici1_konum,kullanici2,kullanici2_konum))
      
while(kullanici1_konum < mesafe and kullanici2_konum < mesafe and kullanici1_konum > -mesafe and kullanici2_konum > -mesafe):
    
    while(kullanici1_konum < mesafe):
        tikla1 = input("\033[035m{} ZARLARI ATMAK İÇİN, BİR DEFA 'ENTER' TUŞUNA BAS..".format(kullanici1))
        secim_zar1 = random.choice(zar1)
        secim_zar2 = random.choice(zar2)
        for i in secim_zar1:
            print(i)
        for j in secim_zar2:
            print(j)
        if (secim_zar1 == bir):
            if (secim_zar2 == topla):
                kullanici1_konum += 1
                break
            else:
                kullanici1_konum -= 1
                break
            
        elif (secim_zar1 == iki):
            if (secim_zar2 == topla):
                kullanici1_konum += 2
                break
            else:
                kullanici1_konum -= 2
                break
        elif (secim_zar1 == uc):
            if (secim_zar2 == topla):
                kullanici1_konum += 3
                break
            else:
                kullanici1_konum -= 3
                break
            
        elif (secim_zar1 == dort):
            if (secim_zar2 == topla):
                kullanici1_konum += 4
                break
            else:
                kullanici1_konum -= 4
                break
        elif (secim_zar1 == bes):
            if (secim_zar2 == topla):
                kullanici1_konum += 5
                break
            else:
                kullanici1_konum -= 5
                break
            
        else:
            if (secim_zar2 == topla):
                kullanici1_konum += 6
                break
            else:
                kullanici1_konum -= 6
                break
    print("""\n\033[036m
******************************************************************
 {} YENİ KONUMUN : {},  SIRA SENDE : {}   
******************************************************************        
""".format(kullanici1,kullanici1_konum,kullanici2))   
            
    while(kullanici2_konum < mesafe):
        tikla1 = input("\033[035m{} ZARLARI ATMAK İÇİN, BİR DEFA 'ENTER' TUŞUNA BAS..".format(kullanici2))
        secim_zar1 = random.choice(zar1)
        secim_zar2 = random.choice(zar2)
        
        for i in secim_zar1:
            print(i)
        for j in secim_zar2:
            print(j)
            
        if (secim_zar1 == bir):
            if (secim_zar2 == topla):
                kullanici2_konum += 1
                break
            else:
                kullanici2_konum -= 1
                break 
        elif (secim_zar1 == iki):
            if (secim_zar2 == topla):
                kullanici2_konum += 2
                break
            else:
                kullanici2_konum -= 2
                break
        elif (secim_zar1 == uc):
            if (secim_zar2 == topla):
                kullanici2_konum += 3
                break
            else:
                kullanici2_konum -= 3
                break  
        elif (secim_zar1 == dort):
            if (secim_zar2 == topla):
                kullanici2_konum += 4
                break
            else:
                kullanici2_konum -= 4
                break
        elif (secim_zar1 == bes):
            if (secim_zar2 == topla):
                kullanici2_konum += 5
                break
            else:
                kullanici2_konum -= 5
                break 
        else:
            if (secim_zar2 == topla):
                kullanici2_konum += 6
                break
            else:
                kullanici2_konum -= 6
                break
            
    print("""\n\033[036m
******************************************************************
 {} YENİ KONUMUN : {},  SIRA SENDE : {}   
******************************************************************        
""".format(kullanici2,kullanici2_konum,kullanici1))
    
if(kullanici1_konum > kullanici2_konum):
    print(f"\n\033[033mKAZANAN {kullanici1}, TEBRİKLER!\n\033[0m")
else:
    print(f"\n\033[033mKAZANAN {kullanici2}, TEBRİKLER!\n\033[0m")