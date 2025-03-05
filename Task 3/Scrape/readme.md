# Twitter Data Scraping Script

This Python script scrapes tweet data from the **@CommBank** Twitter account using **Twitter API v2** and saves it to a CSV file for further analysis. It handles rate limits gracefully and ensures secure handling of sensitive information like API tokens.

---

## **Features**
- Fetches tweets, likes, retweets, replies, hashtags, and mentions.
- Handles Twitter API rate limits using exponential backoff.
- Saves data to a structured CSV file (`commbank_tweets_v2.csv`).
- Secure handling of the Bearer Token using environment variables.

---

## **Prerequisites**
1. **Twitter Developer Account**:
   - Create a [Twitter Developer Account](https://developer.twitter.com/) and obtain a **Bearer Token** for API access.
   
2. **Python Libraries**:
   Install the required libraries using pip:
   ```bash
   pip install tweepy pandas python-dotenv
   ```
## **Setup**
**Clone this repository:**

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   Create a .env file in the root directory and add your Bearer Token:
   ```
   ```bash
   # .env
   BEARER_TOKEN=your_bearer_token_here
   Run the script:
   ```
   ```bash
   python app.py
   ```

## Script Workflow

1. **Authentication**:
   - The script authenticates with Twitter API v2 using the Bearer Token stored in the `.env` file.

2. **Rate Limit Handling**:
   - Implements exponential backoff to handle Twitter API rate limits.

3. **Fetching User ID**:
   - Retrieves the user ID for the @CommBank account.

4. **Scraping Tweets**:
   - Fetches tweets from the @CommBank account, including metrics like likes, retweets, and replies.

5. **Processing Tweet Data**:
   - Extracts relevant data (e.g., hashtags, mentions) and stores it in a structured format.

6. **Saving Data**:
   - Saves the collected data to a CSV file (`commbank_tweets_v2.csv`).

**Output**
The script generates a CSV file (commbank_tweets_v2.csv) with the following columns:

created_at: Timestamp of the tweet.

tweet_id: Unique ID of the tweet.

text: Content of the tweet.

likes: Number of likes.

retweets: Number of retweets.

replies: Number of replies.

hashtags: List of hashtags in the tweet.

mentions: List of mentioned users.

**Usage**
Replace the BEARER_TOKEN placeholder in the .env file with your actual Twitter API Bearer Token.

Run the script:

   ```bash
   python app.py
   ```
The output CSV file (commbank_tweets_v2.csv) will be saved in the same directory as the script.

**Security**
Never share your Bearer Token. The .env file is excluded from version control using .gitignore.

If collaborating, share a .env.example file without sensitive data:

   ```bash
   # .env.example
   BEARER_TOKEN=your_bearer_token_here
   ```
**Contributing**
Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License
This project is licensed under the [MIT License](https://github.com/your-username/your-repo-name/blob/main/LICENSE). See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- **[Tweepy](https://github.com/tweepy/tweepy)**: Python library for accessing the Twitter API.
- **[Twitter API v2](https://github.com/twitterdev/twitter-api-typescript-sdk)**: Official Twitter API documentation and SDKs.

