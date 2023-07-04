#Creating Telegram Bot

#.......... STEP 1 ..........

# Importing Necessary modules
from telethon import TelegramClient, events, sync
from tkinter import *
from tkinter import messagebox

#.......... STEP 3 ..........

#sender function
def send_message():
    #API details
    user_details = user_entry.get()
    message_content = message_entry.get("1.0","end-1c")

    #Raise a warning if no input is given
    if (len(user_details) <=0) & (len(message_content) <=1):
        messagebox.showerror(message="ENTER USER DETAILS")
    else:
        #Note: Enter your personal api_id & api_hash, watch @youtube video to know telegram api_id, api_hash
        api_id = 26929915
        api_hash = 'eb1627567862f31bda7cf892ef629651'

        #Initialise telegram client with API codes
        client = TelegramClient('My account', '26929915', 'eb1627567862f31bda7cf892ef629651')

        #start the process
        client.start()

        #send the message
        client.send_message(user_details, message_content)
        messagebox.showinfo(message="MESSAGE SENT...")




#........... STEP 2 ...........

#Define the user interface
telegram_mess = Tk()
telegram_mess.title("Telegram Message Sender")
telegram_mess.geometry("400x300")

bg_img = PhotoImage(file="image.png")

#show image using label
label1 = Label(telegram_mess, image= bg_img, bd=0)
label1.pack()

#Application Title in the window
title_label = Label(telegram_mess, text="Telegram Message Sender", bg="white")
title_label.place(x=80,y=10)

#input from user entry
user_label = Label(telegram_mess, text="Enter User Details:", bg="#2591D9")
info_label = Label(telegram_mess, text="Note; Phone Number with code or username with @",bg="#2C99DC")
user_label.place(x=0,y=40)
info_label.place(x=0,y=70)
user_entry = Entry(telegram_mess, width=20)
user_entry.place(x=160,y=40)

#message input
message_label = Label(telegram_mess, text="Enter Message:", bg="#35A1DF")
message_label.place(x=0,y=100)
message_entry = Text(telegram_mess, width=30, height=3)
message_entry.place(x=130,y=99)

#send button
send_button = Button(telegram_mess, text="Send", command=send_message, relief=RAISED)
send_button.place(relx=0.5, rely=0.60,anchor=CENTER)

telegram_mess.mainloop()
