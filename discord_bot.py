import requests
import discord
import asyncio
from discord.ext import commands

# Your Twitch Client ID and OAuth token
client_id = '*************************'
oauth_token = '*******************'  # Your OAuth token
user_id = '**********'  # Replace this with your actual user ID
discord_token = '********************'  # Replace with your bot token
CHANNEL_ID = #****************   Replace # and *** with your channel ID

# Create an instance of commands.Bot
intents = discord.Intents.default()
intents.messages = True  # This allows your bot to send messages
bot = commands.Bot(command_prefix='!', intents=intents)

async def check_stream():
    url = f'https://api.twitch.tv/helix/streams?user_id={user_id}'
    headers = {
        'Client-ID': client_id,
        'Authorization': f'Bearer {oauth_token}',
    }

    while True:
        # Make the API request
        response = requests.get(url, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            # Check if the user is live
            if data['data']:
                await send_discord_message("You are currently live on Twitch!")
            else:
                print("You are offline.")
        else:
            print(f"Failed to get streams: {response.status_code}, {response.text}")

        await asyncio.sleep(60)  # Check every 60 seconds

async def send_discord_message(content):
    channel = bot.get_channel(CHANNEL_ID)
    if channel is not None:
        await channel.send(content)
    else:
        print("Channel not found.")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')
    # Start the stream checking task
    bot.loop.create_task(check_stream())

# Run the bot
bot.run(discord_token)
