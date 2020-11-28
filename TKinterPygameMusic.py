from tkinter import  *
import pygame

pygame.init()
root= Tk()
root.title("Music Player")
root.geometry("512x512")
root.minsize(200,200)


# frame 1
f1=Frame(root,borderwidth=3,bg="black",relief=SUNKEN)
f1.pack(side=LEFT,fill=Y)

# frame2
f2=Frame(root,bg="black",relief=SUNKEN)
f2.pack(side=TOP,fill=X)

#
# # adding background
img=PhotoImage(file="music2.png")
photo=Label(root,image=img)
photo.pack()


# # frame 3 (play)
# f3=Frame(root,bg="black",relief=SUNKEN)
# f3.pack(side=LEFT,anchor="nw",pady=50,padx=8)
#
# # frame 4 (pause)
# f4=Frame(root,bg="black")
# f4.pack(side=RIGHT,anchor="nw",pady=50,padx=5)
#
# # Frame 5 (stop)
# f5=Frame(root,bg="black")
# f5.pack(anchor="nw",padx=130,pady=50)


# lable1
l1=Label(f1,text="Dopekid",bg="black",fg="white",font="airstrike 16 ")
l1.pack()

# lable 2
l2=Label(f2,text="Groove Music",font="airstrike 28",bg="black",fg="white")
l2.pack()

# loading music and playing
def music():
    pygame.mixer.music.load("C:\\Users\\Dopekid\\Music\\test.mp3")
    pygame.mixer.music.play()
# pausing the music
def pause():
    pygame.mixer.music.load("C:\\Users\\Dopekid\\Music\\test.mp3")
    pygame.mixer.music.pause()
def resume():
    pygame.mixer.music.load("C:\\Users\\Dopekid\\Music\\test.mp3")
    pygame.mixer.music.unpause()


#  Button 1| Play

b1=Button(photo,text="Play",font="dream 10 italic",bg="black",fg="white",command=music)
b1.pack(side=LEFT,anchor="nw",pady=50,padx=8)

# button 2 | pause
b2=Button(photo,text="Pause",bg="black",fg="white",font="dream 10 italic",command=pause)
b2.pack(side=RIGHT,anchor="nw",pady=50,padx=5)

# Button 3 | stop
b3=Button(photo,text="Stop",bg="black",fg='white',font="dream 10 italic",command=resume)
b3.pack(anchor="nw",padx=130,pady=50)


# adding rest image
img2=PhotoImage(file='music2.png')
photo1=Label(root,image=img2)
photo1.pack()




root.mainloop()
