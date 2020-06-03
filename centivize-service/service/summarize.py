import torch
import nltk
from nltk import tokenize
from transformers import pipeline

def setup():
    nltk.download('punkt')

def summarize(par, num=11):
    qa = pipeline('summarization')
    sent_num = num
    graf = par
    graf = tokenize.sent_tokenize(graf)
    final = []
    for i in range(len(graf)):
        if i % sent_num == 0:
            final.append(graf[i])
        else:
            final[-1] += ' '
            final[-1] += graf[i]
    split = final 
    summ = qa(split)
    out = ''
    for block in summ:
        out += block['summary_text']
    return out
