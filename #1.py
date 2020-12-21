#1
teks = input("Silahkan masukkan kata yang anda ingin rubah : ")
a = input("Huruf apa saja yang anda inginkan untuk diubah ? ")
b = input("Ubah {0} menjadi : ".format(a))

def ubahHurufReplace(teks, a, b) :

    teksReplaced = teks.replace(a, b)
    return teksReplaced

def ubahHurufManual(teks, a, b) :

    listTeks = list(teks)
    for i in range(len(listTeks)) :
        
        if(listTeks[i] == a) :
            listTeks[i] = b
            
    teksReplaced = ''.join(listTeks)
    return teksReplaced

result = ubahHurufReplace(teks, a, b)
print(result)

hasil = ubahHurufManual(teks, a, b)
print(hasil)
