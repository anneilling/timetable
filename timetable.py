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

Label(text="Eesti keel\nkui teine",borderwidth=1,width=8,height=3,bg="#cab4c7").grid(row=1,column=2,sticky=S) #1уроки
Label(text=" ",width=8,height=3,borderwidth=1,bg="white").grid(row=1,column=2,sticky=N) 
Label(text="Tugiõpe\n(keemia)",borderwidth=1,width=8,height=6,bg="#e080e0").grid(row=2,column=2)
Label(text="Eesti keel\nkui teine",borderwidth=1,width=8,height=3,bg="#ff80ff").grid(row=3,column=2,sticky=N)
Label(text=" ",borderwidth=1,width=8,height=3,bg="white").grid(row=3,column=2,sticky=S)
Label(text="Logistikateenused\nja varude juhtimine",relief="solid",borderwidth=1,width=8,height=6,bg="#80e092").grid(row=4,column=2,sticky=N+S+W+E,columnspan=2)
Label(text="arenduskeskkonna\nloomine\n(IT valdkonna)",relief="solid",borderwidth=1,width=8,height=3,bg="#ff80a2").grid(row=5,column=2,sticky=SW+SE,columnspan=2)
Label(text="Eesti keel",relief="solid",borderwidth=1,width=8,height=3,bg="#ff80ff").grid(row=5,column=2,sticky=NW+NE,columnspan=2)

Label(text="Kunstiained (eesti\nkeeles)",relief="solid",borderwidth=1,width=8,height=6,bg="#e080ce").grid(row=3,column=3,sticky=N+S+W+E,columnspan=2)#2уроки
Label(text="Logistikateenused\nja varude juhtimine",relief="solid",borderwidth=1,width=8,height=6,bg="#80e092").grid(row=1,column=3,sticky=N+S+W+E, columnspan=2) 
Label(text="Programmeerimise alused\n(eesti keeles)",relief="solid",borderwidth=1,width=8,height=6,bg="#abe0ff").grid(row=2,column=3,sticky=N+S+W+E, columnspan=3)

Label(text=" ",borderwidth=1,width=8,height=6,bg="white").grid(row=4,column=4) #3уроки
Label(text="Programmeerimise alused\n(eesti keeles)",relief="solid",borderwidth=1,width=8,height=6,bg="#abe0ff").grid(row=5,column=4,sticky=N+S+W+E,columnspan=5)

Label(text="Matemaatika",relief="solid",borderwidth=1,width=8,height=6,bg="#fcb9d0").grid(row=1,column=5,sticky=N+S+W+E,columnspan=2) #4уроки
Label(text=" ",borderwidth=1,width=8,height=6,bg="white").grid(row=3,column=5)
Label(text="Programmeerimise\nalused (eesti\nkeeles)",relief="solid",borderwidth=1,width=8,height=6,bg="#abe0ff").grid(row=4,column=5,sticky=N+S+W+E,columnspan=2)

Label(text=" ",borderwidth=1,width=8,height=6,bg="white").grid(row=2,column=6) #5уроки
Label(text="Kehaline kasvatus",relief="solid",borderwidth=1,width=8,height=6,bg="#e080ce").grid(row=3,column=6,sticky=N+S+W+E,columnspan=2)

Label(text=" ",borderwidth=1,width=8,height=6,bg="white").grid(row=1,column=7) #6уроки
Label(text="Füüsika",borderwidth=1,relief="solid",width=8,height=6,bg="#fcb9d0").grid(row=2,column=7,sticky=N+S+W+E,columnspan=2)
Label(text="Inglise keel",relief="solid",borderwidth=1,width=8,height=3,bg="#fffff0").grid(row=4,column=7,sticky=NW+NE,columnspan=2)
Label(text="arenduskeskkonna\nloomine\n(IT valdkonna)",relief="solid",borderwidth=1,width=8,height=3,bg="#ff80a2").grid(row=4,column=7,sticky=SW+SE,columnspan=2)

Label(text="Keel ja\nkirjandus",borderwidth=1,relief="solid",width=8,height=6,bg="#94ed80").grid(row=1,column=8,sticky=N+S+W+E,columnspan=2) #7уроки
Label(text=" ",borderwidth=1,width=8,height=6,bg="white").grid(row=3,column=8)

Label(text=" ",width=8,height=6,borderwidth=1,bg="white").grid(row=2,column=9) #8уроки
Label(text=" ",width=8,height=6,borderwidth=1,bg="white").grid(row=3,column=9)
Label(text="arenduskeskkonna\nloomine\n(IT valdkonna)",relief="solid",borderwidth=1,width=8,height=3,bg="#ff80a2").grid(row=4,column=9,sticky=NW+NE,columnspan=2)
Label(text="arenduskeskkonna\nloomine\n(IT valdkonna)",relief="solid",borderwidth=1,width=8,height=3,bg="#ff80a2").grid(row=5,column=9,sticky=NW+NE,columnspan=2)
Label(text="Eesti keel",relief="solid",borderwidth=1,width=8,height=3,bg="#cab4c7").grid(row=4,column=9,sticky=SW+SE,columnspan=2)
Label(text="Inglise keel",relief="solid",borderwidth=1,width=8,height=3,bg="#80ff80").grid(row=5,column=9,sticky=SW+SE,columnspan=2)

Label(text="Tugiõpe\n(matema\natika)",width=8,height=6,borderwidth=1,bg="#fcb9d0").grid(row=1,column=10) #9уроки
Label(text=" ",width=8,height=6,borderwidth=1,bg="white").grid(row=2,column=10)
Label(text=" ",width=8,height=6,borderwidth=1,bg="white").grid(row=3,column=10)

Label(text=" ",width=8,height=6,borderwidth=1,bg="white").grid(row=1,column=11) #10уроки
Label(text=" ",width=8,height=6,borderwidth=1,bg="white").grid(row=2,column=11)
Label(text=" ",width=8,height=6,borderwidth=1,bg="white").grid(row=3,column=11)
Label(text="Rühmaju\nhataja\ntund",width=8,height=6,borderwidth=1,bg="#ff80ff").grid(row=4,column=11)
Label(text=" ",width=8,height=6,borderwidth=1,bg="white").grid(row=5,column=11)








aken.mainloop()
