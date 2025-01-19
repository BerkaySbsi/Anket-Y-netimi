
from kullanici_yonetimi import kullanici_ekle, kullanici_girisi, kullanici_rolu
from anket_yonetimi import anket_ekle, soru_ekle, anketleri_goruntule, sorulari_goruntule, yanit_ekle, yanitlari_goruntule
from veritabani import tablolar_olustur
from loglama import log_yaz
from admin import kullanicilari_goruntule, kullanici_sil, anket_sil, admin_ekle, soru_sil

# Ana program başlangıcı
def main():
    # Veritabanı tablolarını oluştur
    tablolar_olustur()
    
    # Admin kullanıcısını ekle
    admin_ekle()
    
    print("Çevrimiçi Anket Yönetim Sistemine Hoş Geldiniz!")
    
    while True: #menü döngüsü oluşturur
        print("\n1. Giriş Yap")
        print("2. Kayıt Ol")
        print("3. Çıkış")
        secim = input("Seçiminizi yapın: ")
        
        if secim == '1':
            # Kullanıcı girişi işlemi
            kullanici_adi = input("Kullanıcı Adı: ")
            sifre = input("Şifre: ")
            kullanici = kullanici_girisi(kullanici_adi, sifre)
            
            if kullanici:
                # Giriş başarılıysa, kullanıcı rolüne göre menüye yönlendir
                print(f"Hoş geldiniz, {kullanici_adi}!")
                rol = kullanici_rolu(kullanici_adi)
                
                if rol == 'admin':
                    admin_menusu(kullanici_adi)
                elif rol == 'anket_olusturucu':
                    anket_olusturucu_menusu(kullanici_adi)
                elif rol == 'katilimci':
                    katilimci_menusu(kullanici_adi, kullanici[0])
            else:
                print("Geçersiz kullanıcı adı veya şifre.")
        
        elif secim == '2':
            # Yeni kullanıcı kaydı işlemi
            kullanici_adi = input("Kullanıcı Adı: ")
            sifre = input("Şifre: ")
            rol = input("Rol (anket_olusturucu/katilimci): ")
            kullanici_ekle(kullanici_adi, sifre, rol)
        
        elif secim == '3':
            # Sistemden çıkış
            print("Çıkış yapılıyor...")
            log_yaz("Sistemden çıkış yapıldı", "Sistem")
            break
        
        else:
            print("Geçersiz seçim, tekrar deneyin.")

# Admin menüsü
def admin_menusu(kullanici_adi):
    while True:
        print("\n1. Anket Oluştur")
        print("2. Anketlere Soru Ekle")
        print("3. Soruları Görüntüle")
        print("4. Anketleri Görüntüle")
        print("5. Anket Sil")
        print("6. Kullanıcıları Görüntüle")
        print("7. Kullanıcı Sil")
        print("8. Soru Sil")
        print("9. Yanıtları Görüntüle")
        print("10. Yanıt Ekle")
        print("11. Çıkış")
        secim = input("Seçiminizi yapın: ")
        
        if secim == '1':
            baslik = input("Anket Başlığı: ")
            aciklama = input("Anket Açıklaması: ")
            anket_ekle(baslik, aciklama, kullanici_adi)
        
        elif secim == '2':
            anket_id = input("Anket ID: ")
            soru_metni = input("Soru Metni: ")
            soru_ekle(anket_id, soru_metni, kullanici_adi)

        elif secim == '3':
            anket_id = input("Anket ID: ")
            sorular = sorulari_goruntule(anket_id)
            for soru in sorular:
                print(f"ID: {soru[0]}, Anket ID: {soru[1]}, Soru Metni: {soru[2]}")
        
        elif secim == '4':
            anketler = anketleri_goruntule()
            for anket in anketler:
                print(f"ID: {anket[0]}, Başlık: {anket[1]}, Açıklama: {anket[2]}")
        
        elif secim == '5':
            anket_id = input("Silinecek Anket ID: ")
            anket_sil(anket_id)
        
        elif secim == '6':
            kullanicilari_goruntule()
        
        elif secim == '7':
            kullanici_id = input("Silinecek Kullanıcı ID: ")
            kullanici_sil(kullanici_id)
        
        elif secim == '8':
            soru_id = input("Silinecek Soru ID: ")
            soru_sil(soru_id)
        
        elif secim == '9':
            yanitlar = yanitlari_goruntule()
            for yanit in yanitlar:
                print(f"ID: {yanit[0]}, Soru ID: {yanit[1]}, Kullanıcı ID: {yanit[2]}, Yanıt Metni: {yanit[3]}")
        
        elif secim == '10':
            anket_id = input("Anket ID: ")
            sorular = sorulari_goruntule(anket_id)
            for soru in sorular:
                print(f"ID: {soru[0]}, Soru Metni: {soru[2]}")
            soru_id = input("Soru ID: ")
            yanit_metni = input("Yanıt Metni: ")
            yanit_ekle(soru_id, 1, yanit_metni, kullanici_adi)  # Admin ID'si 1 olarak varsayılıyor
        
        elif secim == '11':
            break
        
        else:
            print("Geçersiz seçim, tekrar deneyin.")

# Anket oluşturucu menüsü
def anket_olusturucu_menusu(kullanici_adi):
    while True:
        print("\n1. Anket Oluştur")
        print("2. Anketlere Soru Ekle")
        print("3. Soruları Görüntüle")
        print("4. Anketleri Görüntüle")
        print("5. Anketlere Yanıt Ekle")  # Yeni eklenen seçenek
        print("6. Çıkış")
        secim = input("Seçiminizi yapın: ")
        
        if secim == '1':
            # Yeni anket oluşturma
            baslik = input("Anket Başlığı: ")
            aciklama = input("Anket Açıklaması: ")
            anket_ekle(baslik, aciklama, kullanici_adi)
        
        elif secim == '2':
            # Anketlere soru ekleme
            anket_id = input("Anket ID: ")
            soru_metni = input("Soru Metni: ")
            soru_ekle(anket_id, soru_metni, kullanici_adi)

        elif secim == '3':
            # Anketin sorularını görüntüleme
            anket_id = input("Anket ID: ")
            sorular = sorulari_goruntule(anket_id)
            for soru in sorular:
                print(f"ID: {soru[0]}, Anket ID: {soru[1]}, Soru Metni: {soru[2]}")
        
        elif secim == '4':
            # Anketleri görüntüleme
            anketler = anketleri_goruntule()
            for anket in anketler:
                print(f"ID: {anket[0]}, Başlık: {anket[1]}, Açıklama: {anket[2]}")
        
        elif secim == '5':
            # Anketlere yanıt ekleme
            anket_id = input("Anket ID: ")
            sorular = sorulari_goruntule(anket_id)
            for soru in sorular:
                print(f"ID: {soru[0]}, Soru Metni: {soru[2]}")
            soru_id = input("Soru ID: ")
            yanit_metni = input("Yanıt Metni: ")
            yanit_ekle(soru_id, 1, yanit_metni, kullanici_adi)  # Kullanıcı ID'si 1 olarak varsayılıyor
        
        elif secim == '6':
            # Anket oluşturucu menüsünden çıkış
            break
        
        else:
            print("Geçersiz seçim, tekrar deneyin.")


# Katılımcı menüsü
def katilimci_menusu(kullanici_adi, kullanici_id):
    while True:
        print("\n1. Anketleri Görüntüle")
        print("2. Anketlere Yanıt Ekle")
        print("3. Yanıtları Görüntüle")
        print("4. Anketlere Soru Ekle")
        print("5. Soruları Görüntüle")
        print("6. Çıkış")
        secim = input("Seçiminizi yapın: ")
        
        if secim == '1':
            # Anketleri görüntüleme
            anketler = anketleri_goruntule()
            for anket in anketler:
                print(f"ID: {anket[0]}, Başlık: {anket[1]}, Açıklama: {anket[2]}")
        
        elif secim == '2':
            # Anketlere yanıt ekleme
            anket_id = input("Anket ID: ")
            sorular = sorulari_goruntule(anket_id)
            for soru in sorular:
                print(f"ID: {soru[0]}, Soru Metni: {soru[2]}")
            soru_id = input("Soru ID: ")
            yanit_metni = input("Yanıt Metni: ")
            yanit_ekle(soru_id, kullanici_id, yanit_metni, kullanici_adi)
        
        elif secim == '3':
            # Yanıtları görüntüleme
            yanitlar = yanitlari_goruntule()
            for yanit in yanitlar:
                print(f"ID: {yanit[0]}, Soru ID: {yanit[1]}, Kullanıcı ID: {yanit[2]}, Yanıt Metni: {yanit[3]}")
        
        elif secim == '4':
            # Anketlere soru ekleme
            anket_id = input("Anket ID: ")
            soru_metni = input("Soru Metni: ")
            soru_ekle(anket_id, soru_metni, kullanici_adi)

        elif secim == '5':
            # Soruları görüntüleme
            anket_id = input("Anket ID: ")
            sorular = sorulari_goruntule(anket_id)
            for soru in sorular:
                print(f"ID: {soru[0]}, Anket ID: {soru[1]}, Soru Metni: {soru[2]}")
        
        elif secim == '6':
            # Katılımcı menüsünden çıkış
            break
        
        else:
            print("Geçersiz seçim, tekrar deneyin.")
# program doğrudan çalıştırıldığında ana programın başlatılmasını sağlar.
if __name__ == "__main__":
    main()
