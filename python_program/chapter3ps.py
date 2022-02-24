# from googlesearch import search
# import requests
# from bs4 import BeautifulSoup


# def google_search(query):
#     results = search(query, num_results=10)
#     return results

# # Example usage
# urls = google_search("BeautifulSoup in python")
# def scrape_data(url):
#     # Fetch the web page
#     response = requests.get(url)
    
#     # Check if the request was successful
#     if response.status_code == 200:
#         # Parse the HTML content
#         soup = BeautifulSoup(response.content, 'html.parser')
        
#         # Extract specific data
#         # Example: Extracting all the paragraph text
#         paragraphs = soup.find_all('p')
#         for para in paragraphs:
#             print(para.get_text())

            
#     else:
#         print(f"Failed to retrieve the content from {url}")

# # Loop through each URL and scrape data
# # for url in urls:
# #     print(url)
# #     # scrape_data(url)

# scrape_data("https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/")
import pyttsx3
import os

def text_to_speech(text, output_path):
    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()
    
    # Set properties (optional)
    engine.setProperty('rate', 150)    # Speed percent (can go over 100)
    engine.setProperty('volume', 1.0)  # Volume 0-1
    
    # Convert text to speech
    engine.save_to_file(text, output_path)
    
    # Run the engine (unnecessary if save_to_file is used)
    engine.runAndWait()

# Example usage
if __name__ == "__main__":
    text = "Hello, this is a sample text to convert into speech."
    output_path = "output.wav"
    text_to_speech(text, output_path)
    print(f"Speech saved to {output_path}")
