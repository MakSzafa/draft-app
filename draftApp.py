from tkinter import *

from PIL import Image, ImageTk


class MainScreen():

    def __init__(self, okno):
        self.mainFrame = Frame(okno)
        self.mainFrame.grid()

        # cele kompozycji
        self.cele_kompozycji = Label(okno, text="Composition goals:", font=("Arial Bold", 15),
                                     fg="blue")

        self.scaling_bot_goal = Label(okno, text="Scaling ADC", font=("Arial Bold", 15),
                                      fg="red")
        self.prio_bot_goal = Label(okno, text="Prio ADC", font=("Arial Bold", 15),
                                   fg="red")
        self.scaling_mid_goal = Label(okno, text="Scaling MID", font=("Arial Bold", 15),
                                      fg="red")
        self.prio_mid_goal = Label(okno, text="Prio MID", font=("Arial Bold", 15),
                                   fg="red")
        self.splitpush_mid_goal = Label(okno, text="Splitpush MID", font=("Arial Bold", 15),
                                        fg="red")
        self.strong2v2_mid_goal = Label(okno, text="Strong 2v2 MID", font=("Arial Bold", 15),
                                        fg="red")
        self.scaling_jng_goal = Label(okno, text="Scaling JNG", font=("Arial Bold", 15),
                                      fg="red")
        self.safe_engage_jng_goal = Label(okno, text="Safe JNG with engage", font=("Arial Bold", 15),
                                          fg="red")
        self.mobility_engage_jng_goal = Label(okno, text="JNG with mobility and engage", font=("Arial Bold", 15),
                                              fg="red")
        self.early_jng_goal = Label(okno, text="Early prio JNG", font=("Arial Bold", 15),
                                    fg="red")
        # cele kompozycji DONE
        self.scaling_bot_goal_done = Label(okno, text="Scaling ADC", font=("Arial Bold", 15),
                                           fg="blue")
        self.prio_bot_goal_done = Label(okno, text="Prio ADC", font=("Arial Bold", 15),
                                        fg="blue")
        self.scaling_mid_goal_done = Label(okno, text="Scaling MID", font=("Arial Bold", 15),
                                           fg="blue")
        self.prio_mid_goal_done = Label(okno, text="Prio MID", font=("Arial Bold", 15),
                                        fg="blue")
        self.splitpush_mid_goal_done = Label(okno, text="Splitpush MID", font=("Arial Bold", 15),
                                             fg="blue")
        self.strong2v2_mid_goal_done = Label(okno, text="Strong 2v2 MID", font=("Arial Bold", 15),
                                             fg="blue")
        self.scaling_jng_goal_done = Label(okno, text="Scaling JNG", font=("Arial Bold", 15),
                                           fg="blue")
        self.safe_engage_jng_goal_done = Label(okno, text="Safe JNG with engage", font=("Arial Bold", 15),
                                               fg="blue")
        self.mobility_engage_jng_goal_done = Label(okno, text="JNG with mobility and engage", font=("Arial Bold", 15),
                                                   fg="blue")
        self.early_jng_goal_done = Label(okno, text="Early prio JNG", font=("Arial Bold", 15),
                                         fg="blue")

        # wczytywanie ikon postaci
        self.load = Image.open("ilaoi.png")
        self.render = ImageTk.PhotoImage(self.load)
        self.ilaoi = Label(okno, image=self.render)
        self.ilaoi.image = self.render

        self.load = Image.open("orn.png")
        self.render = ImageTk.PhotoImage(self.load)
        self.orn = Label(okno, image=self.render)
        self.orn.image = self.render

        self.load = Image.open("draven.png")
        self.render = ImageTk.PhotoImage(self.load)
        self.draven = Label(okno, image=self.render)
        self.draven.image = self.render

        self.load = Image.open("ezreal.png")
        self.render = ImageTk.PhotoImage(self.load)
        self.ezreal = Label(okno, image=self.render)
        self.ezreal.image = self.render

        self.load = Image.open("tahm.png")
        self.render = ImageTk.PhotoImage(self.load)
        self.tahm = Label(okno, image=self.render)
        self.tahm.image = self.render

        self.load = Image.open("ekko.png")
        self.render = ImageTk.PhotoImage(self.load)
        self.ekko = Label(okno, image=self.render)
        self.ekko.image = self.render

        self.load = Image.open("sett.png")
        self.render = ImageTk.PhotoImage(self.load)
        self.sett = Label(okno, image=self.render)
        self.sett.image = self.render

        self.load = Image.open("oriana.png")
        self.render = ImageTk.PhotoImage(self.load)
        self.oriana = Label(okno, image=self.render)
        self.oriana.image = self.render

        self.load = Image.open("ryze.png")
        self.render = ImageTk.PhotoImage(self.load)
        self.ryze = Label(okno, image=self.render)
        self.ryze.image = self.render

        self.load = Image.open("graves.png")
        self.render = ImageTk.PhotoImage(self.load)
        self.graves = Label(okno, image=self.render)
        self.graves.image = self.render

        self.load = Image.open("hecarim.png")
        self.render = ImageTk.PhotoImage(self.load)
        self.hecarim = Label(okno, image=self.render)
        self.hecarim.image = self.render

        self.load = Image.open("jarvan.png")
        self.render = ImageTk.PhotoImage(self.load)
        self.jarvan = Label(okno, image=self.render)
        self.jarvan.image = self.render

        self.load = Image.open("zac.png")
        self.render = ImageTk.PhotoImage(self.load)
        self.zac = Label(okno, image=self.render)
        self.zac.image = self.render

        # pierwsze pytanie
        self.pierwsze_pytanie = Label(okno, text="Do we play Illaoi TOP?:", font=("Arial Bold", 20), fg="black")
        self.pierwsze_pytanie.grid(row=0, column=0, columnspan=6, sticky=E + W)

        self.v = IntVar()
        self.rad1 = Radiobutton(okno, text='YES', variable=self.v, value=1, command=self.selectTak,
                                font=("Arial Bold", 20), fg="red")
        self.rad2 = Radiobutton(okno, text='NO', variable=self.v, value=2, command=self.selectNie,
                                font=("Arial Bold", 20), fg="red")
        self.rad1.grid(column=2, row=2, sticky=E + W)
        self.rad2.grid(column=4, row=2, sticky=E + W)

        # po odpowiedzi na pierwsze pytanie
        self.top_label = Label(okno, text="TOP", font=("Arial Bold", 20), fg="black")
        self.jungle_label = Label(okno, text="JUNGLE", font=("Arial Bold", 20), fg="black")
        self.mid_label = Label(okno, text="MID", font=("Arial Bold", 20), fg="black")
        self.adc_label = Label(okno, text="ADC", font=("Arial Bold", 20), fg="black")
        self.supp_label = Label(okno, text="SUPPORT", font=("Arial Bold", 20), fg="black")

        self.pierwsze_polecenie1 = Label(okno,
                                         text="Pick scaling ADC and SUPPORT with priority",
                                         font=("Arial Bold", 20),
                                         fg="black")
        self.przycisk1 = Button(okno, text="DONE", font=("Arial", 15), pady=10, command=self.done1, width=20,
                                bg="red")
        self.pierwsze_polecenie2 = Label(okno,
                                         text="Pick ADC and SUPPORT with priority",
                                         font=("Arial Bold", 20),
                                         fg="black")
        self.przycisk2 = Button(okno, text="DONE", font=("Arial", 15), pady=10, command=self.done2, width=20,
                                bg="red")

        # drugie pytanie
        self.drugie_pytanie1 = Label(okno, text="Do we have priority on MID?:", font=("Arial Bold", 20), fg="black")

        self.v1 = IntVar()
        self.rad3 = Radiobutton(okno, text='YES', variable=self.v1, value=1, command=self.selectTak2,
                                font=("Arial Bold", 20), fg="red")
        self.rad4 = Radiobutton(okno, text='NO', variable=self.v1, value=2, command=self.selectNie2,
                                font=("Arial Bold", 20), fg="red")
        self.rad5 = Radiobutton(okno, text='YES', variable=self.v1, value=3, command=self.selectTak3,
                                font=("Arial Bold", 20), fg="red")
        self.rad6 = Radiobutton(okno, text='NO', variable=self.v1, value=4, command=self.selectNie3,
                                font=("Arial Bold", 20), fg="red")

        # po drugim pytaniu
        self.drugie_polecenie1 = Label(okno, text="Pick JUNGLER:", font=("Arial Bold", 20), fg="black")

        self.v2 = IntVar()
        self.rad7 = Radiobutton(okno, text='EARLY PRIORITY', variable=self.v2, value=1, command=self.selectA,
                                font=("Arial Bold", 20), fg="red")
        self.rad8 = Radiobutton(okno, text='MOBILITY AND ENGAGE', variable=self.v2, value=2, command=self.selectB,
                                font=("Arial Bold", 20), fg="red")
        self.rad9 = Radiobutton(okno, text='SCALING', variable=self.v2, value=3, command=self.selectC,
                                font=("Arial Bold", 20), fg="red")
        self.rad10 = Radiobutton(okno, text='SAFE AND ENGAGE', variable=self.v2, value=4, command=self.selectD,
                                 font=("Arial Bold", 20), fg="red")

        # zakonczenie
        self.zakonczenie = Label(okno, text="Get luck & have fun!", font=("Arial Bold", 20), fg="black")

    def selectTak(self):
        self.pierwsze_pytanie.destroy()
        self.rad1.destroy()
        self.rad2.destroy()

        self.top_label.grid(row=2, column=1, sticky=E + W)
        self.jungle_label.grid(row=2, column=2, sticky=E + W)
        self.mid_label.grid(row=2, column=3, sticky=E + W)
        self.adc_label.grid(row=2, column=4, sticky=E + W)
        self.supp_label.grid(row=2, column=5, sticky=E + W)

        self.cele_kompozycji.grid(row=3, column=0, sticky=E + W)
        self.scaling_bot_goal.grid(row=4, column=0, sticky=E + W)
        self.prio_mid_goal.grid(row=5, column=0, sticky=E + W)
        self.splitpush_mid_goal.grid(row=6, column=0, sticky=E + W)
        self.mobility_engage_jng_goal.grid(row=7, column=0, sticky=E + W)
        self.early_jng_goal.grid(row=8, column=0, sticky=E + W)
        self.safe_engage_jng_goal.grid(row=9, column=0, sticky=E + W)

        self.ilaoi.grid(row=3, column=1, rowspan=7, sticky=E + W)

        self.pierwsze_polecenie1.grid(row=0, column=1, columnspan=5, sticky=E + W)

        self.przycisk1.grid(column=3, row=1, sticky=E + W)

    def selectNie(self):
        self.pierwsze_pytanie.destroy()
        self.rad1.destroy()
        self.rad2.destroy()

        self.top_label.grid(row=2, column=1, sticky=E + W)
        self.jungle_label.grid(row=2, column=2, sticky=E + W)
        self.mid_label.grid(row=2, column=3, sticky=E + W)
        self.adc_label.grid(row=2, column=4, sticky=E + W)
        self.supp_label.grid(row=2, column=5, sticky=E + W)

        self.cele_kompozycji.grid(row=3, column=0, sticky=E + W)
        self.prio_bot_goal.grid(row=4, column=0, sticky=E + W)
        self.prio_mid_goal.grid(row=5, column=0, sticky=E + W)
        self.scaling_mid_goal.grid(row=6, column=0, sticky=E + W)
        self.strong2v2_mid_goal.grid(row=7, column=0, sticky=E + W)
        self.early_jng_goal.grid(row=8, column=0, sticky=E + W)
        self.scaling_jng_goal.grid(row=9, column=0, sticky=E + W)

        self.orn.grid(row=3, column=1, rowspan=7, sticky=E + W)

        self.pierwsze_polecenie2.grid(row=0, column=1, columnspan=5, sticky=E + W)

        self.przycisk2.grid(column=3, row=1, sticky=E + W)

    def done1(self):
        self.pierwsze_polecenie1.destroy()
        self.przycisk1.destroy()
        self.scaling_bot_goal.destroy()

        self.scaling_bot_goal_done.grid(row=4, column=0, sticky=E + W)

        self.ezreal.grid(row=3, column=4, rowspan=7, sticky=E + W)
        self.tahm.grid(row=3, column=5, rowspan=7, sticky=E + W)

        self.drugie_pytanie1.grid(row=0, column=0, columnspan=6, sticky=E + W)
        self.rad3.grid(column=2, row=1, sticky=E + W)
        self.rad4.grid(column=4, row=1, sticky=E + W)

    def done2(self):
        self.pierwsze_polecenie2.destroy()
        self.przycisk2.destroy()
        self.prio_bot_goal.destroy()

        self.prio_bot_goal_done.grid(row=4, column=0, sticky=E + W)

        self.draven.grid(row=3, column=4, rowspan=7, sticky=E + W)
        self.tahm.grid(row=3, column=5, rowspan=7, sticky=E + W)

        self.drugie_pytanie1.grid(row=0, column=0, columnspan=6, sticky=E + W)
        self.rad5.grid(column=2, row=1, sticky=E + W)
        self.rad6.grid(column=4, row=1, sticky=E + W)

    def selectTak2(self):
        self.drugie_pytanie1.destroy()
        self.rad3.destroy()
        self.rad4.destroy()
        self.prio_mid_goal.destroy()

        self.prio_mid_goal_done.grid(row=5, column=0, sticky=E + W)

        self.oriana.grid(row=3, column=3, rowspan=7, sticky=E + W)

        self.drugie_polecenie1.grid(row=0, column=1, columnspan=5, sticky=E + W)
        self.rad7.grid(column=2, row=1, sticky=E + W)
        self.rad8.grid(column=4, row=1, sticky=E + W)

    def selectNie2(self):
        self.drugie_pytanie1.destroy()
        self.rad3.destroy()
        self.rad4.destroy()
        self.splitpush_mid_goal.destroy()

        self.splitpush_mid_goal_done.grid(row=6, column=0, sticky=E + W)

        self.ekko.grid(row=3, column=3, rowspan=7, sticky=E + W)

        self.drugie_polecenie1.grid(row=0, column=1, columnspan=5, sticky=E + W)
        self.rad8.grid(column=2, row=1, sticky=E + W)
        self.rad10.grid(column=4, row=1, sticky=E + W)

    def selectTak3(self):
        self.drugie_pytanie1.destroy()
        self.rad5.destroy()
        self.rad6.destroy()
        self.prio_mid_goal.destroy()

        self.prio_mid_goal_done.grid(row=5, column=0, sticky=E + W)

        self.oriana.grid(row=3, column=3, rowspan=7, sticky=E + W)

        self.drugie_polecenie1.grid(row=0, column=1, columnspan=5, sticky=E + W)
        self.rad9.grid(column=3, row=1, sticky=E + W)

    def selectNie3(self):
        self.drugie_pytanie1.destroy()
        self.rad5.destroy()
        self.rad6.destroy()
        self.scaling_mid_goal.destroy()

        self.scaling_mid_goal_done.grid(row=6, column=0, sticky=E + W)

        self.ryze.grid(row=3, column=3, rowspan=7, sticky=E + W)

        self.drugie_polecenie1.grid(row=0, column=1, columnspan=5, sticky=E + W)
        self.rad7.grid(column=3, row=1, sticky=E + W)

    def selectA(self):
        self.drugie_polecenie1.destroy()
        self.rad7.destroy()
        self.rad8.destroy()
        self.rad9.destroy()
        self.rad10.destroy()
        self.early_jng_goal.destroy()

        self.early_jng_goal_done.grid(row=8, column=0, sticky=E + W)

        self.jarvan.grid(row=3, column=2, rowspan=7, sticky=E + W)

        self.zakonczenie.grid(row=0, column=1, columnspan=5, sticky=E + W)

    def selectB(self):
        self.drugie_polecenie1.destroy()
        self.rad7.destroy()
        self.rad8.destroy()
        self.rad9.destroy()
        self.rad10.destroy()
        self.mobility_engage_jng_goal.destroy()

        self.mobility_engage_jng_goal_done.grid(row=7, column=0, sticky=E + W)

        self.hecarim.grid(row=3, column=2, rowspan=7, sticky=E + W)

        self.zakonczenie.grid(row=0, column=1, columnspan=5, sticky=E + W)

    def selectC(self):
        self.drugie_polecenie1.destroy()
        self.rad7.destroy()
        self.rad8.destroy()
        self.rad9.destroy()
        self.rad10.destroy()
        self.scaling_jng_goal.destroy()

        self.scaling_jng_goal_done.grid(row=9, column=0, sticky=E + W)

        self.graves.grid(row=3, column=2, rowspan=7, sticky=E + W)

        self.zakonczenie.grid(row=0, column=1, columnspan=5, sticky=E + W)

    def selectD(self):
        self.drugie_polecenie1.destroy()
        self.rad7.destroy()
        self.rad8.destroy()
        self.rad9.destroy()
        self.rad10.destroy()
        self.safe_engage_jng_goal.destroy()

        self.safe_engage_jng_goal_done.grid(row=9, column=0, sticky=E + W)

        self.zac.grid(row=3, column=2, rowspan=7, sticky=E + W)

        self.zakonczenie.grid(row=0, column=1, columnspan=5, sticky=E + W)


if __name__ == "__main__":
    # okno i podzial kolumn i wierszy
    okno = Tk()
    okno.title("Draft app v1")
    okno.geometry('1400x600')

    # okno.grid_columnconfigure(0, weight=1)
    okno.grid_columnconfigure(1, weight=1)
    okno.grid_columnconfigure(2, weight=1)
    okno.grid_columnconfigure(3, weight=1)
    okno.grid_columnconfigure(4, weight=1)
    okno.grid_columnconfigure(5, weight=1)
    MainScreen(okno)

    # glowna petla
    okno.mainloop()
