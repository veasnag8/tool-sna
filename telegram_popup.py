import requests
import time
import tkinter as tk
from tkinter import messagebox
import io
from PIL import Image, ImageTk

# Replace with your Telegram bot token
BOT_TOKEN = "7233414815:AAHhlUfOAiD8SLJNRNWlY4SJ_PV3wZf-GhY"
# This offset ensures we process only new updates
offset = 0

def get_updates(offset):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates?offset={offset}"
    try:
        response = requests.get(url, timeout=10)
        return response.json()
    except Exception as e:
        print("Error fetching updates:", e)
        return None

def popup_text(message):
    # Display a text pop-up using Tkinter
    root = tk.Tk()
    root.withdraw()  # Hide main window
    messagebox.showinfo("Hacker", message)
    root.destroy()

def popup_image(image):
    # Create a new window to display an image
    window = tk.Tk()
    window.title("New Telegram Photo")
    # Convert PIL image to a Tkinter-compatible image
    tk_image = ImageTk.PhotoImage(image)
    label = tk.Label(window, image=tk_image)
    label.image = tk_image  # Keep a reference!
    label.pack()
    # Run the window's event loop (user must close the window)
    window.mainloop()

def popup_video_message(video_filename):
    # Inform the user that a video was received and saved locally
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("New Telegram Video", f"Video received and saved as:\n{video_filename}")
    root.destroy()

print("Starting Telegram media pop-up receiver...")
print("Waiting for new messages...")

while True:
    data = get_updates(offset)
    if data and data.get("ok") and data.get("result"):
        for update in data["result"]:
            # Update the offset so this update is not processed again
            offset = update["update_id"] + 1
            msg_data = update.get("message", {})

            # If it's a text message
            if "text" in msg_data:
                text = msg_data["text"]
                print("Received text message:", text)
                popup_text(text)

            # If the message contains a photo
            elif "photo" in msg_data:
                print("Received a photo message.")
                # Telegram returns several sizes; take the largest one (last in the list)
                photo_sizes = msg_data["photo"]
                file_id = photo_sizes[-1]["file_id"]
                file_info = requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/getFile?file_id={file_id}").json()
                file_path = file_info["result"]["file_path"]
                photo_url = f"https://api.telegram.org/file/bot{BOT_TOKEN}/{file_path}"
                photo_data = requests.get(photo_url).content
                try:
                    image = Image.open(io.BytesIO(photo_data))
                    popup_image(image)
                except Exception as e:
                    print("Error displaying photo:", e)

            # If the message contains a video
            elif "video" in msg_data:
                print("Received a video message.")
                video = msg_data["video"]
                file_id = video["file_id"]
                file_info = requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/getFile?file_id={file_id}").json()
                file_path = file_info["result"]["file_path"]
                video_url = f"https://api.telegram.org/file/bot{BOT_TOKEN}/{file_path}"
                video_data = requests.get(video_url).content
                video_filename = "received_video.mp4"
                try:
                    with open(video_filename, "wb") as f:
                        f.write(video_data)
                    popup_video_message(video_filename)
                except Exception as e:
                    print("Error saving video:", e)
    else:
        print("No new updates.")
    # Poll every 5 seconds (adjust as needed)
    time.sleep(5)