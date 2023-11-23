from tkinter import*
import random
root=Tk()
root.title("Password Generator")
root.geometry("400x400")

label_show=Label(root)

input_1=Entry(root,text="Guessed Password")
input_1.pack()


label=Label(root)


array_3d=[[['A','B','C','D','E','F','G','H'],
           ["King","Queen"],
           ["&","#","@","!"]]]

def Guessed():
    input_2=input_1.get()
    label["text"] = "Guessed Password: " + input_2
    
    
button=Button(root,text="Show Guessed Password",command=Guessed)
button.pack()
label.pack()

def random_number():
    rand_1=random.randint(0,7)
    rand_2=random.randint(0,1)
    rand_3=random.randint(0,3)
    
    letter_1=array_3d[0][0][rand_1]
    letter_2=array_3d[0][1][rand_2]
    letter_3=array_3d[0][2][rand_3]
    
    label_show["text"] = letter_1 + letter_2 + letter_3
    
btn_1=Button(root,text="Generate Password",command=random_number)
btn_1.place(relx="0.5",rely="0.5",anchor=CENTER)

label_show.place(relx="0.5",rely="0.6",anchor=CENTER)

root.mainloop()