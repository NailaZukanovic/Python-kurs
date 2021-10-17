from tkinter import *
from yt_to_mp3_func import download_mp3,open_downloads, delete_txtbox

#prozor
root = Tk()
root.title('Youtube to mp3 converter')

root.geometry('400x300')

#Natpis iznad unosa
Label(text = 'Unesite link koji zelite', font=('Arial',14)).pack(pady=10)

unosKorisnika = Entry(root, width = 30)
unosKorisnika.pack(pady = 20)


ok_error = Label(root,text='', font=('Arial',14))

ok_error.pack(pady=15)

#fali jos command
btn = Button(root, text='Download MP3', font=('Arial',14), command = lambda : [download_mp3(unosKorisnika.get(),ok_error),delete_txtbox(unosKorisnika)])

btn.pack(pady = 10)

btnDld = Button(root,text='Open Downloads',font=('Arial',14), command = open_downloads)

btnDld.pack(side=BOTTOM)

#Pokretac gui-a
root.mainloop()
