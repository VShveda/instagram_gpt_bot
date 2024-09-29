# Instagram Profile Parser and Message Generator

This project automates Instagram profile parsing and generates personalized greeting messages based on the profile's bio and photo content. The project uses **Selenium** for scraping Instagram profiles and **Google Gemini API** for object detection in images.

## Features
- **Instagram Login**: Automated login to Instagram using Selenium WebDriver.
- **Profile Parsing**: Scrapes profile data such as full name, bio description, and profile picture.
- **Image Processing**: Detects objects in profile pictures using Google Gemini API.
- **Personalized Message Generation**: Generates a greeting message based on the scraped profile data and detected objects.
- **Environment Variables**: Keeps sensitive data such as Instagram credentials and API keys secure using `.env` files (pay attention to the file `.env.sample`).

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/instagram_gpt_bot.git
    cd instagram_gpt_bot
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv .venv
    source .venv/bin/activate   # For Linux/macOS
    .venv\Scripts\activate      # For Windows
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    Create a `.env` file in the project root and add your Instagram credentials and API keys:
    ```
    INSTAGRAM_USERNAME=your_username
    INSTAGRAM_PASSWORD=your_password
    GEMINI_API_KEY=your_gemini_api_key
    ```
   **Google Gemini Availability**: Please note that the Google Gemini API may not be available in all countries. If you encounter issues with accessing Gemini, you may need to install a VPN and connect to a country where the service is supported.

## Usage

You can run the bot by executing the main.py script. You need to set the target_profile_url to the URL of the Instagram profile you want to scrape. It is important that the URL is in the correct format and that the profile is public.
    
    
    if __name__ == "__main__":
    target_profile_url = "https://www.instagram.com/username/"
    main(target_profile_url)
    

1. **Run the bot**:
    ```bash
    python botAPI/main.py
    ```

    The bot will:
    - Log in to Instagram.
    - Scrape profile info (full name, bio description, and profile image).
    - Detect objects in the profile image using Google Gemini API.
    - Generate a personalized message based on profile data and detected objects.

## Dependencies

- `selenium`: Web scraping library to interact with Instagram.
- `webdriver-manager`: Automatically downloads and manages the ChromeDriver.
- `requests`: To download images from profile links.
- `google-generativeai`: For object detection in profile pictures.

## Important Notes

- **VPN Usage**: When using a VPN, ensure that any cookie consent popups are handled correctly.
- **Instagram Blocking**: Frequent logins or scraping may trigger Instagram's security measures, leading to account temporary suspension. Consider adding delays between actions to minimize this risk.
