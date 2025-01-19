# Çevrimiçi Anket Yönetim Sistemi

Bu proje, bir çevrimiçi anket yönetim sistemi oluşturmayı amaçlamaktadır. Bu sistem, kullanıcıların anket oluşturmasını, anketlere katılmasını ve anket sonuçlarını görüntülemesini sağlar. Python ve SQLite kullanılarak geliştirilmiştir.

## Gereksinimler

- Python 3.x
- SQLite3
- pandas

## Kullanım

1. Proje klasöründe bir sanal ortam oluşturun (isteğe bağlı):

    ```bash
    python3 -m venv venv
    ```

2. Sanal ortamı etkinleştirin:

    - Windows:

    ```bash
    venv\Scripts\activate
    ```

    - Unix veya MacOS:

    ```bash
    source venv/bin/activate
    ```

3. Gerekli bağımlılıkları yükleyin:

    ```bash
    pip install -r requirements.txt
    ```

4. Ana programı başlatın:

    ```bash
    python ana_program.py
    ```

## Dosya Yapısı

- `ana_program.py`: Programın ana işlevselliğini içeren Python dosyası.
- `veritabani.py`: SQLite veritabanı işlemlerini gerçekleştiren Python dosyası.
- `kullanici_yonetimi.py`: Kullanıcı yönetimi işlemlerini gerçekleştiren Python dosyası.
- `anket_yonetimi.py`: Anket yönetimi işlemlerini gerçekleştiren Python dosyası.
- `loglama.py`: Loglama işlemlerini gerçekleştiren Python dosyası.
- `README.md`: Bu dosya; proje hakkında bilgi içerir.
- `requirements.txt`: Projede kullanılan bağımlılıkları içeren dosya.

## Katkılar

Bu proje hala geliştirme aşamasındadır. Herhangi bir katkıda bulunmak isterseniz, lütfen bir çekme isteği gönderin veya bir sorun açın. 

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için LICENSE dosyasını inceleyebilirsiniz.
