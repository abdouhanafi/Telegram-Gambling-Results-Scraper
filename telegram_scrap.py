from telethon import TelegramClient
import csv
import os
import json
from datetime import datetime
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.types import MessageMediaPhoto

# Replace these with your own values
api_id = '24167225'
api_hash = '2bc9300d5f9215a133320bd000362cac'
phone_number = '+212610622143'

# List of target channels
target_channels = ['predictions_1xbet']    # Add the usernames of target channels

# Create the client and connect
client = TelegramClient('anon', api_id, api_hash)

# Load the last message IDs
if os.path.exists('last_message_ids.json'):
    with open('last_message_ids.json', 'r') as f:
        last_message_ids = json.load(f)
else:
    last_message_ids = {channel: 0 for channel in target_channels}

async def main():
    # Connect to the client
    await client.start(phone_number)

    # Join the target channels
    for channel in target_channels:
        await client(JoinChannelRequest(channel))

    # Prepare the CSV file
    today = datetime.now().strftime("%Y-%m-%d")
    csv_filename = f'telegram_leaked_data.csv'
    file_exists = os.path.isfile(csv_filename)

    try:
        with open(csv_filename, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            # Write the header only if the file does not exist
            if not file_exists:
                writer.writerow(['Channel', 'Sender ID', 'Date', 'Message', 'Image Path'])

            # Get today's date
            today_date = datetime.now().date()

            # Directory to save images
            images_dir = f'images'
            if not os.path.exists(images_dir):
                os.makedirs(images_dir)

            # Fetch and save messages from each channel
            for channel in target_channels:
                async for message in client.iter_messages(channel, min_id=last_message_ids.get(channel, 0) + 1):
                    if message.date.date() == today_date:
                        image_path = None
                        if isinstance(message.media, MessageMediaPhoto):
                            image_path = os.path.join(images_dir, f'{message.id}.jpg')
                            await message.download_media(image_path)
                            image_path = "/images/" + str(message.id) + ".jpg"

                        writer.writerow([channel, message.sender_id, message.date, message.message, image_path])
                        last_message_ids[channel] = max(last_message_ids.get(channel, 0), message.id)
        with open('last_message_ids.json', 'w') as f:
            json.dump(last_message_ids, f)
    except PermissionError:
        print(f"Permission denied: '{csv_filename}'. Make sure the file is not open in another program and you have the right permissions.")

with client:
    client.loop.run_until_complete(main())
