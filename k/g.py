from google import google
num_page = 3
search_results = google.search("david beckham", num_page)
for result in search_results:
    print(result.description)
