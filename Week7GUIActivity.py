# <!-- #a)Write a console and GUI program that asks the user how many words they would like to write to a
# file, and then asks the user to enter that many words, one at a time. The words should be written to
# a file.
# (b) Write another program that reads the words from the file and displays the following data:
# • The number of words in the file.
# • The longest word in the file.
# • The average length of all of the words in the file. -->



# 

# # Create GUI components
# root = tk.Tk()
# root.title("Word File Processor")
    
# write_button = tk.Button(root, text="Write to File", command=write_to_file)
# read_button = tk.Button(root, text="Read from File", command=read_file)
# results_label = tk.Label(root, text="")

# # Place GUI components
# num_words_label.grid(row=0, column=0)
# num_words_entry.grid(row=0, column=1)
# write_button.grid(row=12, column=0)
# read_button.grid(row=12, column=1)
# results_label.grid(row=13, column=0, columnspan=2)

# root.mainloop()
# 
import tkinter


class myGUI:
    def __init__(self):
    # Create the main window.
     self.main_window = tkinter.Tk()
     self.main_window.title("Word File Reader")

    # Create three frames to group widgets.
     self.top_frame = tkinter.Frame()
     self.mid_frame = tkinter.Frame()
     self.button_frame = tkinter.Frame()
     self.result_frame = tkinter.Frame()

    # Create the widgets for the top frame and pack them( a label and a text box)
     num_words_label = tkinter.Label(self.top_frame, text="How many words will you write in a file? ")
     self.num_words_entry = tkinter.Entry(self.top_frame,bg='light grey',bd=2,width ='5')
     num_words_label.pack(side = 'left')
     self.num_words_entry.pack(side='left')
     word_entires = []
     for i in range(10):
            word_label = tkinter.Label(self, text=f"Word {i+1}:")
            word_entry = tkinter.Entry(self)
            word_entires.append(word_entry)
            word_label.grid(row=i+2, column=0)
            word_entry.grid(row=i+2, column=1)
    # Create the widgets for the top frame and pack them( a label and a text box)
     num2_label = tkinter.Label(self.mid_frame, text="Enter a number2")
     self.num2_entry = tkinter.Entry(self.mid_frame,bg='light grey',bd=2,width ='10')
     num2_label.pack(side = 'left')
     self.num2_entry.pack(side='left')

# Create the widgets for the button frame and pack them( calcbutton and a quit button)
     write_button = tkinter.Button(self.button_frame, text = "Write into File", command = self.file_write)
     read_button = tkinter.Button(self.button_frame, text=)
     quit_button = tkinter.Button(self.button_frame, text='Quit',
     command=self.main_window.destroy)
     write_button.pack(side='left')
     quit_button.pack(side='left')

# Create the widgets for multiline text area widget and pack it(tkinter.Text is a multiline text area)
     self.result_ta = tkinter.Text(self.result_frame, bg='light blue',height=10, width=40)
     self.result_ta.pack()
     self.top_frame.pack()
     self.mid_frame.pack()
     self.button_frame.pack()
     self.result_frame.pack()

# Enter the tkinter main loop.
     tkinter.mainloop()

# The calc_sum method is a callback function for the Calculate button.
    def file_write():
        num_words = int(numwords_entry.get())

        with open("words.txt", "w") as f:
            for i in range(num_words):
                words = word_entires[i].get()
                f.write(words + "\n")

        results_label.congif(text = f"{num_words} words were written to the file 'words.txt'.")


    def read_file():    
        with open("words.txt", "r") as f:
            words = f.read().splitlines()
        
        num_words = len(words)
        longest_word = max(words, key=len)
        avg_length = sum(len(word) for word in words) / num_words
        avg_length = round(avg_length, 2)
    
       results_label.config(text=f"Number of words: {num_words}\nLongest word: {longest_word}\nAverage word length: {avg_length}")

my_gui=myGUI()
