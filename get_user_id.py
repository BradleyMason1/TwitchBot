import requests

# Your Client ID and OAuth token
client_id = '******************'  # Enter your client id
oauth_token = '*****************'  # Enter Your OAuth token

# Twitch API endpoint to get user info
url = 'https://api.twitch.tv/helix/users'

# Set the headers with your Client ID and OAuth token
headers = {
    'Client-ID': client_id,
    'Authorization': f'Bearer {oauth_token}',
}

# Make the API request
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    print("User ID:", data['data'][0]['id'])  # Print your user ID
else:
    print(f"Failed to get user info: {response.status_code}, {response.text}")
