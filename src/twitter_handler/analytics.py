from collections import Counter
import yake
from typing import List
import pandas as pd


def word_frequency(data: List):
    frequencies = {}

    for item in data:
        for word in item.split():
            if word not in frequencies.keys():
                frequencies[word] = 1
            else:
                frequencies[word] += 1
    return frequencies

def get_keywords(data: List):
    # Initialize keyword list
    keywords_df = pd.DataFrame()
    for text in data:
        # Define yake params
        language = "pt"
        max_ngram_size = 1
        deduplication_threshold = 0.9
        numOfKeywords = 20
        # Create key word extractor
        custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords, features=None)
        # Extract keywords
        keywords = custom_kw_extractor.extract_keywords(text)
        # Append extracted keywords to df
        keywords_df = keywords_df.append(dict(keywords), ignore_index=True)

    # Divide the sum of the kewyword values by the number of times it appears (the smaller the value, the more important it is)
    keywords_sum = (keywords_df.sum() / (keywords_df.count()+1)).to_dict()

    return keywords_sum