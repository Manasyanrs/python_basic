import requests
import re

url = requests.get("http://www.columbia.edu/~fdc/sample.html")
text = url.text

result = re.findall(r">(.+)</h3>", text)
print(result)

# зачет!
