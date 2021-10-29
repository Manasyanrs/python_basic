import re


registration_numbers = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'
car = re.findall(r"\b[АВЕКМНОРСТУХ]\d{2,3}\w+\d{2,3}", registration_numbers)
taxi = re.findall(r"\b[АВЕКМНОРСТУХ]{2}\d{2,3}\w+\d{2,3}", registration_numbers)
print("Список номеров частных автомобилей: {}".format(car))
print("Список номеров такси: {}".format(taxi))

# зачет!
