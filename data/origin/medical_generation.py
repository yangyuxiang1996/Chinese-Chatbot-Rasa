#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-02 16:06:08
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-20 10:07:26
FilePath: /rasa-chat/data/origin/medical_generation.py
Description:
'''
import json
from random import choice
import yaml

RELATIONS = {'有...功效', '产自...地', '有...性味', '归...经', '组成', '治疗'}
QUESTIONS = [
    "请问[@](medicine)有什么[功效](ask_about)",
    "[@](medicine)是[用来](ask_about)干什么的",
    "[@](medicine)可以[治疗](ask_about)什么",
    "请问[@](medicine)有什么[疗效](ask_about)",
    "[@](medicine)是什么药",
    "[@](medicine)的[功效](ask_about)和[作用](ask_about)有哪些",
    "请问[@](medicine)的[效果](ask_about)怎么样",
    "[@](medicine)[治](ask_about)什么",
    "[@](medicine)的[产地](ask_about)是哪里",
    "[@](medicine)[产自于](ask_about)哪里",
    "[@](medicine)由什么[成分](ask_about)组成"
    
]

with open('medical.json', 'r') as f:
    data = json.load(f)

all_drugs = set()

for item in data:
    all_drugs.add(item['values'][0]['resourceName'])
print('len of drugs: %d' % len(all_drugs))

questions = []
for drug in all_drugs:
    questions.append(choice(QUESTIONS).replace('@', drug))


yaml_path = r'medical_ner.yaml'

data = {'nlu': {'intent': 'medicines', 'examples': questions}}

with open(yaml_path, 'w', encoding='utf-8') as f:
    yaml.dump(data, f, encoding='utf-8', allow_unicode=True)

print('Processing complete!')