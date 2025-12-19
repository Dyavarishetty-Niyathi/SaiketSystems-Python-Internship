import requests
from bs4 import BeautifulSoup


def fetch_headlines():
    url = "https://indianexpress.com/"

    try:
        response = requests.get(url)
        response.raise_for_status()  # raises error for bad response

    except requests.exceptions.RequestException as e:
        print(" Error while accessing the website.")
        print(e)
        return

    soup = BeautifulSoup(response.text, "html.parser")

    headlines = soup.find_all("h3")

    if not headlines:
        print(" No headlines found.")
        return

    print("\n TOP NEWS HEADLINES\n")
    print("-" * 40)

    count = 1
    for headline in headlines:
        text = headline.get_text(strip=True)

        if text:
            print(f"{count}. {text}")
            count += 1

        if count > 10:   # show only top 10 headlines
            break


if __name__ == "__main__":
    fetch_headlines()
