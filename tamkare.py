s1 = int(input("1. Sayıyı Girin: "))
s2 = int(input("2. Sayıyı Girin: "))
tamkareler = []
for sayi in range(s1, s2 + 1):
    if (sayi ** 0.5) % 1 == 0:
        tamkareler.append(sayi)
print(f"{s1} ile {s2} arasındaki tamkare sayılar: {tamkareler}")