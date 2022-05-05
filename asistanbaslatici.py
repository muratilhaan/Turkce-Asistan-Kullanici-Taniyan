import calendar
import os
import datetime
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import webbrowser
#import time
import sqlite3
import winshell




bag=sqlite3.connect("C:/Users/steam/PycharmProjects/opencvmurat/asistangelistirme/asistan.db")
cursor=bag.cursor()

dbisim=cursor.execute("Select İsim,Hakkında From KULLANICI")
kullanicilar = cursor.fetchall()


temel={"nasılsın":"çok iyiyim",
       "naber":"çok teşekkürler senden naber",
       "merhaba":"merhaba",
       "napıyosun":"senden bir komut bekliyorum",
       "kimsin":"ben Murat İlhan tarafından üretilen bir Asistanın ilk sürümüyüm.İsmim asistan",
       "özellik":"senin için youtube,google,gibi platformlarda istediğini sunabilirim.instagram,twitch,facebook gibi platformları açmak istediğinde bana sadece açmamı söylemen yeterli.Gün içerisinde hava durumu güncel saat ve aradığın konumu senin için bulabilirim.",
       "özelliklerin":"senin için youtube,google,gibi platformlarda istediğini sunabilirim.instagram,twitch,facebook gibi platformları açmak istediğinde bana sadece açmamı söylemen yeterli.Gün içerisinde hava durumu güncel saat ve aradığın konumu senin için bulabilirim."}


listedb=""
for i in kullanicilar:
    x=list(i)
    print(str(x))
    for isimler in i:
        listedb=listedb+" "+isimler
        print(listedb)




def tablo():
    cursor.execute("CREATE TABLE IF NOT EXISTS KULLANICI(İsim TEXT,Soyisim TEXT,Yas INT,Hakkında TEXT)")
    bag.commit()
def ekle(ad,soyad,yas,hakkinda):
    cursor.execute(f"Insert into KULLANICI Values('{ad}','{soyad}',{yas},'{hakkinda}')")
    bag.commit()



tablo()



yenihitap=""
a=0
sorgu = ""
print("Asistan v1 Açılıyor....")


def dinleme():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("dinleniyor...")
        r.pause_threshold = 1
        ses = r.listen(source)
    try:
        sorgu = r.recognize_google(ses, language="tr-TR").lower()
        sorgu.lower()
        print(sorgu)

    except Exception as e:
        print("Dediğin şeyi tam olarak algılayamadım lütfen tekrar söyle.")
        return "None"
    return sorgu


def konusma(metin):
    tts = gTTS(text=metin, slow=False, lang="tr")
    kayit = "C://Users//steam//PycharmProjects//opencvmurat//asistangelistirme//kayit.mp3"
    tts.save(kayit)
    playsound(kayit)
    os.remove(kayit)


def saatzaman():
    saat = datetime.datetime.now().hour
    if saat <= 12 and saat >= 6:
        konusma("Merhaba,Günaydın")
        print("Merhaba,Günaydın")
    elif saat >= 12 and saat <= 18:
        konusma("Merhaba,İyi günler")
        print("Merhaba,iyi günler")
    else:
        konusma("Merhaba,İyi geceler")
        print("Merhaba iyi geceler")


saatzaman()

class tarih():
    # -------------GÜN---------------#
    day = datetime.datetime.now().day
    # ------------AYLAR--------------#
    ay = datetime.datetime.now().month
    if ay == 1:
        ay = "Ocak"
    elif ay == 2:
        ay = "Şubat"
    elif ay == 3:
        ay = "Mart"
    elif ay == 4:
        ay = "Nisan"
    elif ay == 5:
        ay = "Mayıs"
    elif ay == 6:
        ay = "Haziran"
    elif ay == 7:
        ay = "Temmuz"
    elif ay == 8:
        ay = "Ağustos"
    elif ay == 9:
        ay = "Eylül"
    elif ay == 10:
        ay = "Ekim"
    elif ay == 11:
        ay = "Kasım"
    elif ay == 12:
        ay = "Aralık"
    # ---------SAAT-----------#
    saat = datetime.datetime.now().hour
    dakika = datetime.datetime.now().minute
    toplam = (str(saat) + " " + str(dakika))
    # --------Hangi GÜN-------#
    day2 = datetime.datetime.today()
    hafta = calendar.day_name[day2.weekday()]
    if hafta == "Monday":
        hafta = "pazartesi"
    elif hafta == "Tuesday":
        hafta = "salı"
    elif hafta == "Wednesday":
        hafta = "çarşamba"
    elif hafta == "Thursday":
        hafta = "perşembe"
    elif hafta == "Friday":
        hafta = "cuma"
    elif hafta == "Saturday":
        hafta = "cumartesi"
    elif hafta == "Sunday":
        hafta = "pazar"

def beyin():
    global yenihitap
    #import pandas as pd
    beyinwhile=True
    while beyinwhile:
        konusma('adın nedir ')
        id_value =dinleme()
        yenihitap = id_value
        konusma("soyadın ne ")
        qty_value = dinleme()
        konusma("kaç yaşındasın")
        moa_value = dinleme()
        konusma("kimsin")
        tax_value = dinleme()
        ekle(id_value,qty_value,moa_value,tax_value)
        bag.close()

        beyinwhile=False




class ozellikler():
    # -----------------------SİTELER----------------------#
    def youtube(self,istek):
        konusma("Youtube'da aramak istediğin şey nedir?")
        istek=dinleme()
        konusma("Senin için açıyorum")
        self.youtube = webbrowser.open("https://www.youtube.com/results?search_query="+"".join(str(istek)))

    def facebook(self):
        self.facebook = webbrowser.open("https://www.facebook.com/")

    def google(self,istek):
        konusma("google'da ne aramak istersin")
        istek=dinleme()
        konusma("yönlendiriyorum.")
        self.google=webbrowser.open("https://www.google.com/search?q=" + "".join(str(istek)))

    def twitch(self):
        self.twitch = webbrowser.open("https://www.twitch.tv/")

    def instagram(self):
        self.instagram=webbrowser.open("https://www.instagram.com/")

    def discord(self):
        self.discord=webbrowser.open("https://discord.com/")

    def temizle(self):
        konusma(f"{isimalgi}sana bir uyarı gönderdim ve çöp kutusunu temizlemek isteyip istemediğini sordum")
        self.temizleme=winshell.recycle_bin().empty(confirm=True,show_progress=False,sound=True)
        konusma("Çöpler siliniyor")

    def navigasyon(self,konum):
        konusma(f"{isimalgi}.aramak istediğin konumu kısaca söyleyebilir misin?")
        konum=dinleme()
        konusma("seni yönlendiriyorum")
        self.navigasyon=webbrowser.open("https://www.google.com/maps/place/"+"".join(str(konum)))



    # -------------GENEL BİLGİ----------------------#
    def saat(self):
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        konusma(f"saat şuanda {strTime}")

    def aygun(self):
        self.aygun = konusma(f"bugün {tarih.day},{tarih.ay}")

    def haftagun(self):
        self.hangigun = konusma(f"bugün{tarih.hafta}")



b=True
while b:
    isimalgi=""
    konusma("Beni tanıyorsan ismimi söyleyip kendini tanıtabilirsin.mesela ben murat.gibi")
    tanima=dinleme()
    try:
        isimalgi=tanima.split('ben')
        isimalgi=str(isimalgi[1].replace('\n',''))
    except:
        pass


    if "asistan" in tanima and isimalgi in listedb:
        konusma(f"Hoşgeldin {isimalgi},seni tekrardan görmek çok güzel")
        a=1
    if "asistan" in tanima and isimalgi not in listedb:
        konusma("ismimi biliyorsun daha önce tanışmışmıydık?")
        eh=dinleme()
        if "evet" in eh:
            konusma("bana ismini söyler misin")
            yisim=dinleme()
            konusma(f"hatırlamak için hafızamı kontrol ediyorum .")
            if yisim in listedb:
                konusma(f"evet senin hakkında birşeyler hatırladım.")
                a=1
        if "hayır" in eh:
            konusma("demek tanışmadık seni hatırlamam için birkaç soru sormam gerekiyor")
    if isimalgi in listedb and "asistan" not in tanima:
        konusma(f"Hoşgeldin {isimalgi},seni hatırlar gibiyim.")
        a=1
    if "asistan" not in tanima and isimalgi not in listedb:
        konusma("Merhaba Adımı bilmediğine göre daha önce tanışmadık sana yardımcı olabilmem için tanımam gerekiyor.")
        beyin()
        konusma(f"Seninle tanışmak güzeldi{yenihitap}.bir daha geldiğinde bana asistan diyerek seslenebilirsin.")
        isimalgi=yenihitap
        a=1

    while a==1:
        try:
            konusma("Seni dinliyorum?")
            istek = dinleme()
            if "youtube" in istek:
                ozellikler.youtube(istek,istek)
            elif istek in temel:
                konusma(temel[istek])
            elif "facebook" in istek:
                konusma("seni facebook için yönlendiriyorum.")
                ozellikler.facebook(istek)
            elif "twitch" in istek:
                konusma("seni twitch için yönlendiriyorum.")
                ozellikler.twitch(istek)
            elif "google" in istek:
                ozellikler.google(istek,istek)

            elif "çöp" in istek:
                ozellikler.temizle(istek)
                konusma("işlem istediğin şekilde yapılıyor")

            elif "harita" in istek or "navigasyon" in istek:
                ozellikler.navigasyon(istek,istek)


            elif "saat" in istek:
                ozellikler.saat(istek)
            elif "gün" in istek:
                ozellikler.haftagun(istek)
            elif "tarih" in istek :
                ozellikler.aygun(istek)

            elif "güle güle"in istek or "bay" in istek or "görüşürüz" in istek or "çıkış"in istek or "uyu"in istek or "kapat" in istek:
                konusma("Asistan kapatılıyor...")
                print("Asistan kapatılıyor...")
                b=False
                a=0
                exit()

        except:
            pass
    else:
        continue
