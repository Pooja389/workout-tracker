# workout-tracker
Track your daily exercise activities using the Nutritionix API and automatically log them in Google Sheets with this Python script.
# Exercise Tracker API Integration

## Requirements:
1. **Python 3.x** - Ensure that you have Python installed on your system.
2. **Requests** - To interact with APIs.
3. **python-dotenv** - To load environment variables from a `.env` file.
4. **Google Sheets API credentials** - You need a Google API key and sheet access.
5. **Nutritionix API credentials** - You need an API ID and key from Nutritionix.

## Installation Instructions:

1. **Install dependencies:**

   Run the following command in your terminal to install the required Python libraries:
   ```bash
   pip install requests python-dotenv
## Set up environment variables:
   Create a .env file in the root directory of your project and add your credentials. For example:
   api_id=your_nutritionix_api_id
   api_key=your_nutritionix_api_key
   sheet_url=your_google_sheets_api_url
   auth=your_google_sheets_auth_token
## Run the script and enter the details of your exercise when prompted:
   python workout.py


