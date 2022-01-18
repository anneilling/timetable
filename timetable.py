from tkinter import *
aken=Tk()
aken.title("Расписание")
aken.geometry("830x560")
aken.configure(bg="white")


Label(text=" ",width=20,height=5,relief="ridge").grid(row=0,column=0) #номер урока
Label(text="0 ",width=8,height=5,relief="ridge").grid(row=0,column=1)
Label(text="1 ",width=8,height=5,relief="ridge").grid(row=0,column=2)
Label(text="2 ",width=8,height=5,relief="ridge").grid(row=0,column=3)
Label(text="3 ",width=8,height=5,relief="ridge").grid(row=0,column=4)
Label(text="4 ",width=8,height=5,relief="ridge").grid(row=0,column=5)
Label(text="5 ",width=8,height=5,relief="ridge").grid(row=0,column=6) 
Label(text="6 ",width=8,height=5,relief="ridge").grid(row=0,column=7)
Label(text="7 ",width=8,height=5,relief="ridge").grid(row=0,column=8)
Label(text="8 ",width=8,height=5,relief="ridge").grid(row=0,column=9)
Label(text="9 ",width=8,height=5,relief="ridge").grid(row=0,column=10)
Label(text="10 ",width=8,height=5,relief="ridge").grid(row=0,column=11)


Label(text="Esmaspäev ",width=20,height=6,relief="ridge").grid(row=1,column=0) #день недели
Label(text="Tesipäev ",width=20,height=6,relief="ridge").grid(row=2,column=0)
Label(text="Kolmapäev ",width=20,height=6,relief="ridge").grid(row=3,column=0)
Label(text="Neljapäev ",width=20,height=6,relief="ridge").grid(row=4,column=0)
Label(text="Reede ",width=20,height=6,relief="ridge").grid(row=5,column=0)


Label(text=" ",width=8,height=6,relief="ridge").grid(row=1,column=1) #0уроки
Label(text=" ",width=8,height=6,relief="ridge").grid(row=2,column=1)
Label(text=" ",width=8,height=6,relief="ridge").grid(row=3,column=1)
Label(text=" ",width=8,height=6,relief="ridge").grid(row=4,column=1)
Label(text=" ",width=8,height=6,relief="ridge").grid(row=5,column=1)


Label(text=" ",width=8,height=6,relief="ridge").grid(row=1,column=2) #1урокифон
Label(text=" ",width=8,height=6,relief="ridge").grid(row=2,column=2)
Label(text=" ",width=8,height=6,relief="ridge").grid(row=3,column=2)
Label(text=" ",width=8,height=6,relief="ridge").grid(row=4,column=2)
Label(text=" ",width=8,height=6,relief="ridge").grid(row=5,column=2)
Label(text="1234",borderwidth=1,width=8,height=3,bg="#cab4c7").grid(row=1,column=2,sticky=S) #1уроки
Label(text="4321",borderwidth=1,width=8,height=6,bg="#e080e0").grid(row=2,column=2)
Label(text="5678",borderwidth=1,width=8,height=3,bg="#ff80ff").grid(row=3,column=2,sticky=N)
Label(text="8765",borderwidth=1,width=8,height=6,bg="#80e092").grid(row=4,column=2)
Label(text="1234",borderwidth=1,width=8,height=3,bg="#ff80ff").grid(row=5,column=2,sticky=N)
Label(text="4321",borderwidth=1,width=8,height=3,bg="#ff80a2").grid(row=5,column=2,sticky=S)


Label(text=" ",width=8,height=6,relief="ridge").grid(row=1,column=3) #1урокифон
Label(text=" ",width=8,height=6,relief="ridge").grid(row=2,column=3)
Label(text=" ",width=8,height=6,relief="ridge").grid(row=3,column=3)
Label(text=" ",width=8,height=6,relief="ridge").grid(row=4,column=3)
Label(text=" ",width=8,height=6,relief="ridge").grid(row=5,column=3)
Label(text=" ",width=8,height=6,relief="ridge",bg="#80e092").grid(row=1,column=3) #2уроки
Label(text=" ",width=8,height=6,relief="ridge",bg="#abe0ff").grid(row=2,column=3)
Label(text=" ",width=8,height=6,relief="ridge",bg="#e080ce").grid(row=3,column=3)
Label(text=" ",width=8,height=6,relief="ridge",bg="#80e092").grid(row=4,column=3)
Label(text=" ",width=8,height=6,relief="ridge",bg="#ff80ff").grid(row=5,column=3)


Label(text=" ",width=8,height=6,relief="ridge",bg="#80e092").grid(row=1,column=4) #3уроки
Label(text=" ",width=8,height=6,relief="ridge").grid(row=2,column=4)
Label(text=" ",width=8,height=6,relief="ridge").grid(row=3,column=4)
Label(text=" ",width=8,height=6,relief="ridge").grid(row=4,column=4)
Label(text=" ",width=8,height=6,relief="ridge").grid(row=5,column=4)


Label(text=" ",width=8,height=6,relief="ridge").grid(row=1,column=5) #4уроки
Label(text=" ",width=8,height=6,relief="ridge").grid(row=2,column=5)
Label(text=" ",width=8,height=6,relief="ridge").grid(row=3,column=5)
Label(text=" ",width=8,height=6,relief="ridge").grid(row=4,column=5)
Label(text=" ",width=8,height=6,relief="ridge").grid(row=5,column=5)


Label(text=" ",width=8,height=6,relief="ridge").grid(row=1,column=6) #5уроки
Label(text=" ",width=8,height=6,relief="ridge").grid(row=2,column=6)
Label(text=" ",width=8,height=6,relief="ridge").grid(row=3,column=6)
Label(text=" ",width=8,height=6,relief="ridge").grid(row=4,column=6)
Label(text=" ",width=8,height=6,relief="ridge").grid(row=5,column=6)


Label(text=" ",width=8,height=6,relief="ridge").grid(row=1,column=7) #6уроки
Label(text=" ",width=8,height=6,relief="ridge").grid(row=2,column=7)
Label(text=" ",width=8,height=6,relief="ridge").grid(row=3,column=7)
Label(text=" ",width=8,height=6,relief="ridge").grid(row=4,column=7)
Label(text=" ",width=8,height=6,relief="ridge").grid(row=5,column=7)


Label(text=" ",width=8,height=6,relief="ridge").grid(row=1,column=8) #7уроки
Label(text=" ",width=8,height=6,relief="ridge").grid(row=2,column=8)
Label(text=" ",width=8,height=6,relief="ridge").grid(row=3,column=8)
Label(text=" ",width=8,height=6,relief="ridge").grid(row=4,column=8)
Label(text=" ",width=8,height=6,relief="ridge").grid(row=5,column=8)


Label(text=" ",width=8,height=6,relief="ridge").grid(row=1,column=9) #8уроки
Label(text=" ",width=8,height=6,relief="ridge").grid(row=2,column=9)
Label(text=" ",width=8,height=6,relief="ridge").grid(row=3,column=9)
Label(text=" ",width=8,height=6,relief="ridge").grid(row=4,column=9)
Label(text=" ",width=8,height=6,relief="ridge").grid(row=5,column=9)


Label(text=" ",width=8,height=6,relief="ridge").grid(row=1,column=10) #9уроки
Label(text=" ",width=8,height=6,relief="ridge").grid(row=2,column=10)
Label(text=" ",width=8,height=6,relief="ridge").grid(row=3,column=10)
Label(text=" ",width=8,height=6,relief="ridge").grid(row=4,column=10)
Label(text=" ",width=8,height=6,relief="ridge").grid(row=5,column=10)


Label(text=" ",width=8,height=6,relief="ridge").grid(row=1,column=11) #10уроки
Label(text=" ",width=8,height=6,relief="ridge").grid(row=2,column=11)
Label(text=" ",width=8,height=6,relief="ridge").grid(row=3,column=11)
Label(text=" ",width=8,height=6,relief="ridge").grid(row=4,column=11)
Label(text=" ",width=8,height=6,relief="ridge").grid(row=5,column=11)




aken.mainloop()
