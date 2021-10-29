import requests
import re

# TODO Выводится лишный сивол(</h3>) в резултате
url = requests.get("http://www.columbia.edu/~fdc/sample.html")
text = url.text
result = re.findall(r"[^>]+</h3>", text)
print(result)
