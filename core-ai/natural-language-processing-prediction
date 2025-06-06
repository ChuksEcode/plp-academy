# Import necessary libraries:
import nltk                                # For natural language processing tasks.
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download the VADER lexicon, needed by the SentimentIntensityAnalyzer.
nltk.download('vader_lexicon')

# Initialize the sentiment analyzer.
sid = SentimentIntensityAnalyzer()         # VADER is optimized for social media text and other short texts.

# Define a sample text.
text = "I absolutely loved the new design of the application. It is magnificent!"

# Compute sentiment scores.
scores = sid.polarity_scores(text)
# polarity_scores returns a dictionary with sentiment keys: 'neg', 'neu', 'pos', and 'compound'.

# Print the sentiment scores.
print("Sentiment Scores:", scores)