import re
import pandas as pd
from urllib.parse import urlparse

def extract_features(url):
    """Extracts features from a given URL."""
    parsed_url = urlparse(url)
    
    features = {
        "url_length": len(url),
        "num_dots": url.count('.'),
        "num_hyphens": url.count('-'),
        "num_underscores": url.count('_'),
        "num_slashes": url.count('/'),
        "num_digits": sum(c.isdigit() for c in url),
        "contains_ip": bool(re.match(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$", parsed_url.netloc)),
        "https": 1 if url.startswith("https") else 0
    }
    
    return features

if __name__ == "__main__":
    test_url = "http://example.com"
    print(extract_features(test_url))
