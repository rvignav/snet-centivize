import torch
import torch.nn.functional as F
from sentence_transformers import SentenceTransformer
import nltk
from nltk import tokenize

def similarity(par1, par2):
    transformer = SentenceTransformer('roberta-base-nli-stsb-mean-tokens')
    transformer.eval()
    par1 = tokenize.sent_tokenize(par1)
    vec1 = torch.Tensor(transformer.encode(par1))
    vec1 = vec1.mean(0)
    par2 = tokenize.sent_tokenize(par2)
    vec2 = torch.Tensor(transformer.encode(par2))
    vec2 = vec2.mean(0)
    cos_sim = F.cosine_similarity(vec1, vec2, dim=0)
    return cos_sim.item()
