#soru 1
metin = "Açık bilim, araştırma çıktılarına ve süreçlerine herkesin serbestçe erişmesini, bunların ortak kullanımını, dağıtımını ve üretimini kolaylaştıran bilim uygulamasıdır."
print(metin[:20])

#soru2
liste = ["Açık Bilim", "Açık Erişim", "Açık Lisans", "Açık Eğitim", "Açık Veri", "Açık Kültür"]
for i in liste:
    print(i)
#soru3
sozluk = {"Elma" : "Ağaçta yetişen bir tür meyve" , "Salatalık" : "Fidan üzerinde büyüyen bir tür sebze"}
while True:
  print("Lütfen kelimenin baş harfini büyük yazınız!!!")
  girilen = input("Aradığınız kelimeyi giriniz:")
if girilen in sozluk:
  print("Ağaçta Yetişen Bir Tür Meyve")
else:
  print("Başka bir kelime giriniz")
