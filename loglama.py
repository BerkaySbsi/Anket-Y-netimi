import pandas as pd
from datetime import datetime

# Log dosyasına yazma işlevi
def log_yaz(olay, kullanici_adi):
    veri = {
        'Tarih': [datetime.now().strftime('%Y-%m-%d %H:%M:%S')],
        'Kullanici': [kullanici_adi],
        'Olay': [olay]
    }
     # Veriyi DataFrame'e çevir
    df = pd.DataFrame(veri)
    try:
         # Var olan log dosyasını oku
        mevcut_df = pd.read_excel('loglar.xlsx')      
        # Yeni veriyle birleştir     
        yeni_df = pd.concat([mevcut_df, df], ignore_index=True)
    except FileNotFoundError:
        yeni_df = df

      # Veriyi Excel dosyasına yaz
    yeni_df.to_excel('loglar.xlsx', index=False)
