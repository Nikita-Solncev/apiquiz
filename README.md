��#   a p i q u i z 

пример использования:

import requests
response = requests.get("http://127.0.0.1:5000/getquestion?difficulty=easy").json()
print(response)

Вопросы могут быть трёх сложностей: easy, medium, hard. В запросе можно указать сложность в параметре difficulty.
