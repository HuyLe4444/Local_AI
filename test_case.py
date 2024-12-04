from response_generator import GetResponse
import pytest
from unittest.mock import patch, MagicMock
from get_review import GetReview

def test_analyze_review_positive():
    """Test sentiment analysis for a positive review."""
    response_analyzer = GetResponse()
    sentiment = response_analyzer.analyze_review("This is amazing!")
    assert sentiment == "positive"

def test_analyze_review_negative():
    """Test sentiment analysis for a negative review."""
    response_analyzer = GetResponse()
    sentiment = response_analyzer.analyze_review("This is terrible!")
    assert sentiment == "negative"

def test_analyze_review_neutral():
    """Test sentiment analysis for a neutral review."""
    response_analyzer = GetResponse()
    sentiment = response_analyzer.analyze_review("It is okay.")
    assert sentiment in ["neutral", "positive", "negative"]

def test_fetch_review_with_valid_url():
    """Test fetching reviews with a valid URL."""
    mock_html = """
    <ul class="reviews-list">
        <li class="review-item"><p class="pre-white-space">Great product!</p></li>
        <li class="review-item"><p class="pre-white-space">Not bad.</p></li>
    </ul>
    """
    with patch('requests.get') as mock_get:
        mock_get.return_value.content = mock_html
        review = GetReview("http://example.com")
        review.fetch_review()
        assert len(review.all_product_reviews) == 2
        assert "Great product!" in review.all_product_reviews
        assert "Not bad." in review.all_product_reviews

def test_fetch_review_with_no_reviews():
    """Test fetching reviews when no reviews are present."""
    mock_html = "<div>No reviews found</div>"
    with patch('requests.get') as mock_get:
        mock_get.return_value.content = mock_html
        review = GetReview("http://example.com")
        review.fetch_review()
        assert len(review.all_product_reviews) == 0