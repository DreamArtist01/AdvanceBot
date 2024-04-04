import re
from pyrogram import Client, filters
from AnonXMusic import app
from pyrogram.types import Message


# Delete messages with files
@app.on_message(filters.document & filters.group)
async def delete_file_messages(client, message):
    await client.delete_messages(message.chat.id, message.id)



# Regular expression pattern to match bio links
bio_link_pattern = re.compile(r'(http|https)://[^\s]+')


# Delete messages with bio links
@app.on_message(filters.text & filters.group)
async def delete_bio_link_messages(client, message):
    if bio_link_pattern.search(message.text):
        await client.delete_messages(message.chat.id, message.id)


# Delete messages with photo
@app.on_message(filters.photo & filters.group)
async def delete_photo_messages(client, message):
    await client.delete_messages(message.chat.id, message.id)


# Delete messages with video
@app.on_message(filters.video & filters.group)
async def delete_video_messages(client, message):
    await client.delete_messages(message.chat.id, message.id)



# Delete channel messages
@app.on_message(filters.channel & filters.group)
async def delete_channel_messages(client, message):
    await client.delete_messages(message.chat.id, message.id)


# Delete messages with audio
@app.on_message(filters.audio & filters.group)
async def delete_audio_messages(client, message):
    await client.delete_messages(message.chat.id, message.id)


# Delete messages with forwarded 
@app.on_message(filters.forwarded & filters.group)
async def delete_forwarded_messages(client, message):
    await client.delete_messages(message.chat.id, message.id)


# Delete messages with animation
@app.on_message(filters.animation & filters.group)
async def delete_file_messages(client, message):
    await client.delete_messages(message.chat.id, message.id)



# Delete messages with voice note
@app.on_message(filters.voice & filters.group)
async def delete_voice_messages(client, message):
    await client.delete_messages(message.chat.id, message.id)


# Delete messages with video note
@app.on_message(filters.video_note & filters.group)
async def delete_video_messages(client, message):
    await client.delete_messages(message.chat.id, message.id)



# Regular expression pattern to match links
link_pattern = re.compile(r'(http[s]?:\/\/)?[^\s(["<,>.]+?\.[^\s[">,<.]+')

# Delete messages with links
@app.on_message(filters.text & filters.group)
async def delete_link_messages(client, message):
    if link_pattern.search(message.text):
        await client.delete_messages(message.chat.id, message.id)
