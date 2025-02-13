from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import re
import unittest

usuarios = {
    "user1": ["Machine Learning", "Data Science", "Python"],
    "user2": ["Deep Learning", "Artificial Intelligence", "Python"],
    "user3": ["Software Engineering", "Agile", "Project Management"]
}

artigos = [
    "Machine Learning for Beginners",
    "Advanced Data Science Techniques",
    "Introduction to Artificial Intelligence",
    "Agile Project Management",
    "Python for Data Science"
]

def preprocess_custom(text):
    stopwords = {"for", "to", "in", "the", "and", "a"}
    words = text.lower().split()
    return " ".join([word for word in words if word not in stopwords])

def tokenize_fuzzy(text):
    return process.extract(text, artigos, limit=3)

def tokenize_custom(text):
    words = text.split()
    return [" ".join(words[i:i+2]) for i in range(len(words)-1)]

def recomendar_artigos(usuario):
    preferencias = usuarios.get(usuario, [])
    recomendacoes = {}
    
    for artigo in artigos:
        max_score = 0
        for pref in preferencias:
            score = fuzz.ratio(artigo, pref)
            max_score = max(max_score, score)
        recomendacoes[artigo] = max_score
    
    return sorted(recomendacoes, key=recomendacoes.get, reverse=True)

def jaccard_similarity(str1, str2):
    set1, set2 = set(str1.split()), set(str2.split())
    return len(set1 & set2) / len(set1 | set2)

class TestSistemaRecomendacoes(unittest.TestCase):
    def test_preprocess_custom(self):
        self.assertEqual(preprocess_custom("Introduction to AI"), "introduction ai")
    
    def test_tokenize_custom(self):
        self.assertEqual(tokenize_custom("Machine Learning for AI"), ["Machine Learning", "Learning for", "for AI"])
    
    def test_recommendation(self):
        recomendacoes = recomendar_artigos("user1")
        self.assertIn("Machine Learning for Beginners", recomendacoes)
    
    def test_jaccard_similarity(self):
        score = jaccard_similarity("Machine Learning", "Learning Machines")
        self.assertGreater(score, 0)
        
if __name__ == "__main__":
    unittest.main()