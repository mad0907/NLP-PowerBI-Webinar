import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import string

# Download necessary NLTK data
nltk.download("punkt")
nltk.download("stopwords")

# Example text
text = """
Artificial Intelligence (AI) is a rapidly growing field that focuses on building intelligent machines capable of performing tasks 
that typically require human intelligence. These tasks include learning, reasoning, problem-solving, perception, and language understanding. 
AI has applications across various industries, including healthcare, finance, and transportation. 
As technology evolves, AI is becoming increasingly integral to everyday life.
"""

# Step 1: Tokenize sentences
sentences = sent_tokenize(text)

# Step 2: Tokenize words and calculate word frequencies
stop_words = set(stopwords.words("english"))
words = word_tokenize(text.lower())
words = [word for word in words if word not in stop_words and word not in string.punctuation]

# Count word frequencies
word_frequencies = Counter(words)

# Step 3: Score sentences based on word frequencies
sentence_scores = {}
for sentence in sentences:
    for word in word_tokenize(sentence.lower()):
        if word in word_frequencies:
            if sentence not in sentence_scores:
                sentence_scores[sentence] = word_frequencies[word]
            else:
                sentence_scores[sentence] += word_frequencies[word]

# Step 4: Extract the top N sentences (e.g., 2 sentences for the summary)
summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:2]
summary = " ".join(summary_sentences)

# Print the summary
print("Summary:")
print(summary)
