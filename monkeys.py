# -*- coding: utf-8 -*-
"""
Created on Tue May  4 15:43:44 2021

@author: gferr
"""

from monkeylearn import MonkeyLearn

app = MonkeyLearn('e45a9529793fe6be9415f53a65dcdcc34f24b666')

#data = ["This is a great tool!"]
#data = ['first text', {'text': 'second text', 'external_id': 'ANY_ID'}, '']
model_id = 'cl_pi3C7JiL'


### POST request https://api.monkeylearn.com/v3/classifiers/cl_pi3C7JiL/classify/
### GET request https://api.monkeylearn.com/v3/classifiers/

# result = app.classifiers.classify(model_id, data)
# result = app.classifiers.list(page=2,per_page=5,order_by=['is_public','name'])
# result = app.classifiers.classify(model_id,data)
# result = app.base_urlextractors.extract(model_id, data=data)
# result = app.classifiers.list()
result = app.classifiers.deploy(model_id)
print(result.body)

