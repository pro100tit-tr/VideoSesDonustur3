<h1 align="center">Video Sesini Dönüştür</h1>
  <p align="center">
    Video Kodlayıcı Telegram Botu
    <br />
    <a href="https://telegram.dog/SesVideoBot"><strong>Örnek Bot »</strong></a>
    <br />
    <a href="https://github.com/Turkce-Botlar-Sohbet/VideoSesDonustur/issues">Hata Bildir</a>
    |
    <a href="https://github.com/Turkce-Botlar-Sohbet/VideoSesDonustur/issues">Özellik İste</a>
  </p>
</p>

<hr>

<h2 align="center">Bot Hakkında</h2>
<p align="center">
    <a href="https://github.com/Turkce-Botlar-Sohbet/VideoSesDonustur">
        <img src="https://www.flaticon.com/premium-icon/icons/svg/2626/2626281.svg" height="100" width="100" alt="Telegram Logo">
    </a>
</p>
<p align='center'>
    Telegram'ın ses formatına destek vermediği hiç sesi çıkmayan videoları FFmpeg aracılığıyla uygun formata kodlar ve bunu herhangi bir kalite kaybı olmadan yapar.
</p>

### Ortam Değişkenleri:
Ortam değişkenlerini ayarlayın ve bunları [config.env](./config.env) içine ekleyin.
- `API_ID` - [https://my.telegram.org](https://my.telegram.org)'da bir uygulama oluşturarak edinin.
- `API_HASH` - [https://my.telegram.org](https://my.telegram.org)'da bir uygulama oluşturarak edinin.
- `BOT_TOKEN` - [https://t.me/BotFather](https://t.me/BotFather) adresinden bir bot oluşturarak edinin.
- `SUDO_USERS` - Yetkili kullanıcının ID numarasını ekleyin. Birden fazla kullanıcı için ayırıcı olarak boşluk kullanın.
- `DOWNLOAD_DIR` - (İsteğe bağlı) İndirilen dosyaları saklamak için geçici indirme dizini. Varsayılan: "downloads/"

### Kodlama Biçimini Yapılandırma:
FFmpeg profilini değiştirmek isterseniz şuradan ayarlayın: [ffmpeg.py](/bot/helper/ffmpeg.py)

## Heroku ile Kolay Kurulum:
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Railway ile Kolay Kurulum:
[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https%3A%2F%2Fgithub.com%2FTurkce-Botlar-Sohbet%2FVideoSesDonustur&envs=API_ID%2CAPI_HASH%2CBOT_TOKEN%2CSUDO_USERS%2CDOWNLOAD_DIR&optionalEnvs=DOWNLOAD_DIR&API_IDDesc=https%3A%2F%2Fmy.telegram.org%27da+bir+uygulama+olu%C5%9Fturarak+edinin.&API_HASHDesc=https%3A%2F%2Fmy.telegram.org%27da+bir+uygulama+olu%C5%9Fturarak+edinin.&BOT_TOKENDesc=https%3A%2F%2Ft.me%2FBotFather+adresinden+bir+bot+olu%C5%9Fturarak+edinin.&SUDO_USERSDesc=Yetkili+kullan%C4%B1c%C4%B1n%C4%B1n+ID+numaras%C4%B1n%C4%B1+ekleyin.+Birden+fazla+kullan%C4%B1c%C4%B1+i%C3%A7in+ay%C4%B1r%C4%B1c%C4%B1+olarak+bo%C5%9Fluk+kullan%C4%B1n.&DOWNLOAD_DIRDesc=%28%C4%B0ste%C4%9Fe+ba%C4%9Fl%C4%B1%29+%C4%B0ndirilen+dosyalar%C4%B1+saklamak+i%C3%A7in+ge%C3%A7ici+indirme+dizini.+Varsay%C4%B1lan+-%3E+downloads%2F&referralCode=BOTSOHBET)

## Linux'ta Docker ile Kurulum:

- 1. Python ve Docker'ı kurun.
```
sudo snap install docker
sudo apt install python3
```
- 2. Repo'yu Klonlayın.
```
git clone https://github.com/Turkce-Botlar-Sohbet/VideoSesDonustur
cd VideoSesDonustur
```
- 3. Yapılandırma Dosyasını Ayarlayın.
```
nano config.env
```
- 4. Docker Görüntüsü Oluşturun.
```
sudo docker build . -t videosesdonustur
```
- 5. Botu Çalıştırın.
```
sudo docker run videosesdonustur
```

### Telif Hakkı ve Lisans
- Copyright &copy; 2021 &mdash; [Türkçe Botlar Sohbet](https://t.me/botsohbet)
- [MIT License](./LICENSE)

<a href="https://www.digitalocean.com/?refcode=8a7a2b148ace&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge"><img src="https://web-platforms.sfo2.digitaloceanspaces.com/WWW/Badge%203.svg" alt="DigitalOcean Referral Badge" /></a>
