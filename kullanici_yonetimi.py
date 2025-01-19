from veritabani import baglanti_olustur
from loglama import log_yaz
import sqlite3

# Yeni kullanıcı kaydı oluşturma
def kullanici_ekle(kullanici_adi, sifre, rol):
    conn = baglanti_olustur()
    cursor = conn.cursor()
    try:
        cursor.execute('''
        INSERT INTO kullanicilar (kullanici_adi, sifre, rol)
        VALUES (?, ?, ?)
        ''', (kullanici_adi, sifre, rol))
        conn.commit()
        log_yaz(f"Yeni kullanıcı oluşturuldu: {kullanici_adi}, Rol: {rol}", kullanici_adi)
    except sqlite3.IntegrityError:
        print("Bu kullanıcı adı zaten mevcut.")
    finally:
        conn.close()

# Kullanıcı girişini kontrol etme
def kullanici_girisi(kullanici_adi, sifre):
    conn = baglanti_olustur()
    cursor = conn.cursor()
    cursor.execute('''
    SELECT * FROM kullanicilar
    WHERE kullanici_adi = ? AND sifre = ?
    ''', (kullanici_adi, sifre))
    kullanici = cursor.fetchone()
    conn.close()
    return kullanici

# Kullanıcı rolünü kontrol etme
def kullanici_rolu(kullanici_adi):
    conn = baglanti_olustur()
    cursor = conn.cursor()
    cursor.execute('''
    SELECT rol FROM kullanicilar
    WHERE kullanici_adi = ?
    ''', (kullanici_adi,))
    rol = cursor.fetchone()
    conn.close()
    return rol[0] if rol else None
