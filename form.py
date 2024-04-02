import tkinter as tk
from tkinter import messagebox
import re
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import *
def submit_data():
    name = name_entry.get()
    aicte_id = aicte_id_entry.get()
    email = email_entry.get()
    phone_number = phone_number_entry.get()
    college_name = college_Name_entry.get()

    if not (name and aicte_id and email and phone_number and college_name):
        messagebox.showerror("Error", "All fields are required!")
        return

    if not validate_email(email):
        messagebox.showerror("Error", "Invalid email format!")
        return
    if not validate_phone_number(phone_number):
        messagebox.showerror("Error", "Invalid phone number format!")
        return
    generate_pdf(name,aicte_id,email,phone_number,college_name)
def validate_email(email):
        # Regular expression for email validation
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    else:
        return False

def validate_phone_number(phone_number):
            # Regular expression for phone number validation
    pattern = r'^[0-9]{10}$'
    if re.match(pattern, phone_number):
        return True
    else:
        return False

def generate_pdf(name,aicte_id,email,phone_number,college_name):
    c = canvas.Canvas('student_registration_form.pdf',pagesize=A4)
    content = [
        f'Name:{name}',
        f'AICTE ID:{aicte_id}',
        f'Email:{email}',
        f'Phone Number:{phone_number}',
        f'College Name:{college_name}'

    ]
    y = 700
    for i in content:
        c.drawString(100,y,i)
        y-=20
    c.save()
    print("Name:", name)
    print("AICTE ID:", aicte_id)
    print("Email:", email)
    print("Phone Number:", phone_number)
    print("College Name:", college_name)

root = tk.Tk()
root.geometry("400x250")
root.title("Student Registration Form")

name_label = tk.Label(root, text='Name')
name_label.grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

aicte_id_label = tk.Label(root, text='AICTE ID')
aicte_id_label.grid(row=1, column=0)
aicte_id_entry = tk.Entry(root)
aicte_id_entry.grid(row=1, column=1)

email_label = tk.Label(root, text='Email')
email_label.grid(row=2, column=0)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1)

phone_number_label = tk.Label(root, text='Phone Number')
phone_number_label.grid(row=3, column=0)
phone_number_entry = tk.Entry(root)
phone_number_entry.grid(row=3, column=1)

college_Name_label = tk.Label(root, text='College Name')
college_Name_label.grid(row=4, column=0)
college_Name_entry = tk.Entry(root)
college_Name_entry.grid(row=4, column=1)

submit_button = tk.Button(root, text="Submit", command=submit_data)
submit_button.grid(row=5, column=1)

error_label = tk.Label(root, text="")
error_label.grid(row=6, column=1)

root.mainloop()
