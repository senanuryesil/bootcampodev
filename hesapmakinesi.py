sayi1 = int(input("1. sayıyı giriniz:")) 
sayi2 = int(input("2. sayıyı giriniz:")) 
islem = input("Toplama için (+), Çıkarma için (-), Çarpma için(*), Bölme için (/) giriniz")
if islem == "+":
    sonuc = sayi1 + sayi2 
    print("Toplamı:" ,sonuc)
elif islem == "-":
    sonuc = sayi1 - sayi2
    print("Farkı:" ,sonuc)
elif islem == "*":
    sonuc = sayi1 * sayi2
    print("Çarpımı:" ,sonuc)
elif islem == "/" :
    sonuc = sayi1 / sayi2
    print("Bölümü:" ,sonuc)
else:
    print("HATALI İŞLEM")
