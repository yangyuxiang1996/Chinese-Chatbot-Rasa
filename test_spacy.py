import spacy

nlp = spacy.load('zh_core_web_md')
doc = nlp('请问秘诀清凉散有什么疗效')
for token in doc:
  print(token.text)


import jieba
jieba.load_userdict("data/dict.txt")
doc = jieba.cut('请问秘诀清凉散有什么疗效')
for token in doc:
  print(token)