# 🧬 DNA Sekans Analiz ve Kalite Kontrol Aracı

Ham DNA dizilerini analiz eden, mRNA dizisine dönüştüren, PCR optimizasyonu için GC oranını hesaplayan ve başlangıç kodonunu (`AUG`) tespit eden Python tabanlı bir biyoinformatik aracıdır.

## 🚀 Özellikler

* **Büyük/Küçük Harf Duyarsız Giriş:** Kullanıcı tarafından girilen DNA dizilerini `.upper()` metodu ile otomatik olarak standart hale getirir.
* **DNA'dan mRNA'ya Transkripsiyon:** Timin (`T`) bazlarını Urasil (`U`) bazlarına dönüştürür.
* **Baz Kompozisyonu ve Uzunluk Analizi:** Dizinin toplam uzunluğunu (`bp`) ve her bir nükleotidin (`A`, `T`, `G`, `C`) sayısını hesaplar.
* **GC Oranı ve PCR Protokol Önerisi:** GC yüzdesini hesaplar ve %60 eşik değerine göre standart veya yüksek bağlanma sıcaklığı (annealing) gerektiren PCR protokolünü önerir.
* **Başlangıç Kodonu Tespiti:** Oluşturulan mRNA dizisini tarayarak protein kodlama potansiyelini gösteren `AUG` başlangıç kodonunu tespit eder.

## 🛠️ Kullanılan Teknolojiler

* **Python 3** (Yerleşik fonksiyonlar ve string manipülasyon metotları)

## 💻 Kurulum ve Kullanım

1. Projeyi bilgisayarınıza indirin veya klonlayın:
   ```bash
   git clone [https://github.com/aydin008/dna-analizi-mini-biyoinformatik-projesi.git](https://github.com/aydin008/dna-analizi-mini-biyoinformatik-projesi.git)
