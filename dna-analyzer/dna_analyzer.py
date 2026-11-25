dna = input("Bir DNA dizisi giriniz: ")
dna = dna.upper()

def rna_donustur(dna):
    dna.replace("T","U")
    return dna.replace("T","U")
print("mRNA karşılığı: " , rna_donustur(dna))

def gc_orani(dna):
    dna.count("G")
    dna.count("C")
    toplam = dna.count("G") + dna.count("C")
    yuzde = toplam/len(dna) * 100
    return yuzde
print("Hesaplanan yüzde: " , gc_orani(dna))
gc_orani = float(input("Hesaplanan yüzdeyi giriniz: "))

def pcr_durumu(yuzde):
    if yuzde > 60:
        return "Yüksek GC (Yüksek sıcaklık gerekir.)"
    else:
        return "Normal GC (Standart protokol uygulanabilir.)"
print("PCR durumu: " , pcr_durumu(gc_orani))

print("Dizinin toplam uzunluğu: " , len(dna))
print("A bazı sayısı: " , dna.count("A"))
print("T bazı sayısı: " , dna.count("T"))
print("G bazı sayısı: " , dna.count("G"))
print("C bazı sayısı: " , dna.count("C"))

uretilen_rna = rna_donustur(dna)

def kodon_bul(uretilen_rna):
    if "AUG" in uretilen_rna:
        return "Başlangıç kodonu (AUG) bulundu!!!"
    else: 
        return "Başlangıç kodonu (AUG) bulunamadı."

print("Başlangıç kodonu bulunma durumu: " , kodon_bul(uretilen_rna))