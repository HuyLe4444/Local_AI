#plot_sentiment.py
import matplotlib.pyplot as plt

def plot_sentiment_counts(urls, positive_counts, negative_counts, neutral_counts):
    x = range(len(urls))
    plt.figure(figsize=(10, 6))

    bar_width = 0.2

    plt.bar([i - bar_width for i in x], positive_counts, width=bar_width, label='Positive', align='center')
    plt.bar(x, negative_counts, width=bar_width, label='Negative', align='center')
    plt.bar([i + bar_width for i in x], neutral_counts, width=bar_width, label='Neutral', align='center')

    plt.xlabel('Reviews')
    plt.ylabel('Count')
    plt.title('Sentiment Analysis for Each URL')
    plt.xticks(x, urls, rotation='vertical')
    plt.legend()
    plt.tight_layout()
    plt.show()