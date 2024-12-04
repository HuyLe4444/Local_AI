#get_review.py
import requests
from bs4 import BeautifulSoup
import os
from response_generator import GetResponse

class GetReview:
    def __init__(self, url, header = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"):
        self.header = {
            "User-Agent": header
        }
        
        self.url = url
        self.all_product_reviews = []
    
    def fetch_review(self):
        self.all_product_reviews = self._get_review(self.url)
    
    def _get_review(self, url):
        product_reviews = []
        r = requests.get(url, headers=self.header)
        soup = BeautifulSoup(r.content, "html.parser")
        
        # print(soup)

        reviews_list = soup.find('ul', class_='reviews-list')
        if reviews_list:
            reviews = reviews_list.find_all('li', class_='review-item')
            for review in reviews:
                review_text = review.find('p', class_='pre-white-space').text.strip()
                # print(review_text)
                product_reviews.append(review_text)
        
        # print(product_reviews)
        return product_reviews
    
    def write_reviews(self, url_num, output_folder):
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        file_path = os.path.join(output_folder, f"reviews_{url_num}.txt")
        with open(file_path, 'w', encoding='utf-8') as file:
            for review in self.all_product_reviews:
                single_line_review = ' '.join(review.split())
                file.write(f"{single_line_review}\n\n")
                # file.write("------------------------------------\n\n")


