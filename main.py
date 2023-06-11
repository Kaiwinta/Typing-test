import tkinter as tk
import generator
"""
    Goal :
        Have a functionnal typing practice application

    Images Sources:
        keyboard icon : Free Keyboard Classic Icon by Parul Gupta
"""

def main():
    global palette
    palette = ["#E9EDC9","#ccd5ae","#FEFAE0","#3B7080","#3A5743"]

    window = tk.Tk()
    window.geometry("800x450+{}+{}".format(int(window.winfo_screenwidth()/2 - 400), int(window.winfo_screenheight()/2 - 225)))
    window.title('Typing Practice')
    window.iconbitmap('Images/keyboard.ico')
    window.resizable(False,False)
    window.bind('<Escape>',lambda e: window.destroy())
    window.configure(bg=palette[4])

    page1(window)
    window.mainloop()

def page1(frame):
    global palette
    imagebutton=tk.PhotoImage(file='Images/button2.png', master=frame)
    imagedino = tk.PhotoImage(file='Images/dinosaur.png')
    imagepalmier =tk.PhotoImage(file = 'Images/fresepalmier.png')
    
    imagesouligne = tk.PhotoImage(file= 'Images/underline4.png')

    frameTitre = tk.Frame(frame,bg=palette[2])
    frameTitre.place(rely=0.08, relx=0.1, relheight= 0.1 , relwidth=0.8)
    
    frameBas = tk.Frame(frame , bg=palette[0])
    frameBas.place(rely=0.2,relx=0.1,relheight=0.72,relwidth=0.8)

    labelTitre = tk.Label(frameTitre, text="𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐭𝐨 𝐭𝐲𝐩𝐢𝐧𝐠 𝐩𝐫𝐚𝐜𝐭𝐢𝐜𝐞",font=("actual",14), bg= palette[2])
    labelTitre.place(rely=0.10,relx=0.33)

    labelImageUnterline = tk.Label(frameTitre,image=imagesouligne,bg = palette[2])
    labelImageUnterline.place(rely = 0.7 , relx=0.387)

    def gotopage2():
        delete(frameBas)
        page2(frameBas)

    labelImagedino = tk.Label(frameBas,image=imagedino, bg=palette[0])
    labelImagedino.place(relx=-0.05, rely=0.33)

    labelImagepalmier = tk.Label(frameBas,image=imagepalmier, bg=palette[0])
    labelImagepalmier.place(relx=0.35, rely=0.65)

    labelDesciption = tk.Label(frameBas,bg = palette[1])
    labelDesciption.place(relheight=0.4,relwidth=0.4,relx=0.3,rely=0.1)

    buttonPage2 = tk.Button(frameBas, command=gotopage2,image=imagebutton,bg = palette[0])
    buttonPage2.place(rely=0.6,relx=0.4)

    frame.mainloop()

def page2(frame):
    global palette
    def generate():
        """
            Objectif:   faire appel la la fonciton generer
                        bloquer toute tentative qui pourrais ne pas marcher
        """
        if type(entreeLettre.get()) != str or len(entreeLettre.get())<=0:
            labelText.config(bg='red',text="Merci de mettre des lettres dans 'Lettre du test'")
        else:
            try :
                length = entreeLength.get()
                int(length)

                try :
                    nombre = entreeLength.get()
                    int(nombre)
                    if int(length)>=3 and int(nombre) >=2:
                        text = generator.generate_text(entreeLettre.get(),int(entreeLength.get()),int(entreeNombre.get()))
                        labelText.config(bg = palette[3],text=text)
                    else :
                        labelText.config(bg='red',text="Le nombre de mots doit être >= 2 et la taille >=3")

                except ValueError:
                    labelText.config(bg='red',text="Merci de rentrer un Nombre de mots")
                
            except ValueError:
                labelText.config(bg='red',text="Merci de rentrer une taille maximale")

    frameParametre = tk.Frame(frame, bg= palette[1])
    frameParametre.place(relx=0, rely=0 , relheight=0.25 , relwidth=1)

    labelLettre = tk.Label(frameParametre, text = "Lettres du test")
    labelLength = tk.Label(frameParametre, text = "Taille max des mots")
    labelNombre = tk.Label(frameParametre, text = "Nombre de mots")
    entreeLettre = tk.Entry(frameParametre)
    entreeLength = tk.Entry(frameParametre)
    entreeNombre = tk.Entry(frameParametre)

    entreeLettre.place(relwidth=0.25 , relheight=0.23 , relx=0.05, rely=0.4)
    entreeLength.place(relwidth=0.25 , relheight=0.23 , relx=0.375, rely=0.4)
    entreeNombre.place(relwidth=0.25 , relheight=0.23 , relx=0.7, rely=0.4)
    labelLettre.place(relwidth=0.25 , relheight=0.23 , relx=0.05, rely=0.17)
    labelLength.place(relwidth=0.25 , relheight=0.23 , relx=0.375, rely=0.17)
    labelNombre.place(relwidth=0.25 , relheight=0.23 , relx=0.7, rely=0.17)

    buttonGenerate = tk.Button(frameParametre,command =generate , text="Start test" )
    buttonGenerate.place(relheight=0.2,relwidth=0.15 , relx=0.425,rely=0.75)

    labelText = tk.Label(frame, text= "")
    labelText.pack(side='bottom')

def delete(frame):
    for widget in frame.winfo_children():
        widget.destroy() 

if __name__ == "__main__":
    main()


