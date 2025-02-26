import requests
from bs4 import BeautifulSoup

def scrape_amazon_reviews(url):
    print(f"Fetching URL: {url}")  # Debugging line

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    
    print(f"Response Status Code: {response.status_code}")  # Debugging line
    if response.status_code != 200:
        print("Failed to fetch page")
        return []
    
    soup = BeautifulSoup(response.text, "html.parser")
    print("Page content parsed successfully")  # Debugging line

    reviews = []
    for review in soup.find_all("span", {"data-hook": "review-body"}):
        text = review.get_text(strip=True)
        reviews.append(text)
    
    print(f"Extracted {len(reviews)} reviews")  # Debugging line
    return reviews

# Test the function
if __name__ == "__main__":
    url = "https://amzn.in/d/acC95Xh"
    reviews = scrape_amazon_reviews(url)
    print("Reviews:", reviews)
