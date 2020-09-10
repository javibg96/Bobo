import tkinter as tk

from tkinter import *
from tkinter import ttk
import os


class Interfaz:

    def __init__(self):
        self.root = tk.Tk()  # como el main de HTML
        self.apps = []
        if os.path.isfile("aplicaciones_guardadas.txt"):
            with open("aplicaciones_guardadas.txt", "r") as f:
                tempApps = f.read()
                tempApps = tempApps.split("\n")
                self.apps = tempApps
                del self.apps[-1]
        jarvis = False
        self.frame = tk.Frame(self.root, bg="#263D42")
        self.frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

        self.mainframe = ttk.Frame(self.root, padding="10 10 12 12")
        self.mainframe.pack()
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)
        if jarvis:
            self.jarvis()

    def print_contents(self, event):
        event = self.contents.get()
        return event

    def addApp(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        filename = filedialog.askopenfile(initialdir="/", title="elige archivo",
                                          filetypes=(("executables", "*.exe"), ("all files", "*.*")))
        self.apps.append(filename)
        for app in self.apps:
            label = tk.Label(self.frame, text=app, bg="gray")
            label.pack()

    def runApps(self):
        for app in self.apps:
            os.startfile(app)

    def text_input(self):

        variable1 = StringVar()  # Value saved here

        def search():
            print(variable1.get())
            return ''

        ttk.Entry(self.mainframe, width=7, textvariable=variable1).grid(column=2, row=1)

        ttk.Label(self.mainframe, text="comando").grid(column=1, row=1)

        ttk.Button(self.mainframe, text="enviar", command=search).grid(column=2, row=13)

        return search()

    def main_interf(self):

        self.root.title('BOBO')

        openFile = tk.Button(self.root, text="Abrir archivo", padx=10, pady=5, fg="white",
                             bg="#263D42", command=self.addApp)
        openFile.pack(side="right")

        runApp = tk.Button(self.root, text="Iniciar App", padx=10, pady=5, fg="white",
                           bg="#263D42", command=self.runApps)
        runApp.pack(side="left")

        for app in self.apps:
            label = tk.Label(self.frame, text=app, bg="gray")
            label.pack()
        # and here we get a callback when the user hits return.
        # we will have the program print out the value of the
        # application variable when the user hits return
        texto = self.text_input()
        print(texto)
        # print(inputVal)
        self.root.mainloop()

        with open("aplicaciones_guardadas.txt", "w") as f:
            for app in self.apps:
                if type(app) is str:
                    f.write(app + '\n')
                else:
                    f.write(app.name + '\n')

    def jarvis(self):
        frames = [PhotoImage(file='gif-jarvis.gif', format='gif -index %i' % i) for i in range(20)]

        def update(ind):
            frame = frames[ind]
            ind += 1
            print(ind)
            if ind > 19:  # With this condition it will play gif infinitely
                ind = 0
            label2.configure(image=frame)
            self.root.after(90, update, ind)

        label2 = Label(self.root, bg='black')
        label2.pack(side="top")
        self.root.after(0, update, 0)


if __name__ == "__main__":
    Interfaz().main_interf()
