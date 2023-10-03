import requests

# link do open_weather: https://openweathermap.org/

API_KEY = "cb44a0634e9f9e28035d26d64c481920"
cidade = "rio de janeiro"
link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

requisicao = requests.get(link)
requisicao_dic = requisicao.json()
descricao = requisicao_dic['weather'][0]['description']
temperatura = requisicao_dic['main']['temp'] - 273.15
print(descricao, f"{temperatura}ºC")
