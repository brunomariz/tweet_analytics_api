from collections import Counter
import yake
from typing import List
import pandas as pd
import nltk


def word_frequency(data: List):
    frequencies = {}

    for item in data:
        for word in item.split():
            if word not in frequencies.keys():
                frequencies[word] = 1
            else:
                frequencies[word] += 1
    return frequencies

def keyword_analytics(data: List):
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

    # Remove portuguese stopwords
    nltk.download('stopwords')
    stopwords = nltk.corpus.stopwords.words('portuguese') + nltk.corpus.stopwords.words('english') + \
                ['pra', 'pro', 'nao', 'Nao', 'n', 'nn', 'mto', 'mt', 'tbm','vdd']
    # drop_columns = [value for value in stopwords if value in keywords_df.columns]
    drop_columns = [value for value in stopwords if value in keywords_df.columns]
    keywords_df.drop(drop_columns, axis=1, inplace=True)

    # Get sum and count for every keyword
    keywords_count = pd.Series(keywords_df.count(), name='count')
    keywords_sum = pd.Series(keywords_df.sum(), name='sum')
    # Divide the sum of the kewyword values by the number of times it appears (the smaller the value, the more important it is)
    keywords_sum_count = pd.Series(keywords_df.sum() / (keywords_df.count()+1), name='sumOverCount')

    # Combine info into single dataframe
    # keywords_combined = pd.concat([keywords_sum, keywords_count, keywords_sum_count], axis=1)
    
    # Sort series
    keywords_count = keywords_count.sort_values(ascending=False)

    # return keywords_combined.to_dict()
    return {'count':{'index': keywords_count.index.tolist(),'values':keywords_count.tolist()},
            'sum':{'index': keywords_sum.index.tolist(),'values':keywords_sum.tolist()},
            'sumOverCount': {'index': keywords_sum_count.index.tolist(),'values':keywords_sum_count.tolist()}
            }