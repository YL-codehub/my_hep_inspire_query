import urllib.parse
import webbrowser

# Read the search query from the text file
with open('search_query.txt', 'r') as file:
    # search_query = file.read().strip()
    search_query = file.read().replace('\n', ' ').strip()

# Encode the search query to make it URL-safe
encoded_query = urllib.parse.quote(search_query)

# Construct the full URL
base_url = "https://inspirehep.net/literature?sort=mostrecent&size=25&page=1&q="
full_url = f"{base_url}{encoded_query}"

# Open the URL in the default web browser
webbrowser.open(full_url)
