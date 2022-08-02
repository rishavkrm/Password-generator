import tkinter as tk
import customtkinter


# # ---------------------------- UI SETUP ------------------------------- #
#
# window = Tk()
# window.title("Password Manager")
# window.config(padx=50, pady=50)
#
# canvas = Canvas(height=200, width=200)
# logo_img = PhotoImage(file="logo.png")
# canvas.create_image(100, 100, image=logo_img)
# canvas.grid(row=0, column=1)
#
# # Labels
# website_label = Label(text="Website:")
# website_label.grid(row=1, column=0)
# email_label = Label(text="Email/Username:")
# email_label.grid(row=2, column=0)
# password_label = Label(text="Password:")
# password_label.grid(row=3, column=0)
#
# # Entries
# website_entry = Entry(width=21)
# website_entry.grid(row=1, column=1)
# website_entry.focus()
# email_entry = Entry(width=35)
# email_entry.grid(row=2, column=1, columnspan=2)
# email_entry.insert(0, "lenargasimov@gmail.com")
# password_entry = Entry(width=21)
# password_entry.grid(row=3, column=1)
#
# # Buttons
# search_button = Button(text="Search", width=13, command=find_password)
# search_button.grid(row=1, column=2)
# generate_password_button = Button(text="Generate Password", command=generate_password)
# generate_password_button.grid(row=3, column=2)
# add_button = Button(text="Add", width=36, command=save)
# add_button.grid(row=4, column=1, columnspan=2)
#
# window.mainloop()
# #
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # self.geometry(f"{600}x{500}")
        self.title("Password generator")
        canvas = tk.Canvas(height=200, width=200)
        logo_img = tk.PhotoImage(file="logo.png")
        canvas.create_image(100, 100, image=logo_img)
        canvas.grid(row=0, column=1)
        # labels
        # Labels
        website_label = customtkinter.CTkLabel(master=self, text="Website:", fg_color=("white", "gray75"),
                                               corner_radius=8)
        # website_label = Label(text="Website:")
        website_label.grid(row=1, column=0)
        email_label = customtkinter.CTkLabel(master=self, text="Email/Username:", fg_color=("white", "gray75"),
                                             corner_radius=8)
        # email_label = Label(text="Email/Username:")
        email_label.grid(row=2, column=0)
        password_label = customtkinter.CTkLabel(master=self, text="Password:", fg_color=("white", "gray75"),
                                                corner_radius=8)
        # password_label = Label(text="Password:")
        password_label.grid(row=3, column=0)

        ##ENtries
        # Entries

        website_entry = customtkinter.CTkEntry(master=self, placeholder_text="Website name", width=21, border_width=2,
                                               corner_radius=10)
        website_entry.grid(row=1, column=1)
        website_entry.focus()
        email_entry = customtkinter.CTkEntry(master=self, placeholder_text="Website name", width=35, border_width=2,
                                             corner_radius=10)
        email_entry.grid(row=2, column=1, columnspan=2)
        email_entry.insert(0, "rishavkumar2573@gmail.com")
        password_entry = customtkinter.CTkEntry(master=self, placeholder_text="Website name", width=21, border_width=2,
                                                corner_radius=10)
        password_entry.grid(row=3, column=1)

        # Buttons
        # Buttons
        from find_password import find_password
        import generate_password
        from save_password import save
        find_password = find_password(website_entry, tk.messagebox)
        search_button = customtkinter.CTkButton(master=self, width=13, border_width=0, corner_radius=8, text="Search",
                                                command=find_password)
        search_button.grid(row=1, column=2)

        generate_password = generate_password()
        generate_password_button = customtkinter.CTkButton(master=self, border_width=0, corner_radius=8,
                                                           text="CTkButton", command=generate_password)
        generate_password_button.grid(row=3, column=2)

        add_button = customtkinter.CTkButton(master=self, width=120, border_width=0, corner_radius=8, text="Add",
                                             command=save)
        add_button.grid(row=4, column=1, columnspan=2)
