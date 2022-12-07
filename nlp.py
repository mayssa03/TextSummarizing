"""
Created on Mon Dec  5 19:27:34 2022

@author: Mayssa Masmoudi
"""

from googlesearch import search
query=input()
for url in search(query, num_results=1):
    print(url)
    
from newspaper import Article
#get article url
article =Article(url)
article.download()
article.parse()
article.nlp()
corpous = article.text
print(corpous)

import nltk
from string import punctuation
stopwords = nltk.corpus.stopwords.words('english')
print(stopwords)

sentence_list = nltk.sent_tokenize(corpous)
print(sentence_list)
punctuation = punctuation + '\n'
print(punctuation)

word_frequencies = {}
for word in nltk.word_tokenize(corpous):
    if word.lower() not in stopwords:
        if word.lower() not in punctuation:
            if word not in word_frequencies.keys():
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1
                  
print(word_frequencies)

max_frequency = max(word_frequencies.values())
print(max_frequency)

for word in word_frequencies.keys():
    word_frequencies[word] = word_frequencies[word]/max_frequency

print(word_frequencies)


sentence_scores = {}
for sent in sentence_list:
    for word in sent:
        if word.lower() in word_frequencies.keys():
            if sent not in sentence_scores.keys():
                sentence_scores[sent] = word_frequencies[word.lower()]
            else:
                sentence_scores[sent] += word_frequencies[word.lower()]
                
print(sentence_scores)


from heapq import nlargest
select_length = int(len(sentence_list)*0.3)
print(select_length)
summary = nlargest(select_length, sentence_scores)
print(summary)
print(len(sentence_list))
print(len(summary))