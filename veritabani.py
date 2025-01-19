import sqlite3

# Veritabanı bağlantısı oluşturma
def baglanti_olustur():
    return sqlite3.connect('anket_sistemi.db')

# Gerekli tabloları oluşturma
def tablolar_olustur():
    conn = baglanti_olustur()
    cursor = conn.cursor()

    # Kullanıcılar tablosu
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS kullanicilar (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        kullanici_adi TEXT UNIQUE NOT NULL,
        sifre TEXT NOT NULL,
        rol TEXT NOT NULL
    )
    ''')

    # Anketler tablosu
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS anketler (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        baslik TEXT NOT NULL,
        aciklama TEXT
    )
    ''')

    # Sorular tablosu
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS sorular (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        anket_id INTEGER,
        soru_metni TEXT NOT NULL,
        FOREIGN KEY (anket_id) REFERENCES anketler(id)
    )
    ''')

    # Yanıtlar tablosu
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS yanitlar (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        soru_id INTEGER,
        kullanici_id INTEGER,
        yanit_metni TEXT NOT NULL,
        FOREIGN KEY (soru_id) REFERENCES sorular(id),
        FOREIGN KEY (kullanici_id) REFERENCES kullanicilar(id)
    )
    ''')

    conn.commit()
    conn.close()

tablolar_olustur()
