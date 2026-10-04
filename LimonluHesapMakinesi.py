q = ["1","2","3","4","5","6","7","8","9","0","-","."]
w = ["+","-","*","**","/","//","%",".","x","×","÷",":","^"] #unuttuğum işlem varsda diye en başa koydum bunları
while True:
    while True:
        x = input("1. sayı? ")
        x = x.replace(",", ".")
        xn = 0
        xe = 0
        xs = True
        if x == "" or x == "." or x == "-":
            print("Hata. gerçek bir sayı giriniz.  Tekrar dene.\n")
            continue 
        if x.startswith("-."):
            xs = False
        for i, karakter in enumerate(x):
                if karakter in q:
                    if karakter == "-":
                         if i == 0:
                              xe = xe + 1
                              pass
                         else:
                              xe = xe + 1
                              xs = False
                    elif karakter == ".":
                         if i == 0 or i == len(x) - 1:
                              xs = False
                         else:
                              xn = xn + 1
                              pass
                else:
                    xs = False
        if xn <= 1 and xe <= 1 and xs == True:
            break
        else:
             print("Hata. gerçek bir sayı giriniz.  Tekrar dene.\n")
             continue
    while True:
        y = input("2. sayı? ")
        y = y.replace(",", ".")
        yn = 0
        ye = 0
        ys = True
        if y == "" or y == "." or y == "-":
            print("Hata. gerçek bir sayı giriniz.  Tekrar dene.\n")
            continue 
        if y.startswith("-."):
            ys = False
        for i, karakter in enumerate(y):
                if karakter in q:
                    if karakter == "-":
                         if i == 0:
                              ye = ye + 1
                              pass
                         else:
                              ye = ye + 1
                              ys = False
                    elif karakter == ".":
                         if i == 0 or i == len(y) - 1:
                              ys = False
                         else:
                              yn = yn + 1
                              pass
                else:
                    ys = False
        if yn <= 1 and ye <= 1 and ys == True:
            break
        else:
             print("Hata. gerçek bir sayı giriniz.  Tekrar dene.\n")
             continue
    while True:
        islem = input("işlem? ")
        if islem == "8828" and x == "8828" and y == "8828":
            sonuc = "EAL Easter Egg :D"
            break
        if islem in w:
            xx = float(x)
            yy = float(y)
            try:
                if islem == "+":
                    sonuc = xx + yy
                elif islem == "-":
                    sonuc = xx - yy
                elif islem in ["*", ".", "x", "×"]:
                    sonuc = xx * yy
                elif islem == ["**", "^", "..", "xx", "××"]:
                    sonuc = xx ** yy
                elif islem == ["/", ":", "÷"]:
                    sonuc = xx / yy
                elif islem == ["//", "::", "÷÷"]:
                    sonuc = xx // yy
                elif islem == "%":
                    sonuc = xx % yy
                break
            except ZeroDivisionError:
                print("\nHATA! Sıfıra bölemezsin!")
                sonuc = "HATA!"
                break
            except OverflowError:
                print("\nHATA! Sayı belleğe sığmayacak kadar büyük!")
                sonuc = "HATA!"
                break
        else:
            print("hatalı işlem tekrar dene.\n")
            continue
    print("\n****************************")
    print("--> SONUÇ:", sonuc)
    print("****************************\n")
