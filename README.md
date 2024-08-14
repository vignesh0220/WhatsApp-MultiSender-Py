# WhatsApp-MultiSender-Py

This Python script automates the process of sending WhatsApp messages, including images, to multiple recipients at a scheduled time. The script uses the `pywhatkit` library to interact with WhatsApp Web and `schedule` to manage the timing of message delivery.

## Features

- Send images with captions to multiple WhatsApp numbers.
- Automatically handle numbers that may not be registered on WhatsApp.
- Schedule messages to be sent at a specific time.
- Simple and customizable script.

## Requirements

- Python 3.x
- An active WhatsApp Web session on your default web browser.

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/WhatsApp-MultiSender-Py.git

   ```

2. Navigate to the project directory:

   cd WhatsApp-MultiSender-Py

3. Install the required Python libraries:

   pip install pywhatkit schedule

# Usage

Prepare the List of Phone Numbers:

1. Create a list of phone numbers you want to send the message to. Ensure the numbers include the country code, formatted as +[Country Code][Phone Number].

2. Set the Image Path and Caption:
   Specify the path to the image you want to send and the caption for the image in the script.

3. Set the Scheduled Time:
   Define the time you want the messages to be sent in 24-hour format (e.g., 18:30 for 6:30 PM).

4. Run the Script:
   Run the script using Python:
   python your_script_name.py

5. Monitor the Output:

The script will log the success or failure of each message sent. Any errors, such as numbers not being on WhatsApp, will be displayed in the console.

- Important Notes
  ->WhatsApp Web: Ensure you are logged into WhatsApp Web on your default browser before running the script.
  =>Timing: The script uses your local machine's time for scheduling.
  =>Browser Management: The script keeps the browser tab open after sending the message to avoid reopening it repeatedly.
  =>Error Handling: The script handles errors such as numbers not being registered on WhatsApp and will log these
  errors in the console.

License
This project is licensed under the MIT License. See the LICENSE file for details.
