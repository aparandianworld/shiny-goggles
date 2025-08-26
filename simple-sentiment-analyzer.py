#!/usr/bin/env python3

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import sys

def ensure_nltk_data():
    try:
        nltk.data.find('sentiment/vader_lexicon')
    except LookupError:
        print("Downloading vader_lexicon...")
        nltk.download('vader_lexicon')
        
def analyze_sentiment(text):
    try: 
        s = SentimentIntensityAnalyzer()
        scores = s.polarity_scores(text)
        return scores
    except Exception as e:
        print(f"Error analyzing sentiment: {e}")
        return None

def main():
    try:
        ensure_nltk_data()
        sample_data = "I love learning about AI and machine learning! This is amazing!"
        scores = analyze_sentiment(sample_data)
        print(f"Sentiment scores: {scores}")
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()