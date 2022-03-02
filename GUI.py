# import all methods and classes from the tkinter
from tkinter import *

# Function for showing the Pokemon
def showPok() :

	# Create a GUI window
	new_gui = Tk()
	
	# Set the background colour of GUI window
	new_gui.config(background = "white")

	# set the name of tkinter GUI window
	new_gui.title("Pokemon API")

	# Set the configuration of GUI window
	new_gui.geometry("550x600")


	# start the GUI
	new_gui.mainloop()

	
# Driver Code
if __name__ == "__main__" :

	# Create a GUI window
	gui = Tk()
	
	# Set the background colour of GUI window
	gui.config(background = "white")

	# set the name of tkinter GUI window
	gui.title("Pokemon API")

	# Set the configuration of GUI window
	gui.geometry("250x140")

	# Create a Pokemon lable : label with specified font and size
	pok_label = Label(gui, text = "Pokemon API", bg = "dark gray",
						    font = ("times", 28, 'bold'))

	# Create a Enter Pokemon : label
	pok_name = Label(gui, text = "Enter Pokemon Name", bg = "light green")
	
	# Create a text entry box for filling or typing the information.
	pok_field = Entry(gui)

	# Create a Show Pokemon Button and attached to showPok function
	Show = Button(gui, text = "Show Pokemon", fg = "Black",
							bg = "Red", command = showPok)

	# Create a Exit Button and attached to exit function
	Exit = Button(gui, text = "Exit", fg = "Black", bg = "Red", command = exit)
	
	# grid method is used for placing
	# the widgets at respective positions
	# in table like structure.
	pok_label.grid(row = 1, column = 1)

	pok_name.grid(row = 2, column = 1)

	pok_field.grid(row = 3, column = 1)

	Show.grid(row = 4, column = 1)

	Exit.grid(row = 6, column = 1)
	
	# start the GUI
	gui.mainloop()
	
