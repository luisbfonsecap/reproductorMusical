#se importan las librerias
import tkinter as tk
import pygame as pg
import os

#se define el container
container = tk.Tk()

# se define la clase reproductor musical
class ReproductorMusical:
    
    def __init__(self, container):
            self.container=container
            self.container.title('Reproductor de Música')
            self.container.geometry('300x600')
            self.container.configure(background= 'black')
#Se define la variable self.canción con Stringvar para luego usar set y asignar la canción selecionada            
            self.cancion=tk.StringVar()
#Se define la variable self.estado con Stringvar para saber si la canción selecionada está pausada o en reproducción 
            self.estado = tk.StringVar()
            self.estado.set("Detenido")

            self.canciones = os.listdir('canciones/')
            
#se crean los cuadros que van a contener los botones, el nombre de la canción y la lista de canciones

            cuadro1 = tk.Frame(self.container)
            cuadro1.pack(pady=10)
            framefinal1 = tk.Frame(cuadro1)
            framefinal1.pack(pady=2, padx=2)

            cuadro2 = tk.Frame(self.container)
            cuadro2.pack(pady=10)
            framefinal2 = tk.Frame(cuadro2)
            framefinal2.pack(pady=2, padx=2)

            cuadro3 = tk.Frame(self.container)
            cuadro3.pack(pady=10)
            framefinal3 = tk.Frame(cuadro3)
            framefinal3.pack(pady=2, padx=2)

            cuadro4 = tk.Frame(self.container)
            cuadro4.pack(pady=10)
            framefinal4 = tk.Frame(cuadro4)
            framefinal4.pack(pady=2, padx=2)

            #cuadro5 = tk.Frame(self.container) SI HAY MAS TIEMPO TRATO DE SACARLO
            #cuadro5.pack(pady=10)
            #framefinal5 = tk.Frame(cuadro5)
            #framefinal5.pack(pady=2, padx=2)

#se crea el scroll bar para poder moverse por las canciones
            framefinal6 = tk.Label(self.container, textvariable = self.cancion, width=180)
            framefinal6.pack(pady=20, padx=5)

            songsFrame= tk.LabelFrame(self.container,height="256", width="200")
            songsFrame.pack(padx="10")
#se inicializa el mixer de pygame
            pg.mixer.init()

#se definen las funciones que van a controlar los botones de comando y adicionalmente en la función play se crea el label que muestra el nombre de la canción que se está ejecutando y se asigna el estado de la canción
            def Play():
                if self.estado.get() == "Pausado":
                    pg.mixer.music.unpause()
                else:
                    self.cancion.set("canciones/" + self.listaCanciones.get(self.listaCanciones.curselection()))
                    pg.mixer.music.load(self.cancion.get())
                    pg.mixer.music.play()
                self.estado.set("Reproduciendo")
                self.cancion.set(self.listaCanciones.get(self.listaCanciones.curselection()))

            def Anterior():
                pg.mixer.music.rewind()
                self.estado.set("Detenido")

            def Stop():
                pg.mixer.music.stop()
                self.estado.set("Detenido")
                
            def Pausa():
                pg.mixer.music.pause()
                self.estado.set("Pausado")

#se asignas los botones a los cuadros que los van a contener

            self.imagenPlay = tk.PhotoImage(file='play2.png')
            boton1 = tk.Button(framefinal1, image=self.imagenPlay, command=Play)
            boton1.grid(row=1,column=1,padx=1, pady=1)

            self.imagenAnterior = tk.PhotoImage(file='anterior2.png')
            boton2 = tk.Button(framefinal2, image=self.imagenAnterior, command=Anterior)
            boton2.grid(row=1,column=1,padx=1, pady=1)

            self.imagenStop = tk.PhotoImage(file='stop2.png')
            boton3 = tk.Button(framefinal3, image=self.imagenStop, command=Stop)
            boton3.grid(row=1,column=1,padx=1, pady=1)

            self.imagenPausa = tk.PhotoImage(file='pausa2.png')
            boton4 = tk.Button(framefinal4, image=self.imagenPausa, command=Pausa)
            boton4.grid(row=1,column=1,padx=1, pady=1)

            #self.imagenSiguiente = tk.PhotoImage(file='next2.png')  SI HAY MAS TIEMPO TRATO DE SACARLO
            #boton5 = tk.Button(framefinal5, image=self.imagenSiguiente, command=Siguiente)
            #boton5.grid(row=1,column=1,padx=1, pady=1)

#se hace la barra de desplazamiento vertical para las canciones

            scrollbar = tk.Scrollbar(songsFrame)
            scrollbar.pack(side = "right", fill = "both") 

            self.listaCanciones = tk.Listbox(songsFrame,yscrollcommand=scrollbar,selectmode="SINGLE")
            self.listaCanciones.insert(0,*self.canciones)
            self.listaCanciones.pack()
            self.listaCanciones.config(yscrollcommand = scrollbar.set) 
            scrollbar.config(command = self.listaCanciones.yview) 

#se crea un objeto que sea el reproductor
reproductor1 = ReproductorMusical(container)
        
#se crea la ventana para que funcione el reproductor
reproductor1.container.mainloop()

