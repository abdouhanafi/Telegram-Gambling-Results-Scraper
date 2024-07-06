### Description
The Telegram Gambling Results Scraper is a bot developed to collect and analyze gambling results for Champions League and Europa League matches shared in various Telegram channels. This bot efficiently scrapes images and relevant data, storing them in an Excel file for further analysis. The project aims to support educational and research purposes, offering insights into gambling trends and behaviors in sports betting.

This project was developed as part of an academic endeavor at Aalto University in Finland.

### Features
- Scrapes gambling results from specified Telegram channels.
- Collects images and associated data.
- Stores collected data in an Excel file for easy access and analysis.
- Prevents duplication by tracking the last processed message ID.

### Requirements
- Python 3.8+
- Telethon
- Pandas
- OpenCV (for image processing if needed)
- Any other relevant libraries

### Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/abdouhanafi/telegram-gambling-results-scraper.git
   ```
2. **Navigate to the project directory:**
   ```bash
   cd telegram-gambling-results-scraper
   ```
3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Usage
1. **Configure the bot:**
   - Update the configuration settings in `config.py` with your Telegram API credentials and target channel information.

2. **Run the scraper:**
   ```bash
   python telegram_scrap.py
   ```

3. **Analyze the data:**
   - The scraped data will be stored in `telegram_leaked_data.xlsx`. You can open this file using any spreadsheet software for further analysis.

### Files
- `index.py`: Main script or module for the project.
- `telegram_scrap.py`: Script for scraping data from Telegram channels.
- `last_message_ids.json`: JSON file to track the last processed message ID to avoid duplication.
- `telegram_leaked_data.csv`: CSV file storing the collected data.
- `requirements.txt`: List of dependencies required for the project.

### Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

### License
This project is licensed under the MIT License.

### Contact
For any questions or further information, please contact Neima Hlou at abdelfattah.hanafi@aalto.fi.

---

Feel free to modify this README as needed to fit the specific details and structure of your project.
