#PROGRAM MENGHITUNG TOTAL TAGIHAN LISTRIK

def format_indonesia(nilai):
    str_nilai = str(nilai)
    separate_decimal = str_nilai.split(".")
    after_decimal = separate_decimal[0]
    before_decimal = separate_decimal[1]

    reverse = after_decimal[::-1]
    temp_reverse_value = ""

    for index, val in enumerate(reverse):
        if (index + 1) % 3 == 0 and index + 1 != len(reverse):
            temp_reverse_value = temp_reverse_value + val + "."
        else:
            temp_reverse_value = temp_reverse_value + val

    temp_result = temp_reverse_value[::-1]

    return temp_result + "," + before_decimal


golongan=(input("Golongan = "))
daya=float(input("daya = "))
Pemakaian=float(input("Pemakaian = "))

if(golongan=='R1' and daya== 900):
    tarif=1352
elif(golongan=='R1' and daya== 1300):
    tarif=1444.70
elif(golongan=='R1' and daya== 2200):
    tarif=1444.70
elif(golongan=='R2' and daya >=3500 and daya <= 5500 ):
    tarif=1699.53
elif(golongan=='R3' and daya ==6600 ):
    tarif=1699.53
elif(golongan=='B2' and daya >=6600 and daya <=200000):
    tarif=1444.70
elif(golongan=='B3' and daya ==200000):
    tarif=1114.74
elif(golongan=='I3' and daya ==200000):
    tarif=1314.12
elif(golongan=='P1' and daya >=6600 and daya <=200000):
    tarif=1523.28
else:
    tarif=0
if (tarif==0):
    print("data tidak valid")
else:
    tagihan=tarif*Pemakaian
    print("jumlah tagihan anda :",format_indonesia(tagihan))
