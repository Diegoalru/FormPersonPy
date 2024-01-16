"""
Se crea una ventana con los widgets especificados.
"""

import tkinter as tk

import utils

from person import Person


class PersonForm:
    """
    This class creates a tkinter window with the specified widgets.
    """

    def __init__(self, root):
        """
        Creates a PersonForm object.
        :param root: The root widget for the tkinter GUI.
        """
        # This is the initialization of the root widget for the tkinter GUI.
        self.root = root
        # This sets the title of the window to "Person".
        self.root.title("Person")
        # This sets the geometry of the window to 220x160 pixels (width x height).
        self.root.geometry("220x160")
        # This places the window in the center of the screen.
        self.root.eval('tk::PlaceWindow . center')
        # This makes the window non-resizable.
        self.root.resizable(0, 0)
        # This calls the create_window method to create the window with the specified widgets.
        self.create_window()

    def create_window(self):
        """
        Creates the window with the specified widgets.
        :return: None
        """
        name_label = tk.Label(text="Name: ")
        # Places the 'name_label' widget in the grid layout of the tkinter window.
        # Specifies the column in which the widget is placed.
        # Specifies the row in which the widget is placed.
        # 'tk.E' means the widget sticks to the east or right side of the cell.
        # The 'padx' and 'pady' parameters specify the amount of padding in the x (horizontal)
        # and y (vertical) directions respectively.
        name_label.grid(column=0, row=0, sticky=tk.E, padx=5, pady=5)
        name_label.grid(column=0, row=0, sticky=tk.E, padx=5, pady=5)
        name_entry = tk.Entry()
        name_entry.grid(column=1, row=0)

        email_label = tk.Label(text="Email: ")
        email_label.grid(column=0, row=1, sticky=tk.E, padx=5, pady=5)
        email_entry = tk.Entry()
        email_entry.grid(column=1, row=1)

        phone_label = tk.Label(text="Phone: ")
        phone_label.grid(column=0, row=2, sticky=tk.E, padx=5, pady=5)
        phone_entry = tk.Entry()
        phone_entry.grid(column=1, row=2)

        age_label = tk.Label(text="Age: ")
        age_label.grid(column=0, row=3, sticky=tk.E, padx=5, pady=5)
        age_entry = tk.Entry()
        age_entry.grid(column=1, row=3)

        submit_button = tk.Button(
            text="Submit",
            command=lambda: self.submit(
                name_entry.get(),
                email_entry.get(),
                phone_entry.get(),
                age_entry.get()))
        submit_button.grid(column=1, row=4)

        clear_button = tk.Button(
            text="Clear",
            command=lambda: self.clear(
                name_entry,
                email_entry,
                phone_entry,
                age_entry))
        clear_button.grid(column=0, row=4)

    @staticmethod
    def submit(name, email, phone, age):
        """
        Validates the input and creates a Person object.
        :param name: The name of the person.
        :param email: The email of the person.
        :param phone: The phone of the person.
        :param age: The age of the person.
        :return: None
        """
        if name == "" or email == "" or phone == "" or age == "":
            tk.messagebox.showerror("Error", "All fields are required!")
            return

        if not utils.validate_email(email):
            tk.messagebox.showerror("Email Error", "Email not valid")
            return

        if not utils.validate_phone(phone):
            tk.messagebox.showerror("Phone Error", "Phone not valid")
            return

        if not utils.validate_age(age):
            tk.messagebox.showerror("Age Error", "Age not valid")
            return

        person = Person(name, email, phone, age)
        tk.messagebox.showinfo("Person", person)

    @staticmethod
    def clear(name_entry, email_entry, phone_entry, age_entry):
        """
        Clears the input fields.
        :param name_entry: The name entry field.
        :param email_entry: The email entry field.
        :param phone_entry: The phone entry field.
        :param age_entry: The age entry field.
        :return: None
        """
        name_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        age_entry.delete(0, tk.END)
        name_entry.focus()
