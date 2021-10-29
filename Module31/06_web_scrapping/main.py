import requests
import re

url = requests.get("http://www.columbia.edu/~fdc/sample.html")
text = url.text

# TODO во первых укажите от до h3
# TODO используйте группировку символов ()
# TODO +</h3> автоматом плюсует его к выводу
result = re.findall(r"[^>]+</h3>", text)
print(result)
