from veritabani import baglanti_olustur
from loglama import log_yaz

# Yeni anket oluşturma
def anket_ekle(baslik, aciklama, kullanici_adi):
    conn = baglanti_olustur()
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
        INSERT INTO anketler (baslik, aciklama)
        VALUES (?, ?)
        ''', (baslik, aciklama))
        
        conn.commit()
        log_yaz(f"Yeni anket oluşturuldu: {baslik}", kullanici_adi)
    except Exception as e:
        log_yaz(f"Anket oluşturma hatası: {str(e)}", kullanici_adi)
    finally:
        conn.close()

# Anketlere soru ekleme
def soru_ekle(anket_id, soru_metni, kullanici_adi):
    conn = baglanti_olustur()
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
        INSERT INTO sorular (anket_id, soru_metni)
        VALUES (?, ?)
        ''', (anket_id, soru_metni))
        
        conn.commit()
        log_yaz(f"Yeni soru eklendi (Anket ID: {anket_id}): {soru_metni}", kullanici_adi)
    except Exception as e:
        log_yaz(f"Soru ekleme hatası: {str(e)}", kullanici_adi)
    finally:
        conn.close()

# Tüm anketleri listeleme
def anketleri_goruntule():
    conn = baglanti_olustur()
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
        SELECT * FROM anketler
        ''')
        
        anketler = cursor.fetchall()
        return anketler
    except Exception as e:
        log_yaz(f"Anketleri görüntüleme hatası: {str(e)}", "Sistem")
        return []
    finally:
        conn.close()

# Belirli bir ankete ait tüm soruları listeleme
def sorulari_goruntule(anket_id):
    conn = baglanti_olustur()
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
        SELECT * FROM sorular
        WHERE anket_id = ?
        ''', (anket_id,))
        
        sorular = cursor.fetchall()
        return sorular
    except Exception as e:
        log_yaz(f"Soruları görüntüleme hatası (Anket ID: {anket_id}): {str(e)}", "Sistem")
        return []
    finally:
        conn.close()

# Yanıt ekleme
def yanit_ekle(soru_id, kullanici_id, yanit_metni, kullanici_adi):
    conn = baglanti_olustur()
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
        INSERT INTO yanitlar (soru_id, kullanici_id, yanit_metni)
        VALUES (?, ?, ?)
        ''', (soru_id, kullanici_id, yanit_metni))
        
        conn.commit()
        log_yaz(f"Yeni yanıt eklendi (Soru ID: {soru_id}): {yanit_metni}", kullanici_adi)
    except Exception as e:
        log_yaz(f"Yanıt ekleme hatası: {str(e)}", kullanici_adi)
    finally:
        conn.close()


# Tüm yanıtları listeleme
def yanitlari_goruntule():
    conn = baglanti_olustur()
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
        SELECT * FROM yanitlar
        ''')
        
        yanitlar = cursor.fetchall()
        return yanitlar
    except Exception as e:
        log_yaz(f"Yanıtları görüntüleme hatası: {str(e)}", "Sistem")
        return []
    finally:
        conn.close()
