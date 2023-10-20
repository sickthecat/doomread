from newsapi import NewsApiClient
from colorama import init, Fore, Style
from datetime import datetime, timedelta

# Replace 'YOUR_API_KEY' with your actual News API key
api_key = '982187f822464e4394e93a8c9e7a21a9'

# Initialize the NewsApiClient
newsapi = NewsApiClient(api_key=api_key)

def get_headlines_for_topics(topics):
    try:
        # Calculate the date 14 days ago from today
        end_date = datetime.now()
        start_date = end_date - timedelta(days=14)

        # Format the dates in the 'YYYY-MM-DD' format
        from_date = start_date.strftime('%Y-%m-%d')
        to_date = end_date.strftime('%Y-%m-%d')

        # Retrieve headlines from Google News for the last 14 days for each topic
        for topic in topics:
            top_headlines = newsapi.get_everything(q=topic, from_param=from_date, to=to_date)

            # Initialize colorama
            init(autoreset=True)

            # Print the headlines, publishing date, and links with colors
            print(f"Headlines for '{topic}':\n")
            for i, article in enumerate(top_headlines['articles'], start=1):
                title = article['title']
                link = article['url']
                published_at = article['publishedAt']

                # Apply colors to the text
                colored_title = f"{Fore.BLUE}{Style.BRIGHT}{title}{Style.RESET_ALL}"
                colored_link = f"{Fore.GREEN}{link}{Style.RESET_ALL}"
                
                # Format the publishing date
                formatted_date = datetime.fromisoformat(published_at[:-1]).strftime('%Y-%m-%d %H:%M:%S')

                # Print the formatted text with the publishing date
                print(f"{i}. {colored_title}\n   Published on: {formatted_date}\n   {colored_link}\n")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    topics = ['tech', 'crypto', 'politics', 'war']
    get_headlines_for_topics(topics)
