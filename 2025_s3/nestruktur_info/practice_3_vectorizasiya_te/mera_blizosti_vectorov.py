import spacy

nlp = spacy.load("ru_core_news_lg")

text = "Все счастливые семьи счастливы одинаково, каждая несчастливая семья несчастлива по-своему"

doc = nlp(text)
vector = doc.vector  # 300-мерный вектор предложения

#print("Размерность вектора:", len(vector))
#print("Вектор предложения:\n", vector)

doc1 = nlp(text)
doc2 = nlp(text)
similarity = doc1.similarity(doc2)

print("\nМера близости между двумя одинаковыми предложениями:", similarity)
