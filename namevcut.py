import requests

for i in range(1000):
    url = 'https://thispersondoesnotexist.com/'
    response = requests.get(url)

    if response.status_code == 200:
        with open(f'fotolar/foto{i}.jpg', 'wb') as file:
            file.write(response.content)
        print('Dosya başarıyla indirildi ve kaydedildi.')
    else:
        print('Dosya indirilemedi. HTTP Durum Kodu:', response.status_code)
