kenar1 = int(input("1. Kenarı Girin: "))
kenar2 = int(input("2. Kenarı Girin: "))
kenar3 = int(input("3. Kenarı Girin: "))

if kenar1==kenar2==kenar3 :
    print("EŞKENAR ÜÇGEN")
elif kenar1 == kenar2 or kenar1 == kenar3 or kenar2 == kenar3 :
    print("İKİZKENAR ÜÇGEN")
else:
    print("ÇEŞİTKENAR ÜÇGEN")



