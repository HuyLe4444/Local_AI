import requests
from bs4 import BeautifulSoup

def read_urls(filename):
    """
    Read URLs from an input file and return them as a list.
    
    Args:
        filename (str): Path to the input file containing URLs
        
    Returns:
        list: List of URLs with whitespace stripped
    """
    with open(filename, 'r') as file:
        urls = file.readlines()
    return [url.strip() for url in urls]

def write_reviews(all_product_reviews, filename):
    """
    Write collected reviews to an output file.
    
    Args:
        all_product_reviews (list): List of lists containing reviews for each product
        filename (str): Path to the output file where reviews will be written
    """
    with open(filename, 'w', encoding='utf-8') as file:
        for product_num, reviews in enumerate(all_product_reviews, 1):
            file.write(f"Review #{product_num}:\n")
            for review in reviews:
                file.write(f"{review}\n\n")
            file.write("------------------------------------" + "\n\n")
def main():
    # Set up headers for request
    # This helps prevent the request from being blocked by websites
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    # List to store reviews from all products
    all_product_reviews = []
    
    # Read URLs from file
    urls = read_urls('input.txt')
    
    # Get reviews from each URL
    for url in urls:
        # Current product review store here
        product_reviews = []
        
        # Request HTML from URL then parse it
        r = requests.get(url, headers=header)
        soup = BeautifulSoup(r.content, "html.parser")
        
        # Find review container
        reviews_list = soup.find('ul', class_='reviews-list')
        if reviews_list:
            # Get every review inside that container
            reviews = reviews_list.find_all('li', class_='review-item-simple')
            for review in reviews:
                # Just get the text from paragraph element then add to array
                review_text = review.find('p', class_='pre-white-space').text.strip()
                product_reviews.append(review_text)
        
        # Add reviews from current product to main list
        all_product_reviews.append(product_reviews)
    
    # Write all reviews to file
    write_reviews(all_product_reviews, 'output.txt')
    

if __name__ == "__main__":
    main()