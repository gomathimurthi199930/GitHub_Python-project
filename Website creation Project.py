from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from tkinter import Menu
import tkinter as tk
import cv2
from PIL import Image, ImageTk, ImageEnhance, ImageFilter
from tkinter import messagebox, Toplevel
import json
import os
import platform
import subprocess
import webbrowser

window=Tk()
window.title("www.wildwonderzoologicalpark.in")
window.geometry("1264x2000")
canvas_width=1650
canvas_height=40

'''# === Scrollable Canvas Setup ===
canvas = tk.Canvas(window)
scrollbar = ttk.Scrollbar(window, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0,0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="right", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")'''

# ---------- HEADER FRAME ----------
header_frame = tk.Frame(window, bg="white", height=100)
header_frame.pack(fill="x")

# Load and place images
def load_logo(path, size=(100, 100)):
    img = Image.open(path)
    img = img.resize(size, Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(img)

# Replace these paths with your actual logo file paths
image = load_logo("D:/1. Python/New folder/Logo2.png", size=(40,40))
logo_label = tk.Label(header_frame, image=image, bg="white")
logo_label.pack(side="left", padx=10, pady=10)

# If you want to add title text (optional)
title_label = tk.Label(header_frame, text="Wild Wonder Zoological Park", font=("Arial", 14, "bold"), bg="white")
title_label.pack(side="left", padx=2)


notebook=ttk.Notebook(window)
notebook.pack(expand=1,fill=BOTH)

window1=ttk.Frame(notebook) 
notebook.add(window1,text="Home")

window0=ttk.Frame(notebook)
notebook.add(window0,text="Dashboard")

window2=ttk.Frame(notebook)
notebook.add(window2,text="Animal Info")

window3=ttk.Frame(notebook)
notebook.add(window3,text="Online Ticket Booking")

window6=ttk.Frame(notebook)
notebook.add(window6,text="Contact us")

# Create canvas and place background image
canvas = Canvas(window1, width=1440, height=600)
canvas.pack(fill="both", expand=True)

# Load background image
bg_img = PhotoImage(file="D:/1. Python/New folder/Forest2.png")
canvas.create_image(0, 0, anchor=NW, image=bg_img)

# Add text with transparent background using canvas
canvas.create_text(200, 200, text="Welcome to our Zoo!",font=("Arial", 24, "bold"), fill="#a7c957")

canvas.create_text(200, 250, text="About the Zoo",font=("Arial", 16, "bold"), fill="#a7c957")

zoo_info = (
    "'Our Zoological Park was the first Zoo established in the\n"
    "country in 1855. It is one of the largest Zoos in Southeast\n"
    "Asia, spreading across 602 hectares of land. It is one of\n"
    "the most modern and scientifically managed Zoos in the\n"
    "country and it is rated as the 'Best Zoo' in the country\n"
    "with a top score of 82% in the first Management\n"
    "Effectiveness Evaluation conducted by the Central Zoo\n"
    "Authority, MOEF & CC. The park works with the mission\n"
    "of conservation breeding of rare and endangered\n"
    "animals, veterinary care & conservation education.'"
)

canvas.create_text(260, 390, text=zoo_info,
                   font=("Arial", 14), fill="#a7c957", anchor="center", justify=LEFT)
canvas.image = bg_img

footer = tk.Frame(window, bg="#222222", height=80)
footer.pack(side="bottom", fill="x")

# Create style for footer labels (if using ttk)
style = ttk.Style()
style.configure("Footer.TLabel", background="#222222", foreground="white", font=("Arial", 10,"bold"))

# Left label
left_label = ttk.Label(footer, text="Location: Wild Wonder Zoological Park,\nVandalur, Chennai, \nTamil Nadu - 600 048.", style="Footer.TLabel")
left_label.place(relx=0.01, rely=0.5, anchor="w")

# Center label
center_label = ttk.Label(footer, text="Contact us \nPhone: 044-29542301 \nFax: 044-22750741", style="Footer.TLabel")
center_label.place(relx=0.5, rely=0.5, anchor="center")

# Right label
right_label = ttk.Label(footer, text="For Help & Support \nEmail:Support@wildwonderzoologicalpark.in", style="Footer.TLabel")
right_label.place(relx=0.99, rely=0.5, anchor="e")

# Keep a reference to the image to prevent garbage collection

def move_text():
    x1,y1,x2,y2 = canvas.bbox(text)
    if x2<0:
        canvas.move(text.canvas_width,0)
    else:
        canvas.move(text,-2,0)
    window0.after(30,move_text)

canvas=tk.Canvas(window0,width=canvas_width,height=canvas_height,bg="#a4eb34")
canvas.pack()

text=canvas.create_text(canvas_width,18,text="Our Zoological park is happy to welcome you to the Zoo premises. The Zoo is open to visitor following the precautionary measures, safety protocols and guidelines to provide a safe Zoo experience.!",fill="black",font=("Arial",12,"bold"))
move_text();


label6=Label(window0,text="Our Zoological Park Timings",font="arial 16 bold")
label6.place(relx=0.15,rely=0.13,anchor=CENTER)

table=ttk.Treeview(window0,columns=("day","time"),show="headings")
table.heading("day",text="Day")
table.heading("time",text="Timings")
table.place(relx=0.15,rely=0.35,anchor=CENTER)
 

table.insert("",index=0,values=("Monday","Closed/Holiday"))
table.insert("",index=1,values=("Tuesday","08:30 A.M - 04.00 P.M"))
table.insert("",index=2,values=("Wednesday","08:30 A.M - 04.00 P.M"))
table.insert("",index=3,values=("Thursday","08:30 A.M - 04.00 P.M"))
table.insert("",index=4,values=("Frtday","08:30 A.M - 04.00 P.M"))
table.insert("",index=5,values=("Saturday","08:30 A.M - 04.00 P.M"))

table.column("#1", width=80)  # Set width of first column to 50 pixels
table.column("#2", width=140)

label7=Label(window0,text="Zoo Park Entry Fee",font="arial 16 bold")
label7.place(relx=0.50,rely=0.13,anchor=CENTER)

label8=Label(window0,text="Weekday Charges",font="arial 15 bold underline")
label8.place(relx=0.55,rely=0.18,anchor=E)

label9=Label(window0,text="""> Rs.70 per Adult (Above 10 years)
> Rs.45 per Child (3-10 years)
> Rs.120 for Still Camera
> Rs.600 for Video Camera
""",font="arial 13")
label9.place(relx=0.61,rely=0.285,anchor=E)

label10=Label(window0,text="Weekend & Holiday Charges",font="arial 15 bold underline")
label10.place(relx=0.61,rely=0.38,anchor=E)

label11=Label(window0,text="""> Rs.80 per Adult (Above 10 years)
> Rs.55 per Child (3-10 years)
> Rs.120 for Still Camera
> Rs.600 for Video Camera
""",font="arial 13")
label11.place(relx=0.61,rely=0.48,anchor=E)


label12=Label(window0,text="Click here for",font="arial 15 bold")
label12.place(relx=0.48,rely=0.58,anchor=CENTER)

button1=Button(window0,text="get tickets...!")
button1.place(relx=0.55,rely=0.58,anchor=CENTER)

def open_map(event):
    folder_path = r"D:/1. Python/New folder/Map.jpg"
    # If it's a folder, open the file manager there:
    if platform.system() == "Windows":
        os.startfile(folder_path)
    elif platform.system() == "Darwin":  # macOS
        subprocess.call(["open", folder_path])
    else:  # Linux
        subprocess.call(["xdg-open", folder_path])

label133=Label(window0,text="Zoo Map",font="arial 16 bold")
label133.place(relx=0.80,rely=0.13,anchor=CENTER)

# Hyperlink‐style label for the folder path
link = tk.Label(
    window0,
    text=r"D:/1. Python/New folder/Map.jpg",
    fg="blue",
    cursor="hand2",
    font=("Arial", 12, "underline"),
    bg="#f0f0f0"
)
link.place(relx=0.85,rely=0.18,anchor=CENTER)
link.bind("<Button-1>", open_map)

'''#footer_label=Label(window1,text="Location: Zoological Park,\nVandalur, \nChennai, \nTamil Nadu - 600 048.\nPhone: 044-29542301 \nFax: 044-22750741 \nFor Help & Support \nEmail:Support@zpin",wraplength=250,foreground= "white",background="#333333",font="Arial 10 bold")
#footer_label.pack(side="bottom",fill="x")

footer = tk.Frame(window, bg="#222222", height=80)
footer.pack(side="bottom", fill="x")

# Create style for footer labels (if using ttk)
style = ttk.Style()
style.configure("Footer.TLabel", background="#222222", foreground="white", font=("Arial", 10,"bold"))

# Left label
left_label = ttk.Label(footer, text="Location: Wild Wonder Zoological Park,\nVandalur, Chennai, \nTamil Nadu - 600 048.", style="Footer.TLabel")
left_label.place(relx=0.01, rely=0.5, anchor="w")

# Center label
center_label = ttk.Label(footer, text="Contact us \nPhone: 044-29542301 \nFax: 044-22750741", style="Footer.TLabel")
center_label.place(relx=0.5, rely=0.5, anchor="center")

# Right label
right_label = ttk.Label(footer, text="For Help & Support \nEmail:Support@wildwonderzoologicalpark.in", style="Footer.TLabel")
right_label.place(relx=0.99, rely=0.5, anchor="e")'''

# Second Tab
# Load the video
cap = cv2.VideoCapture("D:/1. Python/New folder/AAPZ_Web.mp4")  # 🔁 Replace with your video file path

'''def show_frame():
    global cap
    ret, frame = cap.read()
    if ret:
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        label1.imgtk = imgtk
        label1.configure(image=imgtk)
        label1.after(10, show_frame)
    else:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Restart video
        show_frame()'''

# Create a label to show video
label13 = Label(window2)
label13.pack()

# Function to update video frame
def show_frame():
    ret, frame = cap.read()
    if ret:
        frame = cv2.resize(frame, (1500, 300))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        label13.imgtk = imgtk
        label13.config(image=imgtk)
        label13.after(15, show_frame)
    else:
        cap.release()

# Start playing video
show_frame()

label114=Label(window2,text="Animal Stock 2024-25",font="arial 16 bold underline")
label114.place(relx=0.5,rely=0.52,anchor=CENTER)

label15=Label(window2,text="Abstract",font="arial 14 underline")
label15.place(relx=0.5,rely=0.57,anchor=CENTER)


table=ttk.Treeview(window2,columns=("Slno","Species","No.Species","No.Specimens"),show="headings")
table.heading("Slno",text="Sl.No.")
table.heading("Species",text="Species")
table.heading("No.Species",text="No.of.Species")
table.heading("No.Specimens",text="No.of.Specimens")
table.place(relx=0.5,rely=0.78,anchor=CENTER)

table.insert(parent="",index=0,values=(1,"Mammals",55,664))
table.insert(parent="",index=1,values=(2,"Birds",97,1227))
table.insert(parent="",index=2,values=(3,"Reptiles",38,341))
table.insert(parent="",index=3,values=(4,"Amphibians",2,8))
table.insert(parent="",index=4,values=(" ","Total",192,2240))

table.column("#1", width=40)  # Set width of first column to 50 pixels
table.column("#2", width=80)
table.column("#3", width=80)
table.column("#4", width=99)


#image4=PhotoImage(file="D:/1. Python/New folder/1.png")
#label16=Label(window2,image=image4)
#label16.place(relx=0.5,rely=0.9,anchor=CENTER)
#label16.grid(row=10,column=3,padx=10,pady=10)

# Path to store user data
USER_FILE = "users.json"

# Load user database
def load_users():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as f:
            return json.load(f)
    return {}

# Save user database
def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f)

user_db = load_users()

def ticket_booking_window():
    window4 = Toplevel()
    window4.title("Zoo Ticket Booking")
    window4.geometry("400x200")
    tk.Label(window4, text="Welcome to the Zoo Ticket Booking Page!", font=("Arial", 14)).pack(pady=30)
    window4.configure(bg="lightgreen")


    # Load image
    bg_image = Image.open("D:/1. Python/New folder/Tiger.png")  # Replace with your image file
    bg_image = bg_image.resize((1550, 900), Image.Resampling.LANCZOS)  # Resize to window size    
    bg_photo = ImageTk.PhotoImage(bg_image)

    # Optional: Dim the background for better contrast
    enhancer = ImageEnhance.Brightness(bg_image)
    bg_image = enhancer.enhance(0.6)

    # Set image as label
    bg_label = tk.Label(window4, image=bg_photo)
    bg_label.image = bg_photo  # Keep a reference
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Header bar
    header_frame = tk.Frame(window4, bg="white")
    header_frame.place(x=0, y=0, relwidth=1)

    image = load_logo("D:/1. Python/New folder/Logo2.png", size=(40, 40))
    logo_label = tk.Label(header_frame, image=image, bg="white")
    logo_label.image = image  # Keep reference
    logo_label.pack(side="left", padx=10, pady=10)

    title = tk.Label(header_frame, text="Wild Wonder Zoological Park", font=("Arial", 18, "bold"), bg="white")
    title.pack(side="left", padx=2)
   
    # Ticket booking form frame
    form_frame = tk.Frame(window4, bg="lightgreen", bd=2, relief="groove")
    form_frame.place(relx=0.5, rely=0.5, anchor="center")


    tk.Label(form_frame, text="Zoo Ticket Booking", font=("Arial", 18, "bold"), bg="lightgreen").pack(pady=20)
    
    tk.Label(form_frame, text="Enter number of tickets:", font=("Arial", 12), bg="lightgreen").pack(pady=5)
    ticket_entry = tk.Entry(form_frame, font=("Arial", 12))
    ticket_entry.pack(pady=5)

    def book_tickets():
        try:
            count = int(ticket_entry.get())
            if count <= 0:
                raise ValueError
            messagebox.showinfo("Booking Confirmed", f"{count} ticket(s) booked successfully!")
            window4.destroy()
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number of tickets.")

    tk.Button(form_frame, text="Book Now", font=("Arial", 12), bg="green", fg="white", command=book_tickets).pack(pady=10)
    tk.Button(form_frame, text="Cancel", font=("Arial", 10), command=window4.destroy).pack(pady=(0, 10))

def login_window():
    def login():
        email = email_entry.get()
        password = password_entry.get()
        if email in user_db and user_db[email] == password:
            messagebox.showinfo("Success", "Login successful!")
            #loginframe.destroy()
            ticket_booking_window()
        else:
            messagebox.showerror("Error", "Invalid credentials.")
    def open_create_account():
        create_account_window()

    login_frame = tk.Frame(window3, bg="#a7c957", width=400, height=480)
    login_frame.place(relx=0.5, rely=0.4, anchor="center")

    label16=Label(login_frame,text="Login",font="Arial 20 bold",background="#a7c957")
    label16.pack(pady=(20, 5))

    label17=Label(login_frame, text="Login to book tickets and submit\nyour queries", background="#a7c957", font="Arial 10", justify="center").pack(pady=(0, 20))


    label18=Label(login_frame, text="Email ID or Mobile Number", font="Arial 10 bold", background="#a7c957", anchor="w").pack(fill="x", padx=30)
    email_entry = Entry(login_frame, font=("Arial", 10))
    email_entry.pack(padx=30, pady=(0, 10), fill="x")

    label19=Label(login_frame, text="Password", font="Arial 10 bold", background="#a7c957", anchor="w").pack(fill="x", padx=30)
    password_entry = Entry(login_frame, show="*", font=("Arial", 10))
    password_entry.pack(padx=30, pady=(0, 10), fill="x")

    # Buttons
    loginbut=tk.Button(login_frame,text="Login",command=login, bg="#E62129", fg="white", font="Arial 11").pack(padx=30, pady=(10, 5), fill="x")

    # Divider
    label18=Label(login_frame, text="────────── OR ──────────", background="#a7c957").pack(pady=5)

    label19=Label(login_frame, text="If you don't have an account ?", background="#a7c957", font="Arial 10").pack()


    Createacc=tk.Button(login_frame, text="Create Account", command=open_create_account, bg="#5A7D9A", fg="white", font=("Arial", 11)).pack(padx=30, pady=(5, 20), fill="x")


def create_account_window():
    def register():
        email2 = email2_entry.get()
        password2 = password2_entry.get()

        if not email2 or not password2:
            messagebox.showwarning("Input error", "All fields are required.")
            return

        if email2 in user_db:
            messagebox.showerror("Error", "Account already exists.")
        else:
            user_db[email2] = password2
            messagebox.showinfo("Success", "Account created successfully!")
            window5.destroy()
            login_window()

    window5 = Toplevel(window)
    window5.title("Create Account")
    window5.geometry("1264x2000")
    window5.configure(bg="lightblue")

    tk.Label(window5, text="Create Account", font=("Arial", 18, "bold"), bg="lightblue").pack(pady=10)

    tk.Label(window5, text="Email or Mobile Number:", bg="lightblue").pack()
    email2_entry = tk.Entry(window5, width=30)
    email2_entry.pack(pady=5)

    tk.Label(window5, text="Password:", bg="lightblue").pack()
    password2_entry = tk.Entry(window5, width=30, show="*")
    password2_entry.pack(pady=5)

    tk.Button(window5, text="Register", command=register, bg="green", fg="white").pack(pady=10)

# Load banner background
banner_image = Image.open("D:/1. Python/New folder/leo.png").resize((1600,350))
banner_photo = ImageTk.PhotoImage(banner_image)
banner_label = tk.Label(window6, image=banner_photo)
banner_label.image = banner_photo
banner_label.pack()

# Overlay Title
title_frame = tk.Frame(window6, bg="#000000", width=1000, height=50)
title_frame.place(relx=0.1, rely=0.25, anchor="center")
tk.Label(title_frame, text="CONTACT US", font=("Arial", 24, "bold"), bg="#000000", fg="white").pack(pady=10)

# Main contact info frame
contact_frame = tk.Frame(window6, bg="white", bd=0.5, relief="solid", padx=30, pady=20)
contact_frame.pack()

# Left Frame - Contact Details
left = tk.Frame(contact_frame, bg="white")
left.grid(row=0, column=3, sticky="nw")

def info(icon, label, value, color="#f4a300"):
    f = tk.Frame(left, bg="white")
    f.pack(anchor="w", pady=1)
    tk.Label(f, text=icon, bg="white").pack(side="left")
    tk.Label(f, text=label, font=("Arial", 10, "bold"), bg="white").pack(side="left")
    tk.Label(f, text=value, font=("Arial", 10), fg=color, bg="white").pack(side="left")

info("📧", " Email: ", "support@aazp.in")
info("📞", " Phone: ", "044 - 29542301")
info("📠", " Fax: ", "044 - 29542301")

# Address
tk.Label(left, text="\n📍 Address:", font=("Arial", 10, "bold"), bg="white").pack(anchor="w")
address = """Wild Wonder Zoological Park,
Grand Southern Trunk Rd, Vandalur,
Chennai, Tamil Nadu - 600048

Enquiry hours: 9.00 AM to 5.00 PM only
Tuesday Holiday"""
tk.Label(left, text=address, bg="white", justify="left").pack(anchor="w", pady=5)

# Social Media Icons
social_frame = tk.Frame(left, bg="white")
social_frame.pack(anchor="w", pady=10)

icons = ["facebook", "instagram", "twitter", "youtube"]
for icon in icons:
    try:
        img = Image.open(f"{icon}.png").resize((24, 24))
        img_tk = ImageTk.PhotoImage(img)
        lbl = tk.Label(social_frame, image=img_tk, bg="white", cursor="hand2")
        lbl.image = img_tk
        lbl.pack(side="left", padx=5)
    except:
        tk.Label(social_frame, text=icon.title(), bg="white").pack(side="left", padx=5)

# Right Frame - Static Map
def open_map():
    webbrowser.open("https://www.google.com/maps/place/Arignar+Anna+Zoological+Park/@12.8801091,80.0783171,17z/data=!3m1!4b1!4m6!3m5!1s0x3a52f604b07fd4cd:0xb2f00bc9eb6c9c86!8m2!3d12.8801091!4d80.080892!16zL20vMDc3Mmp0?entry=ttu&g_ep=EgoyMDI1MDUxMy4xIKXMDSoASAFQAw%3D%3D")

right = tk.Frame(contact_frame, bg="white")
right.grid(row=0, column=1, padx=20)

try:
    map_image = Image.open("D:/1. Python/New folder/location.png").resize((200,200))
    map_photo = ImageTk.PhotoImage(map_image)
    map_label = tk.Label(right, image=map_photo, cursor="hand2")
    map_label.image = map_photo
    map_label.pack()
    map_label.bind("<Button-1>", lambda e: open_map())

    label563=Label(window6,text="Click the above image",background="white",font="Arial 10")
    label563.place(relx=0.42,rely=0.95,anchor=CENTER)
except:
    tk.Label(right, text="[Map Placeholder]", bg="lightgray", width=50, height=20).pack()


login_window()  # Show the login form initially
window.mainloop()  # Start the Tkinter GUI loop
