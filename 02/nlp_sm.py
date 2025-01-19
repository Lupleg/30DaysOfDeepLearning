import nltk
import ssl
import certifi
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Use certifi certificates
ssl._create_default_https_context = ssl._create_unverified_context

# Download necessary NLTK data files
nltk.download('punkt')
nltk.download('stopwords')

# Sample text
text = "Natural language processing (NLP) is a field of artificial intelligence."

# Tokenize the text
tokens = word_tokenize(text)
print("Tokens:", tokens)

# Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
print("Filtered Tokens:", filtered_tokens)