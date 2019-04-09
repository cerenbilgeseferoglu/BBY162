_author_ = "cerenbilgeseferoglu"
print("Aşağıdaki soruları cevaplayınız\nNOT:Her soru 20 puandır\n********************************")
sorular = ['Cumhuriyet ilan edildiğinde Atatürk kaç yaşındaydı?',
           'Atatürk\'ün Samsun\'a çıktığı tarih aşağıdakilerden hangisidir?',
           'Atatürk\'ün Gazi ünvanını aldığı savaş aşağıdakilerden hangisidir?',
           'Atatürk aşağıdaki okulların hangisinde öğrenim görmemiştir?',
           'Aşağıdakilerden hangisi Atatürk ilkelerinden biri değildir?']

cevaplar = ['A','D','C','B','D']
cevapA = ['42','1912','I.Kosova','Şemsi Efendi İlkokulu','Milliyetçilik']
cevapB = ['41','1921','Trablusgarp Savaşı','Millet Mektebi','Devletçilik']
cevapC = ['43','1922','Sakarya Meydan Savaşı','Kara Harp Okulu','Halkçılık']
cevapD = ['52','1919','Kurtuluş Savaşı','Manastır Askeri İdadisi','Devrimcilik']

sonuc = 0
for i in range(len(sorular)):
    print("Soru " + str(i+1)+":"+sorular[i])
    print("A) " + cevapA[i])
    print("B) " + cevapB[i])
    print("C) " + cevapC[i])
    print("D) " + cevapD[i])
    cevap = input("Cevabınızı Giriniz: ")
    if cevaplar[i] == cevap.upper():
        print("Sonuç Doğru")
        sonuc += 20
print("Tebrikler,test sona erdi!")
print("Aldığınız not: " +str(int((sonuc/len(sorular))*5)))
input()

