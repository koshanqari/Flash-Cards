import builtins
from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
# BACKGROUND_COLOR = "#f0f1f1"
from PIL import Image, ImageTk

#setting up the main window
root = Tk()
root.geometry("500x500")
root.config(bg=BACKGROUND_COLOR)
root.title("K.Qari's Words Memorizer")


#all the funcions go in here ------------------------------------------
#flippig the card fxn

# GLOBAL VARIABLES----------------
num = 1 #odd --> back
        #even -> front
random_index_v = 0
#---------------------------------
def card_flip():
    print(list1)
    print("card flip fxn")
    global num
    num+=1
    print(num)
    
    right_wrong()
    if num%2 == 0:
        card_image_l.config(image = img_front)
        card_text_l.config(text = df.at[random_index_v, "Meanings"], bg="#fefffe")
        show_next_b.place_forget()

    else:
        random_index()
        card_image_l.config(image = img_back)
        card_text_l.config(text = df.at[random_index_v, "Word"], bg="#90c2ae")
        show_next_b.place(x=220, y=400)

def random_index():
    print("random word index generated")
    if len(list1) <= 0:
        Label(text="Congratulations you have memorised all the words").place(x=110, y=200)
        show_next_b.place_forget()
    else:
        global random_index_v
        random_index_v = random.choice(list1)
        return



def right():
    global list1
    print("right fxn")
    card_flip()
    print(random_index_v)
    if len(list1) > 0:
        list1.remove(random_index_v)
    print(list1)
    

def wrong():
    print("wrong fxn")
    card_flip()


def right_wrong():
    print("right worng fxn")
    global num
    if num%2 == 0:
        
        right_b.place(x=350, y=400)
        wrong_b.place(x=100, y=400)
        show_next_b.pack_forget()
    else:
        right_b.place_forget()
        wrong_b.place_forget()

#game logic------------------------------------------------------------
try:
    df = pandas.read_csv("data/words.csv")
except FileNotFoundError: 
    dict ={
        "Word":["Add words to \n data\words.csv file"],
        "Meanings":["Add words to \n data\words.csv file"]
    }
    df2 = pandas.DataFrame(dict)
    df2.to_csv("data/words.csv", index=False)
else:
    list1 = [i for i in range(len(df["Word"]))]







# GUI--------------------------------------------------------------
# Reading the Images
image = Image.open("images\card_front.png")
resize_image = image.resize((300, 200))
img_front = ImageTk.PhotoImage(resize_image) #variable: img_fromt 
image = Image.open("images\card_back.png")
resize_image = image.resize((300, 200))
img_back = ImageTk.PhotoImage(resize_image) #variable: img_back


card_image_l = Label(image=img_back, bg=BACKGROUND_COLOR)
card_image_l.place(x=100, y=100)



#label on cards
random_index()
card_text_l = Label(text=df.at[random_index_v, "Word"], font=("sans", 13, "bold"), bg="#90c2ae")
card_text_l.place(x=220, y=200)



#buttons
show_next_b = Button(text="Card Flip", command=card_flip)
show_next_b.place(x=220, y=400)

right_b = Button(text=" Right ", command=right)
wrong_b = Button(text="Wrong", command=wrong)
#----------------------------------------------------------------------




#keep this in the end
root.mainloop()

