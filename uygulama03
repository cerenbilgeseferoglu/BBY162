print("Adam asmaca oyununa hoşgeldiniz !!!!!\nipucu:Bulacağınız kelime bir meyve ismidir ve toplamda 5 deneme hakkınız bulunmaktadır...")
kelimeler = ["kayısı", "şeftali", "ananas", "portakal", "karpuz", "çilek"]
for kelime in kelimeler:
    hak = 5
    bulunan = ""
    while True:
        for i in kelime:
            if i not in bulunan:
                print("-", end = " ")
            else:
                print(i, end =" ")
        print("\n{} deneme hakkınız kaldı".format(hak))
        x = input("Lütfen bir harf girin: ")
        if (x in kelime) & (x not in bulunan):
            if x not in bulunan:
                bulunan = bulunan + x
        else:
            hak -= 1
        finished = True
        for i in kelime:
            if i not in bulunan:
                finished = False
        if finished:
            print("\nTebrikler Bildiniz :)")
            tekrar = input("\nTekrar oynamak ister misiniz ? (evet / hayır): ")
            if tekrar == "evet":
                break
            else:
                exit()
        if hak == 0:
            print("\nAdam asıldı.. Kaybettiniz :(")
            tekrar = input("\nTekrar oynamak ister misiniz ? (evet / hayır): ")
            if tekrar == "evet":
                break
            else:
                exit()
