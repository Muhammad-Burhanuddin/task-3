import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the website you want to scrape
url = 'https://www.digitalvidya.com/blog/article-submission-sites/'

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all article titles and URLs
    articles = []
    for article in soup.find_all('article'):
        title_tag = article.find('h2')  # Assuming article titles are within <h2> tags
        if title_tag:  # Ensure the tag was found
            title = title_tag.text.strip()
        else:
            title = 'No title found'  # Or use a placeholder or skip this article
        
        link_tag = article.find('a')
        if link_tag and 'href' in link_tag.attrs:
            link = link_tag['href']
        else:
            link = 'No URL found'  # Or handle it as necessary
        
        articles.append({'Title': title, 'URL': link})
    
    # Convert the list of articles into a DataFrame
    df = pd.DataFrame(articles)
    
    # Save the DataFrame to a CSV file
    df.to_csv('articles.csv', index=False)
    
    print("Data successfully scraped and saved to articles.csv")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
