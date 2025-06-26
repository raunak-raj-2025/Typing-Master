# Importing useful things
import tkinter as tk
import random
from tkinter import messagebox as tmsg
import time

# Making commands of the buttons

#Making command of exit button
def exit():
    root.destroy()
    
# Making some variables
font_size = 15
sentence_goal = 5
theme_colour = "#f0f8ff"
text_area_colour = "light grey"
button_colour = "grey"

# Making command of start test button
def start():    
    global font_size, sentence_goal, theme_colour, text_area_colour
# Making test window
    test = tk.Toplevel()
    test.title("Typing master")
    test.geometry("690x1480")
    test.config(bg=theme_colour)
    test.grab_set()
    
# Creating a label to show Typing speed test
    tk.Label(test, text="Typing Speed Test", font="comicsansms 20", bg=theme_colour).pack(pady=10)
    
# A label that shows Timer
    label = tk.Label(test, text="00:00:00", font="comicsansms 20", bg=theme_colour)
    label.pack(pady=50)
    
    start_time = time.time()
    def update():
        elapsed = int(time.time() - start_time)
        hours = elapsed // 3600
        minutes = (elapsed % 3600) // 60
        seconds = elapsed % 60
        label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")
        test.after(1000, update)
    update()
    
# Creating variable
    labelvar = tk.StringVar()
    
# Creating a label to show sentences
    slabel = tk.Label(test, textvariable=labelvar, font="comicsansms 15", wraplength=660, justify="left", bg=theme_colour)
    slabel.pack()
    
# Taking all sentences in a list
    sentences = [
    "The sun was setting behind the mountains.",
    "She opened the book and started reading.",
    "He always drinks coffee in the morning.",
    "The cat jumped onto the windowsill.",
    "They went for a walk in the park.",
    "I forgot to bring my umbrella today.",
    "We are planning a trip to the beach.",
    "The dog barked loudly at the stranger.",
    "He solved the puzzle in no time.",
    "She baked a chocolate cake yesterday.",
    "The train arrived five minutes late.",
    "He was watching a documentary on space.",
    "The kids were playing in the backyard.",
    "I received your message this afternoon.",
    "We need to buy more milk and bread.",
    "She sings beautifully and plays guitar.",
    "The car wouldn’t start this morning.",
    "He tripped over the loose rug.",
    "The teacher gave us a surprise quiz.",
    "I need to charge my phone soon.",
    "We watched the stars until midnight.",
    "He forgot to turn off the stove.",
    "The museum was closed for renovation.",
    "She ran as fast as she could.",
    "They painted the walls light blue.",
    "I heard a strange noise outside.",
    "He built a treehouse for his kids.",
    "The library is open until 8 PM.",
    "She likes to paint landscapes in oils.",
    "The wind knocked over the flower pot.",
    "I have an appointment with the dentist.",
    "They enjoyed the concert last night.",
    "He always keeps his desk tidy.",
    "The cookies smell absolutely delicious.",
    "She dreams of becoming a scientist.",
    "The water in the lake was freezing.",
    "He picked up the phone and called her.",
    "They discovered a hidden cave behind the waterfall.",
    "I’m learning to play the piano.",
    "The fire alarm went off suddenly.",
    "We planted a tree in our backyard.",
    "She took a deep breath and smiled.",
    "The balloon floated up into the sky.",
    "He dropped his keys under the couch.",
    "The baby slept peacefully through the night.",
    "We waited in line for two hours.",
    "He bought a new pair of sneakers.",
    "The chef prepared a five-course meal.",
    "She wrote a poem about the rain.",
    "The light flickered during the storm."
]
    
# adding a sentence to the slabel
    current_sentence = random.choice(sentences)
    labelvar.set(current_sentence)
    
# Text area in which user writes sentence
    text_area = tk.Text(test, font=f"comicsansms {font_size}")
    text_area.config(bg=text_area_colour)
    
# Command of next button which change the sentence
    correct_count = 0
    total_words = 0
    def next():
        nonlocal current_sentence, correct_count, total_words# To modify the variable from outer scope
        
        if current_sentence == text_area.get(1.0, "end").strip():
                     
             correct_count += 1
             total_words += len(current_sentence.split())
             
             if correct_count == sentence_goal:
                 submit()
                 return
                     
             current_sentence = random.choice(sentences)
             labelvar.set(current_sentence)
             text_area.delete(1.0, "end")
            
        else:
            value = tmsg.showinfo("Try again!", "Your typing does not\nmatch the sentence.\nPlease try again!")
            test.lift()
            test.focus_force()
            
# command for the submit button which submits the test and shows typing speed in wpm
    def submit():
        nonlocal total_words
        if total_words == 0:
            tmsg.showinfo("Nothing found", "Please type something\nto get your typing speed")
            test.lift()
            test.focus_force()
        else:
            elapsed_time = time.time() - start_time
            wpm = round((total_words / elapsed_time) * 60)
            tmsg.showinfo("Typing Speed", f"Test completed!\nYour typing speed is {wpm} WPM.")
            test.destroy()
    
# A button that shows next
    tk.Button(test, text="Next", bg=button_colour, borderwidth=8, relief="raised", pady=30, padx=50, command=next, font="comicsansms 15").pack(anchor="e", pady=20)
    
# Packing text area here to show it below next button 
    text_area.pack()
    
# Running the test window
    test.mainloop()

# Help command that creates a help window and it contains how to use typing master          
def help():
    
# Creating command of back button which backs to the main window
    def back():
        help_window.destroy()
        
# Creating help window
    help_window = tk.Toplevel()
    help_window.title("Help")
    help_window.geometry("690x1480")
    help_window.config(bg="#f0f8ff")
    
    tk.Label(help_window, text="Instructions To\nUse The App", font="comicsansms 15", bg="light grey").pack(fill="x")
    
# Making a text variable
    textvar = tk.StringVar()
    textvar.set("""
    1. Click on "Start Test" to begin the typing speed test.
    
    2. A random sentence will appear on the screen.
    
    3. Type the exact sentence in the text box provided.
    
    4. After you type the sentence, click the "Next" button:
        
        °if the sentence is correct, a new ne will appear.
        
        °if it is wrong, you will be asked to try again.
        
    5. You need to type 5 correct sentences to complete the test.
    
    6. Your typing speed will be shown in words per minute(WPM) after completing the test.
    
    7.  Use the exit button to close the application at any time.
                                      """)
                                      
    help_label = tk.Label(help_window, textvariable=textvar, wraplength=600, justify="left", font="comicsansms 10", bg="#f0f8ff")
    help_label.pack(fill="x")
    
# Creating a back button
    tk.Button(help_window, text="Back", pady=25, padx=30, bg="grey", font="comicsansms 15", command=back).pack(anchor="e")
    
# Running the help window
    help_window.mainloop()
  
# command of setting button  
def setting():
    global font_size, sentence_goal,  theme_colour, text_area_colour,button_colour
    
# Making command of save button which saves the changes and exit the setting window
    def save():
        global font_size, sentence_goal,  theme_colour, text_area_colour,button_colour
        
        font_size = fontvar.get()
        sentence_goal = sentencevar.get()
        theme_colour = themevar.get()
        text_area_colour = text_areavar.get()
        button_colour = buttonvar.get()
        setting_window.destroy()
    
    setting_window = tk.Toplevel()
    setting_window.title("Settings")
    setting_window.geometry("690x1480")
    
# Creating labels
    tk.Label(setting_window, text="Settings", font="comicsansms 25", pady=30).grid(row=0, column=0, columnspan=2, pady=20)
    
    tk.Label(setting_window, text="Change font size:", font="comicsansms 10").grid(row=1, column=0, pady=20)
    
    tk.Label(setting_window, text="Change number of\nsentences to correct:", font="comicsansms 10").grid(row=2, column=0, pady=20)
    
    tk.Label(setting_window, text="Change theme colour:", font="comicsansms 10").grid(row=3, column=0, pady=20)
    
    tk.Label(setting_window, text="Change typing area\ncolour:", font="comicsansms 10").grid(row=4, column=0, pady=20)
    
    tk.Label(setting_window, text="Change next button\ncolour:", font="comicsansms 10").grid(row=5, column=0, pady=20)
    
# creating some variables
    fontvar = tk.IntVar(value=15)
    sentencevar = tk.IntVar(value=5)
    themevar = tk.StringVar(value="#f0f8ff")
    text_areavar = tk.StringVar(value="light grey")
    buttonvar = tk.StringVar(value="grey")
    
# creating entries
    entry1 = tk.Entry(setting_window, textvariable=fontvar)
    entry1.grid(row=1, column=1)
    
    entry2 = tk.Entry(setting_window, textvariable=sentencevar)
    entry2.grid(row=2, column=1)
    
    entry3 = tk.Entry(setting_window, textvariable=themevar)
    entry3.grid(row=3, column=1)
    
    entry4 = tk.Entry(setting_window, textvariable=text_areavar)
    entry4.grid(row=4, column=1)
    
    entry5 = tk.Entry(setting_window, textvariable=buttonvar)
    entry5.grid(row=5, column=1)
    
# Creating a save button
    tk.Button(setting_window, text="Save", font="comicsansms 15", pady=20, bg="grey", borderwidth=8, relief="groove", command=save).grid(row=6, column=1)
    
# Running the setting window
    setting_window.mainloop()
    
# creating command of about us button which shows about the app
def about():
    tmsg.showinfo("About Us", "This is a Typing master app.\nIt is made by Raunak to\ntest typing speed.")
    
# Making window
root = tk.Tk()
root.title("Typing by Raunak")
root.geometry("720x1540")

# creating the main window
root.config(bg="#f5f5f5")

tk.Label(root, text="Typing Master", font="comicsansms 20 bold", bg="#f5f5f5", fg="#212121").grid(row=0, column=0, padx=120)

tk.Label(root, bg="#f5f5f5", text="Raunak's Typing\nMaster - Improve\nspeed and accuracy.", font="comicsansms 15").grid(row=1, column=0, pady=100)

menu = tk.Label(root, bg="#f0f8ff", relief="groove", borderwidth=16)
menu.grid(row=3, column=0)

tk.Button(menu, text="Start Test", font="lucida 10", bg="dark grey", pady=30, relief="groove", borderwidth=8, command=start).grid(row=0, column=0, pady=30,  sticky="w", padx=30)

tk.Button(menu, text="Help", font="lucida 10", bg="dark grey", pady=30, padx=60, relief="groove", borderwidth=8, command=help).grid(row=0, column=1, pady=30, sticky="e", padx=30)

tk.Button(menu, text="About Us", font="lucida 10", bg="dark grey", padx=35, pady=30, relief="groove", borderwidth=8,command=about).grid(row=1, column=0, pady=30, sticky="w", padx=30)

tk.Button(menu, text="Settings", font="lucida 10", bg="dark grey", pady=30, relief="groove", borderwidth=8, command=setting).grid(row=1, column=1, pady=30, sticky="e", padx=30)

tk.Button(menu, text="Exit", font="lucida 10", bg="dark grey", pady=30, padx=82, relief="groove", borderwidth=8, command=exit).grid(row=2, column=0, pady=30, columnspan=2)

tk.Label(root, text="Press 'Start Test'\nand begin typing!", font="comicsansms 15", bg="#f5f5f5").grid(row=4, column=0, pady=130)

# Running the window
root.mainloop()