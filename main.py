"""
This is the main entry point of the application.
It creates an instance of the PersonForm class and starts the tkinter main loop.
"""

import tkinter as tk

from create_window import PersonForm

# This is the main entry point of the application.
# It creates an instance of the PersonForm class and starts the tkinter main loop.
if __name__ == '__main__':
    try:
        # Create an instance of the PersonForm class.
        # The PersonForm class is responsible for creating and managing the application's GUI.
        window = PersonForm(tk.Tk())

        # Start the tkinter main loop.
        # The main loop is what makes the application run and respond to user input.
        window.root.mainloop()
    except tk.TclError as e:
        # If an exception occurs, print the exception to the console.
        print(e)
