import tkinter as tk
import customtkinter

root_tk = customtkinter.CTk()

# root_tk.geometry(f"{600}x{500}")
root_tk.title("Password generator")
logo_img = tk.PhotoImage(file="lock (3).png")
main_label = customtkinter.CTkLabel(master=root_tk,
                                    corner_radius=8, image=logo_img)
main_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

logo_label = customtkinter.CTkLabel(master=root_tk, text="Password Generator",
                                    corner_radius=8, text_font=('Egyptian nights', 50))
logo_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

# # labels
# Labels
website_label = customtkinter.CTkLabel(master=root_tk, text="Website:",
                                       corner_radius=8)
# website_label = Label(text="Website:")
website_label.place(relx=0.2, rely=0.5, anchor=tk.CENTER)
email_label = customtkinter.CTkLabel(master=root_tk, text="Email/Username:",
                                     corner_radius=8)
# email_label = Label(text="Email/Username:")
email_label.place(relx=0.2, rely=0.65, anchor=tk.CENTER)
password_label = customtkinter.CTkLabel(master=root_tk, text="Password:",
                                        corner_radius=8)
# password_label = Label(text="Password:")
password_label.place(relx=0.2, rely=0.8, anchor=tk.CENTER)

##ENtries
# Entries

website_entry = customtkinter.CTkEntry(master=root_tk, placeholder_text="Website name", width=150, border_width=2,
                                       corner_radius=10)
website_entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
website_entry.focus()
email_entry = customtkinter.CTkEntry(master=root_tk, placeholder_text="Email/Username", width=150, border_width=2,
                                     corner_radius=10)
email_entry.place(relx=0.5, rely=0.65, anchor=tk.CENTER)
password_entry = customtkinter.CTkEntry(master=root_tk, placeholder_text="Password", width=150, border_width=2,
                                        corner_radius=10)
password_entry.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

# Buttons
# Buttons
from find_password import find_password

search_button = customtkinter.CTkButton(master=root_tk, width=13, border_width=0, corner_radius=8, text="Search",
                                        command=find_password)
search_button.place(relx=0.8, rely=0.5, anchor=tk.CENTER)
from generate_password import generate_password


def gen_password():
    password = generate_password()
    password_entry.insert(tk.INSERT, password)


generate_password_button = customtkinter.CTkButton(master=root_tk, border_width=0, corner_radius=8,
                                                   text="Generate", command=gen_password)
generate_password_button.place(relx=0.3, rely=0.9, anchor=tk.CENTER)

from save_password import save

add_button = customtkinter.CTkButton(master=root_tk, width=120, border_width=0, corner_radius=8, text="Add",
                                     command=save)
add_button.place(relx=0.7, rely=0.9, anchor=tk.CENTER)

# root_tk.mainloop()
