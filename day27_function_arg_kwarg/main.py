import tkinter

window = tkinter.Tk()
window.title("My First GUI program")
window.minsize(width=500, height=300)

# label

my_label = tkinter.Label(text= "I am a Label",
                         font=("Arial", 24, "bold", "italic"))
my_label.pack(side="left")
my_label.pack()


# # ---------------------------------------------------- 

# # Advanced Python Arguments (*args, **kwargs)
# import turtle

# tim =turtle.Turtle()
# tim.write("some text")



# window.mainloop()

