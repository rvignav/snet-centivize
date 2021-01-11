import torch
import nltk
from nltk import tokenize
from transformers import pipeline

def setup():
    nltk.download('punkt')

def summarize(par, percent_len=0.5):
    qa = pipeline('summarization')
    graf = par
    graf = tokenize.sent_tokenize(graf)

    sent_num = 3 // percent_len
    if sent_num <= 3 or len(graf) <= 3:
        return "Parameter combination results in an undesirable output. Consider either lengthening the input text or changing the percent_len argument."
    if sent_num >= len(graf):
        return "percent_len is below the minimum value for this particular sequence, lowering it further will not shorten the output"
    
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