from tkinter import *
from text import word_choice, polish_text, english_text
from tkinter import ttk
import time

# Making new Tk window and importing word list
x = word_choice(words=english_text)
end = False
entry_text = x[0:100]
window = Tk()
window.title('Typing Speed Program')
window.config(width= 600, height=600, padx= 15, pady=25, bg='black')
count = 0


# Start Button Command and Reset game

def stop():
    window.destroy()

def start_typing():
    global x, entry, words_text, t0, start_button, entry_text, canvas_window, start_text
    if box.get() == 'English':
        x = word_choice(words=english_text)
    elif box.get() == 'Polish':
        x = word_choice(words=polish_text)
    entry_text = x[0:100]
    canvas.delete(greeting_text)
    start_text = canvas.create_text(200, 100, text='Start Typing and press Enter after each word', font=('Arial', 10, 'bold'), fill='white')
    words_text = canvas.create_text(200, 170, text = x[0:3], font = ('Arial',10, 'bold'), fill= 'white')
    entry = Entry(window, width=30)
    entry.bind('<Return>', show)
    canvas_window = canvas.create_window(200, 250, window=entry)
    t0 = time.time()
    start_button.destroy()
    box.destroy()


# Show new word after good type and count score
def show(event=None):
    global words_text, entry, entry_text, count, canvas_window, score_text
    y = entry.get()

    if y == entry_text[0]:
        del entry_text[0]
        print(entry_text[0])
        entry.delete(0, END)
        canvas.delete(words_text)
        list_text = f'{entry_text[0]} {entry_text[1]} {entry_text[2]}'
        words_text = canvas.create_text(200, 170, text=list_text, font=('Arial', 10, 'bold'), fill='white')
        count += 1
        t1 = time.time()

    # Show score
    if count == 20:
        if t1-t0 >= 60:
            b = round(t1 - t0, 2)
            canvas.delete(canvas_window)
            canvas.delete(words_text)
            canvas.delete(start_text)
            end = True
            words_text = canvas.create_text(200, 170,
                                            text='Your speed was poor ;(',
                                            font=('Arial', 10, 'bold'), fill='white')
            score_text = canvas.create_text(200, 250,
                                            text=f'Your score was 30 words in {b} seconds!!',
                                            font=('Arial', 10, 'bold'), fill='white')
            quit_button = Button(text='Exit', command=stop)
            quit_button.grid(column=0, row=2, columnspan=2)

        elif 60 >= t1-t0 >= 30:
            b = round(t1 - t0, 2)
            canvas.delete(canvas_window)
            canvas.delete(words_text)
            canvas.delete(start_text)
            end = True
            words_text = canvas.create_text(200, 170,
                                            text='You were average.',
                                            font=('Arial', 10, 'bold'), fill='white')
            score_text = canvas.create_text(200, 250,
                                            text=f'Your score was 30 words in {b} seconds!!',
                                            font=('Arial', 10, 'bold'), fill='white')
            quit_button = Button(text='Exit', command=stop)
            quit_button.grid(column=0, row=2, columnspan=2)

        else:
            b = round(t1 - t0, 2)
            canvas.delete(canvas_window)
            canvas.delete(words_text)
            canvas.delete(start_text)
            end = True
            words_text = canvas.create_text(200, 170,
                                            text='You were FAST!!',
                                            font=('Arial', 10, 'bold'), fill='white')
            score_text = canvas.create_text(200, 250,
                                            text=f'Your score was 30 words in {b} seconds!!',
                                            font=('Arial', 10, 'bold'), fill='white')
            quit_button = Button(text='Exit', command= stop)
            quit_button.grid(column=0, row=2, columnspan=2)



# Create buttons and Entries

global canvas, greeting_text
canvas = Canvas(width= 400, height = 400, bg='black', highlightthickness = 0, bd=0)
greeting_text = canvas.create_text(200, 200, text = 'Choose your language and click start to start typing', font = ('Arial',10, 'bold'), fill= 'white')
canvas.grid(column= 0, row=0, columnspan=2)


n = StringVar()
n.set('English')
box = ttk.Combobox(window, width = 12, textvariable = n)
box['values'] = ('English', 'Polish')
box.grid(column = 1, row =2)

start_button = Button(width= 10, text = 'Start', command= start_typing)
start_button.grid(column=0, row =2)


window.mainloop()