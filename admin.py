from veritabani import baglanti_olustur
from loglama import log_yaz

def admin_ekle():
    # Veritabanı bağlantısı oluştur
    conn = baglanti_olustur()
    cursor = conn.cursor()
    try:
        # 'admin' kullanıcı adını kontrol et
        cursor.execute("SELECT * FROM kullanicilar WHERE kullanici_adi = 'admin'")
        if not cursor.fetchone():
            # Eğer yoksa, admin kullanıcısını ekle
            cursor.execute("INSERT INTO kullanicilar (kullanici_adi, sifre, rol) VALUES (?, ?, ?)", ('admin', 'adminpassword', 'admin'))
            conn.commit()
            log_yaz("Admin kullanıcı oluşturuldu.", "Sistem")
    except Exception as e:
        # Hata durumunda log yaz
        log_yaz(f"Admin ekleme hatası: {str(e)}", "Sistem")
    finally:
        # Bağlantıyı kapat
        conn.close()

admin_ekle()

def kullanicilari_goruntule():
    # Veritabanı bağlantısı oluştur
    conn = baglanti_olustur()
    cursor = conn.cursor()
    try:
        # Tüm kullanıcıları seç
        cursor.execute("SELECT * FROM kullanicilar")
        kullanicilar = cursor.fetchall()
    except Exception as e:
        # Hata durumunda log yaz
        log_yaz(f"Kullanıcıları görüntüleme hatası: {str(e)}", "Sistem")
        kullanicilar = []
    finally:
        # Bağlantıyı kapat
        conn.close()

    # Kullanıcı bilgilerini yazdır
    for kullanici in kullanicilar:
        print(f"ID: {kullanici[0]}, Kullanıcı Adı: {kullanici[1]}, Rol: {kullanici[3]}")

def kullanici_sil(kullanici_id):
    # Veritabanı bağlantısı oluştur
    conn = baglanti_olustur()
    cursor = conn.cursor()
    try:
        # Belirtilen ID'ye sahip kullanıcıyı sil
        cursor.execute("DELETE FROM kullanicilar WHERE id = ?", (kullanici_id,))
        conn.commit()
        print("Kullanıcı silindi.")
    except Exception as e:
        # Hata durumunda log yaz
        log_yaz(f"Kullanıcı silme hatası: {str(e)}", "Sistem")
    finally:
        # Bağlantıyı kapat
        conn.close()

def anket_sil(anket_id):
    # Veritabanı bağlantısı oluştur
    conn = baglanti_olustur()
    cursor = conn.cursor()
    try:
        # Belirtilen ID'ye sahip anketi sil
        cursor.execute("DELETE FROM anketler WHERE id = ?", (anket_id,))
        conn.commit()
        print("Anket silindi.")
    except Exception as e:
        # Hata durumunda log yaz
        log_yaz(f"Anket silme hatası: {str(e)}", "Sistem")
    finally:
        # Bağlantıyı kapat
        conn.close()

def soru_sil(soru_id):
    # Veritabanı bağlantısı oluştur
    conn = baglanti_olustur()
    cursor = conn.cursor()
    try:
        # Belirtilen ID'ye sahip soruyu sil
        cursor.execute("DELETE FROM sorular WHERE id = ?", (soru_id,))
        conn.commit()
        print("Soru silindi.")
    except Exception as e:
        # Hata durumunda log yaz
        log_yaz(f"Soru silme hatası: {str(e)}", "Sistem")
    finally:
        # Bağlantıyı kapat
        conn.close()
