import pywhatkit as whatsapp_kit
import schedule
import time
from typing import List

def send_whatsapp_image(phone_number: str, image_path: str, caption: str) -> None:
    """
    Send a WhatsApp image to a phone number.

    Args:
        phone_number (str): The phone number to send the image to.
        image_path (str): The path to the image to send.
    """
    try:
        whatsapp_kit.sendwhats_image(phone_number, image_path , caption, wait_time=15, tab_close=True)
    except Exception as e:
        print(f"Failed to send message to {phone_number}: {str(e)}")

def send_images_to_multiple_numbers(numbers: List[str], image_path: str,caption: str) -> None:
    """
    Send a WhatsApp image to multiple phone numbers.

    Args:
        numbers (List[str]): A list of phone numbers to send the image to.
        image_path (str): The path to the image to send.
    """
    for number in numbers:
        send_whatsapp_image(number, image_path,caption)

# List of phone numbers in the format "+[Country Code][Phone Number]"
phone_numbers = [
    "+918610068479", "+919465168486"
]

# Caption to send with the image
caption = "This is my first WhatsApp Automation text"

# Path to the image
image_path = "img.jpg"

# Time to send the message (24-hour format)
send_hour = 10  # 6 PM
send_minute = 37 # 30 minutes past the hour


 
# Schedule the image sending
schedule.every().day.at(f"{send_hour:02d}:{send_minute:02d}").do(
    send_images_to_multiple_numbers, phone_numbers, image_path,caption)

while True:
    schedule.run_pending()
    time.sleep(1)