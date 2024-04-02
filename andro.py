print("## prorgram python menghitung luas segtiga")
print("==========================================")
print ()

def hitungluassegtiga(a,t):
    return round(0,5 *a *t,2)

alas = float(input("input alas segitiga"))
tinggi = float(input("input tinggi segitiga"))

print("luas segitiga = ",hitungluassegtiga(alas,tinggi))
