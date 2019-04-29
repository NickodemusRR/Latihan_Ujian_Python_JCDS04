import requests

#API Powered by NewsAPI.org
API_KEY = '1acdc8bbd29b45b184cc5347af79dee9'

# membuat dictionary pilihan kategori
category = {
    '1':'technology',
    '2':'business',
    '3':'sport',
    '4':'health',
    '5':'science',
}

# membuat dictionary kategori dalam bahasa Indonesia
category_ind = {
    'technology':'teknologi',
    'business':'bisnis',
    'sport':'olahraga',
    'health':'kesehatan',
    'science':'sains',
}

# Fungsi untuk memilih kategori berita
def pilih_berita():
    pilihan = input('Selamat datang, mau tahu berita apa hari ini?\n[1] Berita seputar teknologi\n[2] Berita seputar bisnis\n[3] Berita seputar olahraga\n[4] Berita seputar kesehatan\n[5] Berita seputar sains\nKetik pilihan Anda [1/2/3/4/5] : ') 
    if category.get(pilihan) == None:
        print('Maaf input yang Anda masukkan tidak valid.\n')
        pilih_berita()
    else:
        top_news(pilihan)

# Fungsi untuk menampilkan 5 berita teratas
def top_news(pilihan):
    pilihan = pilihan
    url = 'https://newsapi.org/v2/top-headlines?country=id&category='+category[pilihan]+'&apiKey='+API_KEY
    berita = requests.get(url)
    print('\nBerikut adalah top 5 berita Indonesia bidang {}:'.format(category_ind[category[pilihan]]))
    i = 0
    while i <= 4:
        print('{} - {}'.format(i+1, berita.json()['articles'][i]['title']))
        i += 1

# Menjalankan fungsi pilih_berita()
pilih_berita()