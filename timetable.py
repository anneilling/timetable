from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
aken=Tk()
aken.title("Расписание")
aken.geometry("830x577")
aken.configure(bg="white")
def uus_aken(ind:int):
    if askyesno("Küsimus","Kas teen lahti?"):
        showinfo("Vatus","Teen aken lahti")
    else:
        showinfo("Vastus","Panen aken kinni")
        aken.destroy()
    uusaken=Toplevel()
    tabs=ttk.Notebook(uusaken)
    #texts

def tund_eesti(event):
    aken1=Toplevel()
    aken1.title("eesti")
    aken1.geometry("200x100")
    aken1.configure(bg="thistle")
    Label(aken1,text="Эстонский...",width=30).grid()

def tund_log(event):
    aken1=Toplevel()
    aken1.title("Logistika")
    aken1.geometry("200x100")
    aken1.configure(bg="thistle")
    Label(aken1,text="Не опаздывать",width=30).grid()
def tund_mat(event):
    aken1=Toplevel()
    aken1.title("Matematika")
    aken1.geometry("200x100")
    aken1.configure(bg="thistle")
    Label(aken1,text="Математика она и в африке...",width=30).grid()
def tund_rus(event):
    aken1=Toplevel()
    aken1.title("Ruskie")
    aken1.geometry("200x100")
    aken1.configure(bg="thistle")
    Label(aken1,text="КОМАНДИРОВАнНЫЕ??",width=30).grid()
def tund_tugmat(event):
    aken1=Toplevel()
    aken1.title("MatemV2.0")
    aken1.geometry("200x100")
    aken1.configure(bg="thistle")
    Label(aken1,text="Для де*илов",width=30).grid()
def tund_tugkeem(event):
    aken1=Toplevel()
    aken1.title("KeemiaV2.0")
    aken1.geometry("200x100")
    aken1.configure(bg="thistle")
    Label(aken1,text="Для де*илов",width=30).grid()
def tund_prog(event):
    aken1=Toplevel()
    aken1.title("I LOVE PROGRAMERIMINE")
    aken1.geometry("200x100")
    aken1.configure(bg="thistle")
    Label(aken1,text="Лучший урок на свете!!11!11!!11!11",width=30).grid()
def tund_fus(event):
    aken1=Toplevel()
    aken1.title("FUSIKA")
    aken1.geometry("200x100")
    aken1.configure(bg="thistle")
    Label(aken1,text="Красивый конспект",width=30).grid()
def tund_kunst(event):
    aken1=Toplevel()
    aken1.title("KUNST")
    aken1.geometry("200x100")
    aken1.configure(bg="thistle")
    Label(aken1,text="Поспать подольше",width=30).grid()
def tund_keh(event):
    aken1=Toplevel()
    aken1.title("eesti")
    aken1.geometry("200x100")
    aken1.configure(bg="thistle")
    Label(aken1,text="Режим невидимки",width=30).grid()
def tund_ingl(event):
    aken1=Toplevel()
    aken1.title("eesti")
    aken1.geometry("200x100")
    aken1.configure(bg="angl")
    Label(aken1,text="Страдать",width=30).grid()
def tund_merk(event):
    aken1=Toplevel()
    aken1.title("eesti")
    aken1.geometry("200x100")
    aken1.configure(bg="thistle")
    Label(aken1,text="Спать...",width=30).grid()
def tund_alin(event):
    aken1=Toplevel()
    aken1.title("eesti")
    aken1.geometry("200x100")
    aken1.configure(bg="thistle")
    Label(aken1,text="Домой :^)",width=30).grid()


Label(text=" ",width=20,height=6,relief="solid").grid(row=0,column=0) #номер урока
Label(text="0 ",width=8,height=6,relief="solid").grid(row=0,column=1)
Label(text="1 ",width=8,height=6,relief="solid").grid(row=0,column=2)
Label(text="2 ",width=8,height=6,relief="solid").grid(row=0,column=3)
Label(text="3 ",width=8,height=6,relief="solid").grid(row=0,column=4)
Label(text="4 ",width=8,height=6,relief="solid").grid(row=0,column=5)
Label(text="5 ",width=8,height=6,relief="solid").grid(row=0,column=6) 
Label(text="6 ",width=8,height=6,relief="solid").grid(row=0,column=7)
Label(text="7 ",width=8,height=6,relief="solid").grid(row=0,column=8)
Label(text="8 ",width=8,height=6,relief="solid").grid(row=0,column=9)
Label(text="9 ",width=8,height=6,relief="solid").grid(row=0,column=10)
Label(text="10 ",width=8,height=6,relief="solid").grid(row=0,column=11)
Label(text=" ",borderwidth=1,width=20,height=6).grid(row=0,column=0) 
Label(text="0 ",borderwidth=1,width=8,height=6).grid(row=0,column=1)
Label(text="1 ",borderwidth=1,width=8,height=6).grid(row=0,column=2)
Label(text="2 ",borderwidth=1,width=8,height=6).grid(row=0,column=3)
Label(text="3 ",borderwidth=1,width=8,height=6).grid(row=0,column=4)
Label(text="4 ",borderwidth=1,width=8,height=6).grid(row=0,column=5)
Label(text="5 ",borderwidth=1,width=8,height=6).grid(row=0,column=6) 
Label(text="6 ",borderwidth=1,width=8,height=6).grid(row=0,column=7)
Label(text="7 ",borderwidth=1,width=8,height=6).grid(row=0,column=8)
Label(text="8 ",borderwidth=1,width=8,height=6).grid(row=0,column=9)
Label(text="9 ",borderwidth=1,width=8,height=6).grid(row=0,column=10)
Label(text="10 ",borderwidth=1,width=8,height=6).grid(row=0,column=11)


Label(text="Esmaspäev ",width=20,height=6,relief="solid").grid(row=1,column=0) #день недели
Label(text="Tesipäev ",width=20,height=6,relief="solid").grid(row=2,column=0)
Label(text="Kolmapäev ",width=20,height=6,relief="solid").grid(row=3,column=0)
Label(text="Neljapäev ",width=20,height=6,relief="solid").grid(row=4,column=0)
Label(text="Reede ",width=20,height=6,relief="solid").grid(row=5,column=0)
Label(text="Esmaspäev ",borderwidth=1,width=20,height=6).grid(row=1,column=0) 
Label(text="Tesipäev ",borderwidth=1,width=20,height=6).grid(row=2,column=0)
Label(text="Kolmapäev ",borderwidth=1,width=20,height=6).grid(row=3,column=0)
Label(text="Neljapäev ",borderwidth=1,width=20,height=6).grid(row=4,column=0)
Label(text="Reede ",borderwidth=1,width=20,height=6).grid(row=5,column=0)


Label(text=" ",width=8,height=6,relief="solid").grid(row=1,column=1) #0уроки
Label(text=" ",width=8,height=6,relief="solid").grid(row=2,column=1)
Label(text=" ",width=8,height=6,relief="solid").grid(row=3,column=1)
Label(text=" ",width=8,height=6,relief="solid").grid(row=4,column=1)
Label(text=" ",width=8,height=6,relief="solid").grid(row=5,column=1)
Label(text=" ",borderwidth=1,width=8,height=6,bg="white").grid(row=1,column=1) 
Label(text=" ",borderwidth=1,width=8,height=6,bg="white").grid(row=2,column=1)
Label(text=" ",borderwidth=1,width=8,height=6,bg="white").grid(row=3,column=1)
Label(text=" ",borderwidth=1,width=8,height=6,bg="white").grid(row=4,column=1)
Label(text=" ",borderwidth=1,width=8,height=6,bg="white").grid(row=5,column=1)

Label(text=" ",width=8,height=6,relief="solid").grid(row=1,column=2) #1урокифон
Label(text=" ",width=8,height=6,relief="solid").grid(row=2,column=2)
Label(text=" ",width=8,height=6,relief="solid").grid(row=3,column=2)
Label(text=" ",width=8,height=6,relief="solid").grid(row=4,column=2)
Label(text=" ",width=8,height=6,relief="solid").grid(row=5,column=2)


Label(text=" ",width=8,height=6,relief="solid").grid(row=1,column=3) #2урокифон
Label(text=" ",width=8,height=6,relief="solid").grid(row=2,column=3)
Label(text=" ",width=8,height=6,relief="solid").grid(row=3,column=3)
Label(text=" ",width=8,height=6,relief="solid").grid(row=4,column=3)
Label(text=" ",width=8,height=6,relief="solid").grid(row=5,column=3)


Label(text=" ",width=8,height=6,relief="solid").grid(row=1,column=4) #3уроки
Label(text=" ",width=8,height=6,relief="solid").grid(row=2,column=4)
Label(text=" ",width=8,height=6,relief="solid").grid(row=3,column=4)
Label(text=" ",width=8,height=6,relief="solid").grid(row=4,column=4)
Label(text=" ",width=8,height=6,relief="solid").grid(row=5,column=4)


Label(text=" ",width=8,height=6,relief="solid").grid(row=1,column=5) #4уроки
Label(text=" ",width=8,height=6,relief="solid").grid(row=2,column=5)
Label(text=" ",width=8,height=6,relief="solid").grid(row=3,column=5)
Label(text=" ",width=8,height=6,relief="solid").grid(row=4,column=5)
Label(text=" ",width=8,height=6,relief="solid").grid(row=5,column=5)


Label(text=" ",width=8,height=6,relief="solid").grid(row=1,column=6) #5уроки
Label(text=" ",width=8,height=6,relief="solid").grid(row=2,column=6)
Label(text=" ",width=8,height=6,relief="solid").grid(row=3,column=6)
Label(text=" ",width=8,height=6,relief="solid").grid(row=4,column=6)
Label(text=" ",width=8,height=6,relief="solid").grid(row=5,column=6)


Label(text=" ",width=8,height=6,relief="solid").grid(row=1,column=7) #6уроки
Label(text=" ",width=8,height=6,relief="solid").grid(row=2,column=7)
Label(text=" ",width=8,height=6,relief="solid").grid(row=3,column=7)
Label(text=" ",width=8,height=6,relief="solid").grid(row=4,column=7)
Label(text=" ",width=8,height=6,relief="solid").grid(row=5,column=7)


Label(text=" ",width=8,height=6,relief="solid").grid(row=1,column=8) #7уроки
Label(text=" ",width=8,height=6,relief="solid").grid(row=2,column=8)
Label(text=" ",width=8,height=6,relief="solid").grid(row=3,column=8)
Label(text=" ",width=8,height=6,relief="solid").grid(row=4,column=8)
Label(text=" ",width=8,height=6,relief="solid").grid(row=5,column=8)


Label(text=" ",width=8,height=6,relief="solid").grid(row=1,column=9) #8уроки
Label(text=" ",width=8,height=6,relief="solid").grid(row=2,column=9)
Label(text=" ",width=8,height=6,relief="solid").grid(row=3,column=9)
Label(text=" ",width=8,height=6,relief="solid").grid(row=4,column=9)
Label(text=" ",width=8,height=6,relief="solid").grid(row=5,column=9)


Label(text=" ",width=8,height=6,relief="solid").grid(row=1,column=10) #9уроки
Label(text=" ",width=8,height=6,relief="solid").grid(row=2,column=10)
Label(text=" ",width=8,height=6,relief="solid").grid(row=3,column=10)
Label(text=" ",width=8,height=6,relief="solid").grid(row=4,column=10)
Label(text=" ",width=8,height=6,relief="solid").grid(row=5,column=10)


Label(text=" ",width=8,height=6,relief="solid").grid(row=1,column=11) #10уроки
Label(text=" ",width=8,height=6,relief="solid").grid(row=2,column=11)
Label(text=" ",width=8,height=6,relief="solid").grid(row=3,column=11)
Label(text=" ",width=8,height=6,relief="solid").grid(row=4,column=11)
Label(text=" ",width=8,height=6,relief="solid").grid(row=5,column=11)


eesti=Label(text="Eesti keel\nkui teine",borderwidth=1,width=8,height=3,bg="#cab4c7")
eesti.grid(row=1,column=2,sticky=S) #1уроки
Label(text=" ",width=8,height=3,borderwidth=1,bg="white").grid(row=1,column=2,sticky=N) 
tugkeem=Label(text="Tugiõpe\n(keemia)",borderwidth=1,width=8,height=6,bg="#e080e0")
tugkeem.grid(row=2,column=2)
eesti2=Label(text="Eesti keel\nkui teine",borderwidth=1,width=8,height=3,bg="#ff80ff")
eesti2.grid(row=3,column=2,sticky=N)
Label(text=" ",borderwidth=1,width=8,height=3,bg="white").grid(row=3,column=2,sticky=S)
log=Label(text="Logistikateenused\nja varude juhtimine",relief="solid",borderwidth=1,width=8,height=6,bg="#80e092")
log.grid(row=4,column=2,sticky=N+S+W+E,columnspan=2)
merk=Label(text="arenduskeskkonna\nloomine\n(IT valdkonna)",relief="solid",borderwidth=1,width=8,height=3,bg="#ff80a2")
merk.grid(row=5,column=2,sticky=SW+SE,columnspan=2)
eesti3=Label(text="Eesti keel",relief="solid",borderwidth=1,width=8,height=3,bg="#ff80ff")
eesti3.grid(row=5,column=2,sticky=NW+NE,columnspan=2)

kunst=Label(text="Kunstiained (eesti\nkeeles)",relief="solid",borderwidth=1,width=8,height=6,bg="#e080ce")
kunst.grid(row=3,column=3,sticky=N+S+W+E,columnspan=2)#2уроки
log2=Label(text="Logistikateenused\nja varude juhtimine",relief="solid",borderwidth=1,width=8,height=6,bg="#80e092")
log2.grid(row=1,column=3,sticky=N+S+W+E, columnspan=2) 
prog=Label(text="Programmeerimise alused\n(eesti keeles)",relief="solid",borderwidth=1,width=8,height=6,bg="#abe0ff")
prog.grid(row=2,column=3,sticky=N+S+W+E, columnspan=3)

Label(text=" ",borderwidth=1,width=8,height=6,bg="white").grid(row=4,column=4) #3уроки
prog2=Label(text="Programmeerimise alused\n(eesti keeles)",relief="solid",borderwidth=1,width=8,height=6,bg="#abe0ff")
prog2.grid(row=5,column=4,sticky=N+S+W+E,columnspan=5)

mat=Label(text="Matemaatika",relief="solid",borderwidth=1,width=8,height=6,bg="#fcb9d0")
mat.grid(row=1,column=5,sticky=N+S+W+E,columnspan=2) #4уроки
Label(text=" ",borderwidth=1,width=8,height=6,bg="white").grid(row=3,column=5)
prog3=Label(text="Programmeerimise\nalused (eesti\nkeeles)",relief="solid",borderwidth=1,width=8,height=6,bg="#abe0ff")
prog3.grid(row=4,column=5,sticky=N+S+W+E,columnspan=2)

Label(text=" ",borderwidth=1,width=8,height=6,bg="white").grid(row=2,column=6) #5уроки
keh=Label(text="Kehaline kasvatus",relief="solid",borderwidth=1,width=8,height=6,bg="#e080ce")
keh.grid(row=3,column=6,sticky=N+S+W+E,columnspan=2)

Label(text=" ",borderwidth=1,width=8,height=6,bg="white").grid(row=1,column=7) #6уроки
fus=Label(text="Füüsika",borderwidth=1,relief="solid",width=8,height=6,bg="#fcb9d0")
fus.grid(row=2,column=7,sticky=N+S+W+E,columnspan=2)
ing=Label(text="Inglise keel",relief="solid",borderwidth=1,width=8,height=3,bg="#fffff0")
ing.grid(row=4,column=7,sticky=NW+NE,columnspan=2)
merk2=Label(text="arenduskeskkonna\nloomine\n(IT valdkonna)",relief="solid",borderwidth=1,width=8,height=3,bg="#ff80a2")
merk2.grid(row=4,column=7,sticky=SW+SE,columnspan=2)

rus=Label(text="Keel ja\nkirjandus",borderwidth=1,relief="solid",width=8,height=6,bg="#94ed80")
rus.grid(row=1,column=8,sticky=N+S+W+E,columnspan=2) #7уроки
Label(text=" ",borderwidth=1,width=8,height=6,bg="white").grid(row=3,column=8)

Label(text=" ",width=8,height=6,borderwidth=1,bg="white").grid(row=2,column=9) #8уроки
Label(text=" ",width=8,height=6,borderwidth=1,bg="white").grid(row=3,column=9)
merk3=Label(text="arenduskeskkonna\nloomine\n(IT valdkonna)",relief="solid",borderwidth=1,width=8,height=3,bg="#ff80a2")
merk3.grid(row=4,column=9,sticky=NW+NE,columnspan=2)
merk4=Label(text="arenduskeskkonna\nloomine\n(IT valdkonna)",relief="solid",borderwidth=1,width=8,height=3,bg="#ff80a2")
merk4.grid(row=5,column=9,sticky=NW+NE,columnspan=2)
est1=Label(text="Eesti keel",relief="solid",borderwidth=1,width=8,height=3,bg="#cab4c7")
est1.grid(row=4,column=9,sticky=SW+SE,columnspan=2)
ingl=Label(text="Inglise keel",relief="solid",borderwidth=1,width=8,height=3,bg="#80ff80")
ingl.grid(row=5,column=9,sticky=SW+SE,columnspan=2)

tugmat=Label(text="Tugiõpe\n(matema\natika)",width=8,height=6,borderwidth=1,bg="#fcb9d0")
tugmat.grid(row=1,column=10) #9уроки
Label(text=" ",width=8,height=6,borderwidth=1,bg="white").grid(row=2,column=10)
Label(text=" ",width=8,height=6,borderwidth=1,bg="white").grid(row=3,column=10)

Label(text=" ",width=8,height=6,borderwidth=1,bg="white").grid(row=1,column=11) #10уроки
Label(text=" ",width=8,height=6,borderwidth=1,bg="white").grid(row=2,column=11)
Label(text=" ",width=8,height=6,borderwidth=1,bg="white").grid(row=3,column=11)
alin=Label(text="Rühmaju\nhataja\ntund",width=8,height=6,borderwidth=1,bg="#ff80ff")
alin.grid(row=4,column=11)

Label(text=" ",width=8,height=6,borderwidth=1,bg="white").grid(row=5,column=11)
Label(aken, borderwidth=0, relief="solid", text="7.40-8.25", width=8,height=1).grid(row=0, column=1,sticky=S)
Label(aken, borderwidth=0, relief="solid", text="8.30-9.15", width=8,height=1).grid(row=0, column=2,sticky=S)
Label(aken, borderwidth=0, relief="solid", text="9.20-10.05", width=8,height=1).grid(row=0, column=3,sticky=S)
Label(aken, borderwidth=0, relief="solid", text="10.10-10.55", width=8,height=1).grid(row=0, column=4,sticky=S)
Label(aken, borderwidth=0, relief="solid", text="11.00-11.45", width=8,height=1).grid(row=0, column=5,sticky=S)
Label(aken, borderwidth=0, relief="solid", text="11.50-12.35", width=8,height=1).grid(row=0, column=6,sticky=S)
Label(aken, borderwidth=0, relief="solid", text="12.40-13.25", width=8,height=1).grid(row=0, column=7,sticky=S)
Label(aken, borderwidth=0, relief="solid", text="13.30-14.15", width=8,height=1).grid(row=0, column=8,sticky=S)
Label(aken, borderwidth=0, relief="solid", text="14.20-15.05", width=8,height=1).grid(row=0, column=9,sticky=S)
Label(aken, borderwidth=0, relief="solid", text="15.10-15.55", width=8,height=1).grid(row=0, column=10,sticky=S)
Label(aken, borderwidth=0, relief="solid", text="16.00-16.45", width=8,height=1).grid(row=0, column=11,sticky=S)

eesti.bind("<Button-1>",
           lambda e="Discription": tund_eesti(e))
eesti2.bind("<Button-1>",
          lambda e="Discription": tund_eesti(e))
eesti3.bind("<Button-1>",
          lambda e="Discription": tund_eesti(e))
est1.bind("<Button-1>",
          lambda e="Discription": tund_eesti(e))
log.bind("<Button-1>",
          lambda e="Discription": tund_log(e))
log2.bind("<Button-1>",
          lambda e="Discription": tund_log(e))
mat.bind("<Button-1>",
          lambda e="Discription": tund_mat(e))
rus.bind("<Button-1>",
          lambda e="Discription": tund_rus(e))
tugmat.bind("<Button-1>",
          lambda e="Discription": tund_tugmat(e))
tugkeem.bind("<Button-1>",
          lambda e="Discription": tund_tugkeem(e))
prog.bind("<Button-1>",
          lambda e="Discription": tund_prog(e))
prog2.bind("<Button-1>",
          lambda e="Discription": tund_prog(e))
prog3.bind("<Button-1>",
          lambda e="Discription": tund_prog(e))
fus.bind("<Button-1>",
          lambda e="Discription": tund_fus(e))
kunst.bind("<Button-1>",
          lambda e="Discription": tund_kunst(e))
keh.bind("<Button-1>",
          lambda e="Discription": tund_keh(e))
ingl.bind("<Button-1>",
          lambda e="Discription": tund_ingl(e))
ing.bind("<Button-1>",
          lambda e="Discription": urok_ingl(e))
merk.bind("<Button-1>",
          lambda e="Discription": tund_merk(e))
merk2.bind("<Button-1>",
          lambda e="Discription": tund_merk(e))
merk3.bind("<Button-1>",
          lambda e="Discription": tund_merk(e))
merk4.bind("<Button-1>",
          lambda e="Discription": tund_merk(e))
alin.bind("<Button-1>",
          lambda e="Discription": tund_alin(e))
   

aken.mainloop()
