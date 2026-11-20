import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"
headers = {"User-Agent": "Mozilla/5.0"}

try:
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    items = soup.select('h2[data-testid="card-headline"]')

    headlines = []

    for item in items:
        title = item.get_text(" ", strip=True)

        if title and title not in headlines:
            headlines.append(title)

        if len(headlines) == 5:
            break

    print("Top 5 BBC News Headlines:\n")

    for i, title in enumerate(headlines, 1):
        print(f"{i}. {title}")

    if len(headlines) < 5:
        print(f"\nOnly {len(headlines)} headlines found.")

except requests.RequestException as error:
    print("Error fetching news:", error)