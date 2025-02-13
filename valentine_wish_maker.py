import tkinter as tk
from tkinter import messagebox

# Function to handle the "Send" button click
def send_wish():
    crush_name = entry_name.get()
    custom_message = text_message.get("1.0", tk.END).strip()

    if not crush_name or not custom_message:
        messagebox.showwarning("Oops!", "Please enter your crush's name and a message!")
    else:
        # Display a fun confirmation message
        messagebox.showinfo("Sent!", f"Your Valentine's wish to {crush_name} has been sent! 💌\n\nMessage: {custom_message}")

# Create the main window
app = tk.Tk()
app.title("Valentine Wish Maker")
app.geometry("400x300")
app.configure(bg="#ffcccb")  # Light pink background

# Label for crush's name
label_name = tk.Label(app, text="Enter Your Crush's Name:", bg="#ffcccb", fg="#8b0000", font=("Arial", 12))
label_name.pack(pady=10)

# Entry field for crush's name
entry_name = tk.Entry(app, font=("Arial", 12))
entry_name.pack(pady=5)

# Label for custom message
label_message = tk.Label(app, text="Write Your Valentine's Wish:", bg="#ffcccb", fg="#8b0000", font=("Arial", 12))
label_message.pack(pady=10)

# Text box for custom message
text_message = tk.Text(app, height=5, width=40, font=("Arial", 12))
text_message.pack(pady=5)

# Send button
send_button = tk.Button(app, text="Send Wish 💘", command=send_wish, bg="#ff1493", fg="white", font=("Arial", 14))
send_button.pack(pady=20)

# Run the app
app.mainloop()
