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

def main():
    try:
        ensure_nltk_data()
        sample_data = "I love learning about AI and machine learning! This is amazing!"
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()