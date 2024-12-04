# main.py
from get_review import GetReview
from response_generator import GetResponse
from plot_sentiment import plot_sentiment_counts
import os
import matplotlib.pyplot as plt

response_analyzer = GetResponse()

# Initialize lists to store sentiment counts for each URL
urls = []
positive_counts = []
negative_counts = []
neutral_counts = []

with open('input.txt', 'r') as f:
    url_num = 0
    for url in f:
        url = url.strip()
        print(f"Processing URL: {url}")
        review = GetReview(url)
        review.fetch_review()
        
        positive_count = 0
        negative_count = 0
        neutral_count = 0
        
        for i, review_text in enumerate(review.all_product_reviews):
            sentiment = response_analyzer.analyze_review(review_text)
            review.all_product_reviews[i] = f"{review_text} (Sentiment: {sentiment})"
            
            if sentiment == 'positive':
                positive_count += 1
            elif sentiment == 'negative':
                negative_count += 1
            else:
                neutral_count += 1
        
        review.write_reviews(url_num, 'output')
        url_num += 1
        
        # Store the counts for plotting
        urls.append(f"review_{url_num - 1}")
        positive_counts.append(positive_count)
        negative_counts.append(negative_count)
        neutral_counts.append(neutral_count)
        
        print(f"URL: {url}")
        print(f"Positive: {positive_count}, Negative: {negative_count}, Neutral: {neutral_count}")
        print("-" * 40)

plot_sentiment_counts(urls, positive_counts, negative_counts, neutral_counts)