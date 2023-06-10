import tkinter as tk
"""
    Goal :
        Have a functionnal typing practice application

    Images Sources:
        keyboard icon : Free Keyboard Classic Icon by Parul Gupta
"""

def main():
    global palette
    palette = ["#E9EDC9","#ccd5ae","#FEFAE0"]

    window = tk.Tk()
    window.geometry("800x450+{}+{}".format(int(window.winfo_screenwidth()/2 - 400), int(window.winfo_screenheight()/2 - 225)))
    window.title('Typing Practice')
    window.iconbitmap('Images/keyboard.ico')
    window.resizable(False,False)
    window.bind('<Escape>',lambda e: window.destroy())
    window.configure(bg=palette[1])

    page1(window)
    window.mainloop()

def page1(frame):
    global palette
    
    frameTitre = tk.Frame(frame,bg=palette[2])
    frameTitre.place(rely=0.08, relx=0.1, relheight= 0.1 , relwidth=0.8)
    
    frameBas = tk.Frame(frame , bg=palette[0])
    frameBas.place(rely=0.2,relx=0.1,relheight=0.72,relwidth=0.8)

    labelTitre = tk.Label(frameTitre, text="𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐭𝐨 𝐭𝐲𝐩𝐢𝐧𝐠 𝐩𝐫𝐚𝐜𝐭𝐢𝐜𝐞",font=("actual",15), bg= palette[2])
    labelTitre.place(rely=0.10,relx=0.37)

def page2(frame):
    print("page3")


if __name__ == "__main__":
    main()


