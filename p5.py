def compute_pagerank(graph, damping_factor=0.85, iterations=3):
    # Get all pages (nodes)
    pages = list(graph.keys())
    total_pages = len(pages)

    # Initialize PageRank (equal probability)
    page_rank = {page: 1 / total_pages for page in pages}
    print("Initial PageRank:", page_rank)

    # Iterate to update PageRank
    for iteration in range(1, iterations + 1):
        new_page_rank = {page: 0 for page in pages}

        # Distribute rank scores
        for page in pages:
            outgoing_links = graph[page]

            # If page has outgoing links
            if len(outgoing_links) > 0:
                share = page_rank[page] / len(outgoing_links)
                for linked_page in outgoing_links:
                    new_page_rank[linked_page] += share
            else:
                # Handle dangling node (no outgoing links)
                share = page_rank[page] / total_pages
                for p in pages:
                    new_page_rank[p] += share

        # Apply damping factor
        for page in pages:
            new_page_rank[page] = (
                (1 - damping_factor) / total_pages +
                damping_factor * new_page_rank[page]
            )

        page_rank = new_page_rank

        print(f"\nAfter iteration {iteration}:")
        for page in sorted(page_rank):
            print(f"{page}: {page_rank[page]:.4f}")

    return page_rank


# Example graph
web_graph = {
    'A': ['B', 'C'],
    'B': ['C'],
    'C': ['A'],
    'D': ['C']
}

# Run PageRank
final_ranks = compute_pagerank(web_graph, damping_factor=0.85, iterations=3)

print("\nFinal PageRank:")
for page in sorted(final_ranks):
    print(f"{page}: {final_ranks[page]:.4f}")