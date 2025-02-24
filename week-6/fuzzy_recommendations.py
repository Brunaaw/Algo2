from fuzzy_match import match
import re
import unittest

usuarios = {
    "Alice": ["Machine Learning", "Data Science", "Python"],
    "Bruno": ["Deep Learning", "Artificial Intelligence", "Python"],
    "Carla": ["Software Engineering", "Agile", "Project Management"]
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

def tokenize_custom(text):
    return text.split()

def calcular_similaridade_usuarios(usuario):
    preferencias_usuario = set(usuarios.get(usuario, []))
    similaridade = {}
    for outro_usuario, prefs in usuarios.items():
        if outro_usuario != usuario:
            interseccao = len(preferencias_usuario.intersection(prefs))
            similaridade[outro_usuario] = interseccao / len(preferencias_usuario.union(prefs))
    return similaridade

def recomendar_artigos(usuario):
    similaridade = calcular_similaridade_usuarios(usuario)
    recomendacoes = {}
    for outro_usuario, sim_score in similaridade.items():
        for artigo in usuarios[outro_usuario]:
            if artigo not in usuarios[usuario]:
                recomendacoes[artigo] = recomendacoes.get(artigo, 0) + sim_score
    return sorted(recomendacoes, key=recomendacoes.get, reverse=True)

if __name__ == "__main__":
    usuario_input = input("Selecione um usuário digitando o número correspondente: 1 - Alice, 2 - Bruno, 3 - Carla: ")
    usuarios_nomes = {"1": "Alice", "2": "Bruno", "3": "Carla"}
    usuario_input = usuarios_nomes.get(usuario_input, None)
    if usuario_input in usuarios:
        recomendacoes = recomendar_artigos(usuario_input)
        print("Recomendações para", usuario_input, ":", recomendacoes)
    else:
        print("Usuário não encontrado.")

class TestSistemaRecomendacoes(unittest.TestCase):
    def test_preprocess_custom(self):
        self.assertEqual(preprocess_custom("Introduction to AI"), "introduction ai")

    def test_tokenize_custom(self):
        self.assertEqual(tokenize_custom("Machine Learning for AI"), ["Machine", "Learning", "for", "AI"])

    def test_recommendation(self):
        recomendacoes = recomendar_artigos("Alice")
        self.assertTrue(len(recomendacoes) > 0)

if __name__ == "__test__":
    unittest.main()