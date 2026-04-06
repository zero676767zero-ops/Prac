from html.parser import HTMLParser
from urllib.request import urlopen
from urllib.parse import urljoin
import json


class LinkParser(HTMLParser):

    def __init__(self):
        super().__init__()
        self.links = []
        self.base_url = ""

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for key, value in attrs:
                if key == "href":
                    full_url = urljoin(self.base_url, value)
                    self.links.append(full_url)

    def extract_links(self, url):
        self.links = []
        self.base_url = url

        try:
            response = urlopen(url)
            content_type = response.getheader("Content-Type")

            if content_type and "text/html" in content_type:
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8", errors="ignore")
                self.feed(html_string)
                response.close()
                return html_string, self.links
            else:
                return "", []

        except Exception as e:
            print("Error opening URL:", url, e)
            return "", []


def crawl(start_url, search_word):
    parser = LinkParser()

    visited_urls = set()
    found_urls = []

    html_data, links = parser.extract_links(start_url)
    links.append(start_url)

    for index, link in enumerate(links, start=1):
        if link in visited_urls:
            continue

        visited_urls.add(link)
        print(f"{index}. Scanning:", link)

        try:
            html_data, _ = parser.extract_links(link)

            if search_word.lower() in html_data.lower():
                print(">>> Word FOUND at:", link)
                found_urls.append(link)
            else:
                print("No match")

        except Exception as e:
            print("Failed:", e)

    # Final Output
    print("\nCrawling Finished")
    print("Total Pages Visited:", len(visited_urls))
    print("URLs containing the word:")
    print(json.dumps(found_urls, indent=2))


# Run crawler
crawl("https://facebook.com", "example")