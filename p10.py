import csv
import requests
import xml.etree.ElementTree as ET
import networkx as nx
import matplotlib.pyplot as plt


# 1. Load RSS feed
def load_rss(url, file_name):
    response = requests.get(url)

    if response.status_code == 200:
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"RSS feed saved as '{file_name}'")
    else:
        print("Failed to fetch RSS feed")


# 2. Parse XML
def parse_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    news_items = []
    allowed_fields = {'guid', 'title', 'pubDate', 'description', 'link'}

    for item in root.findall('.//item'):
        news = {}

        for child in item:
            tag = child.tag.split('}')[-1]  # remove namespace

            if tag in allowed_fields:
                news[tag] = child.text

            # Optional media
            if tag == 'content' and 'url' in child.attrib:
                news['media'] = child.attrib['url']

        news_items.append(news)

    return news_items


# 3. Save to CSV (Excel)
def save_to_csv(news_items, file_name):
    fields = ['guid', 'title', 'pubDate', 'description', 'link', 'media']

    with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(news_items)

    print(f"Data saved to '{file_name}' (can open in Excel)")


# 4. Generate Web Graph
def generate_web_graph(news_items):
    graph = nx.DiGraph()

    source_node = "RSS Feed"
    graph.add_node(source_node)

    for item in news_items:
        title = item.get('title', 'Unknown Article')
        link = item.get('link', '')

        graph.add_node(title)
        graph.add_edge(source_node, title)

        if link:
            graph.add_node(link)
            graph.add_edge(title, link)

    return graph


# 5. Plot Graph
def plot_graph(graph):
    plt.figure(figsize=(12, 8))

    pos = nx.spring_layout(graph, k=0.5, seed=42)

    nx.draw(
        graph,
        pos,
        with_labels=True,
        node_size=1500,
        node_color="lightblue",
        font_size=8,
        edge_color="gray",
        arrows=True
    )

    plt.title("Web Graph from RSS Feed")
    plt.show()


# Main function
def main():
    rss_url = "https://feeds.feedburner.com/50WordStories"
    xml_file = "rss_feed.xml"
    csv_file = "news_data.csv"

    load_rss(rss_url, xml_file)

    news_items = parse_xml(xml_file)

    save_to_csv(news_items, csv_file)

    graph = generate_web_graph(news_items)

    plot_graph(graph)


if __name__ == "__main__":
    main()