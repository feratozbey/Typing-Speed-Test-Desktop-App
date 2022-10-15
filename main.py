import tkinter
from random import choice

# Constants
MIN = 60
FONT_NAME = 'Monaco'
APP_BG_COLOR = '#749F82'
TEXT_COLOR = '#CFFF8D'

# Reads all paragraphs from text file and randomly chooses a paragraph
with open('50 paragraphs.txt') as txt:
    lines = txt.readlines()
random_line = choice(lines)


# This function is triggered first, when button is pressed.
def call_paragraph():
    # Cleans text field and pastes random paragraph
    text_field.delete('1.0', tkinter.END)
    text_field.insert(1.0, random_line)
    # Triggers next function
    count_down(MIN)


def count_down(time):

    # Count down stops when timer hits "0"
    if time >= 0:

        # Handles timer
        canvas.itemconfig(timer_text, text=f"{time}")
        window.after(1000, count_down, time - 1)

        # When timer hits "0"
        if time == 0:
            score = 0 # To keep track of how many words have been written correct

            # Gets entry and paragraph splits within spaces. Creates array for entry and paragraph to compare
            answer = entry.get()
            answer_array = answer.split(" ")
            random_text = random_line.replace('\n', '')
            random_text_array = random_text.split(" ")

            # For loop to compare each words between entry and paragraph
            for i in range(len(random_text_array) + 1):
                try:
                    if answer_array[i] == random_text_array[i]:
                        score += 1

                # If user can not type all the words, there will be discrepancy between length of the entry and array
                # If it occurs exception will handle the situation
                except IndexError:
                    pass

            # Shows up the score on textfield
            conclusion = f'==========================================================================\n' \
                         f'==================  YOU CAN TYPE {score} WORDS PER MINUTE! ===============\n' \
                         f'=========================================================================='
            text_field.delete('1.0', tkinter.END)
            text_field.insert(5.0, conclusion)


# Creates window and configures it
window = tkinter.Tk()
window.title('Typing Speed Test')
window.config(padx=50, pady=80, background=APP_BG_COLOR)

# Computer generated paragraph textbox widget
text_field = tkinter.Text(window, width=75, height=10, background='#A8E890', foreground='#425F57', font=(FONT_NAME, 12))
text_field.grid(row=0, column=0)
text_field.insert(5.0, '==========================================================================''======  When you '
                       'are ready press "Begin".  Text will appear here! '
                       '========''=============================================================================')

# Creates canvas
canvas = tkinter.Canvas(window, width=500, height=350, highlightthickness=0, background=APP_BG_COLOR)

# Creates clock image and places it
clock = tkinter.PhotoImage(file='images/clock.png')
canvas.create_image(250, 150, image=clock)

# Count down text on clock
timer_text = canvas.create_text(250, 150, text="60", fill=TEXT_COLOR, font=(FONT_NAME, 70, 'bold'))

# User entry textbox widget
entry = tkinter.Entry(window, width=70)
canvas.create_window(250, 300, window=entry)
canvas.grid(row=1, column=0)

# Label
canvas.create_text(250, 280, text="Type Here", fill=TEXT_COLOR, font=(FONT_NAME, 16))

# Begin  Button
button = tkinter.Button(text='Begin', command=call_paragraph, width=10, height=1,
                        padx=10, pady=10, background='#425F57', foreground='#CFFF8D', font=(FONT_NAME, 16))
button.grid(row=2, column=0)

window.mainloop()
