import requests
import joblib

# Google Drive file ID (get from the shared link)
file_id = '1uIxoKi1Rb2vjA-rWhbK5dAaYIALG6lk7'

# URL to download the file
download_url = f"https://drive.google.com/uc?id={file_id}&export=download"

# Download the .pkl file from Google Drive
response = requests.get(download_url, allow_redirects=True)

# Save the file locally
with open('subscription_model.pkl', 'wb') as f:
    f.write(response.content)

# Load the model
model = joblib.load('subscription_model.pkl')

# You can now use the 'model' variable to make predictions
