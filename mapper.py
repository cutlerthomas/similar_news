#!/bin/python3

import contractions
import itertools
import json
import nltk
from nltk.corpus import stopwords
import re
import sys
from urllib.parse import urlparse

shingle_size = 3
nltk.download('stopwords')
sw = stopwords.words('english')


def get_root_domain(url):
    """Extract the root domain from a URL or fallback to the original string."""
    try:
        parsed_url = urlparse(url)
        domain = parsed_url.netloc  # Extract the domain (e.g., 'www.bbc.com')
        if domain:
            return domain.replace('www.', '')  # Remove 'www.' if present
    except Exception:
        pass  # If parsing fails, do nothing

    # Fallback to the original source if URL parsing fails
    return url if url else "Unknown"

for line in sys.stdin:
    articles = json.loads(line)
    for article in articles:
        text = article.get('content') or article.get('Content').lower().strip()
        tokens = contractions.fix(text).split()
        cleaned_tokens = [re.sub(r'[^\w\s]', ' ', token).strip() for token in tokens if re.sub(r'[^\w\s]', '', token)]
        compacted_tokens = [word for word in cleaned_tokens if word.strip()]
        filtered_tokens = [word for word in compacted_tokens if word not in sw]
        text = ' '.join(filtered_tokens)
        raw_source = article.get('Source') or article.get('page') or article.get('source', 'Unknown')
        source = get_root_domain(raw_source)
        print(f"{source}:::{text}")