
import requests
from bs4 import BeautifulSoup


def extract_data(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract links from the landing page
    links = [link.get("href") for link in soup.find_all("a")]

    # Extract titles and descriptions from articles
    articles = soup.find_all("article")
    extracted_data = []
    for article in articles:
        # Check if the article contains a header and a paragraph
        title_element = article.find("h2")
        description_element = article.find("p")

        # If both title and description are found, extract them
        if title_element and description_element:
            title = title_element.text.strip()
            description = description_element.text.strip()
            extracted_data.append({"title": title, "description": description})

    return links, extracted_data


if __name__ == "__main__":
    bbc_url = "https://www.bbc.com/"
    dawn_url = "https://www.dawn.com/"

    bbc_links, bbc_data = extract_data(bbc_url)
    dawn_links, dawn_data = extract_data(dawn_url)

    print("BBC Links:", bbc_links)
    print("BBC Data:")
    for item in bbc_data:
        print("Title:", item["title"])
        print("Description:", item["description"])
        print("--------------------")

    print("\nDawn Links:", dawn_links)
    print("Dawn Data:")
    for item in dawn_data:
        print("Title:", item["title"])
        print("Description:", item["description"])
        print("--------------------")





