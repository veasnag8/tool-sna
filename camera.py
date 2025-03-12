import cv2
import requests

# Replace with your actual Telegram bot token
BOT_TOKEN = "7233414815:AAHhlUfOAiD8SLJNRNWlY4SJ_PV3wZf-GhY"

# Step 1: Get the latest updates to find Chat ID
updates_url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"
response = requests.get(updates_url).json()

# Extract the Chat ID (if there are messages)
if "result" in response and response["result"]:
    CHAT_ID = response["result"][-1]["message"]["chat"]["id"]
    print(f"✅ Chat ID found: {CHAT_ID}")

    # Step 2: Capture an image from the webcam
    cap = cv2.VideoCapture(0)  # Open the webcam
    ret, frame = cap.read()
    cap.release()

    if ret:
        image_path = "captured_image.jpg"
        cv2.imwrite(image_path, frame)
        print(f"✅ Image saved: {image_path}")

        # Step 3: Send the image to Telegram
        send_photo_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
        with open(image_path, "rb") as img_file:
            files = {"photo": img_file}
            data = {"chat_id": CHAT_ID}
            response = requests.post(send_photo_url, files=files, data=data)

        if response.status_code == 200:
            print("✅ Image uploaded to Telegram successfully!")
        else:
            print("❌ Upload failed:", response.text)
    else:
        print("❌ Failed to capture image")
else:
    print("❌ No chat ID found. Send a message to your bot first.")