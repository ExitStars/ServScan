#-*-coding:utf-8-*-
# Modüller
from tkinter import *
from tkinter import messagebox
from time import sleep
from threading import Thread
from socket import socket
from requests import get
from re import findall

anapen = Tk()
anapen.title("ServScan.Alfa | Turkz / Ar-Ge Grup")
anapen.geometry("400x300")
anapen.resizable(False, False)

bloklist = []
serverlist = []

def temizle():
    durum["text"] = "Tarama Yok"
    durum["fg"] = "red"


def blokTarama():
    temizle()
    durum["text"] = "Tarama Var"
    durum["fg"] = "green"

    class scan(Thread):
       def run(self):
           try:
                target = GenerateIP()
                s=socket()
                s.connect((target, 80))
                bloklist.append(target)
                s.close()
           except:
               pass

    ip = ipiste.get()
    ayrilmisIP = ip.split(".")
    olusanIP = ayrilmisIP[0]+"."+ayrilmisIP[1]+"."+ayrilmisIP[2]+"."

    global blok

    def GenerateIP():
        global blok
        blok = blok+1
        return olusanIP+str(blok)
    blok = 0

    for i in range(1, 256):
       t = scan()
       t.start()

    for i in range(len(bloklist)):
        bulunanipler.insert(END, bloklist[i])

    temizle()

def blokCikti():
    dosya = open("bloktarama.txt", "w")
    for i in bloklist:
        dosya.write(i+"\n")
    dosya.close()
    messagebox.showinfo("Bilgilendirme" , "Dosya Bulundugunuz Dizine Kaydedildi")

def serverCikti():
    dosya = open("servertarama.txt", "w")
    for i in serverlist:
        dosya.write(i+"\n")
    dosya.close()
    messagebox.showinfo("Bilgilendirme" , "Dosya Bulundugunuz Dizine Kaydedildi")

def serverTarama():
    temizle()
    durum["text"] = "Tarama Var"
    durum["fg"] = "green"
    for i in range(1, 100, 10):
        payload = get("http://www.bing.com/search?q=ip:{}&first=1".format(ipiste.get())).text
        bul = findall("<cite>(.*?)</cite>", payload)
        for i in bul:
            serverlist.append(i)
    for i in range(len(serverlist)):
        serverdakisiteler.insert(END, serverlist[i])



baslik = Label(text="Turkz.Org Ar-Ge Server IP Scanner",relief="sunken", fg="blue")
baslik.place(x=95,y=10)

durum = Label()
durum["text"] = "Tarama Yok"
durum["fg"] = "red"
durum.place(x=315, y=10)

ipistetext = Label(text="IP Adresi: ", fg="blue")
ipistetext.place(y=40)

ipiste = Entry(width=15)
ipiste.place(x= 95,y=40)

bloktaramabut = Button(text="Blok Tara", fg="blue", command=blokTarama)
bloktaramabut.place(x=225, y=37)

servertaramabut = Button(text="Server Tara", fg="blue", width=7, command=serverTarama)
servertaramabut.place(x=310, y=37)

bulunaniplertext1 = Label(text="Blok IP Adresleri")
bulunaniplertext1.place(x=45, y=70)

bulunanipler = Listbox()
bulunanipler.place(x=10, y= 90)

blokciktial = Button(text="Blok Çıktısı", command=blokCikti)
blokciktial.place(x= 10, y=250)

bulunaniplertext2 = Label(text="Serverdaki Siteler")
bulunaniplertext2.place(x=255, y=70)

serverdakisiteler = Listbox()
serverdakisiteler.place(x=225, y= 90)

serverciktial = Button(text="Server Çıktısı", command=serverCikti)
serverciktial.place(x= 285, y=250)

tzgrup = Label(text="Araştırma & Geliştirme", fg="blue")
tzgrup.place(x=135, y=250)
tzgrup = Label(text="Turkz Hack Grup", fg="blue")
tzgrup.place(x=150, y=265)
tzgrup = Label(text="www.turkz.org", fg="blue")
tzgrup.place(x=155, y=280)

mainloop()
