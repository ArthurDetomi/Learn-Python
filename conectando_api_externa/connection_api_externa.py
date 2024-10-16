import requests 
import json
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

API_KEY = ''

def find_weather_by_city_name(city_name = ''):
    params = {'appid' : API_KEY, 'q' : city_name}
    request = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather', params=params
    )
    
    content_json = json.loads(request.content)
    
    return content_json['weather'][0]['main']

def write_city_and_weather_in_txt_file(city_with_weather_dict = {'' : ''}):
    file = open('cidade_clima.txt', 'w')
    file.write('[Cidades/Clima]\n')
    
    count = 1
    for city_name in city_with_weather_dict.keys():
        file.write(f'{count} - {city_name}/{city_with_weather_dict[city_name]}\n')
        count += 1
    
    file.close()  

def write_city_and_weather_in_pdf_file(city_with_weather_dict = {'':''}):
    c = canvas.Canvas('saida.pdf', pagesize=letter)
    
    c.setTitle('Cidade/Clima')
    
    x = 100; y = 750
    count = 1
    for city_name in city_with_weather_dict:
        c.drawString(x, y, f'{count} - {city_name}/{city_with_weather_dict[city_name]}')
        y -= 20
        count += 1
        if y < 50:
            c.showPage()
            y = 750
        
        
    c.showPage()
    c.save()
    print('PDF criado com sucesso!')        

def main():
    city_list = [
        "Teresina",
        "Rio de Janeiro",
        "Brasília",
        "Fortaleza",
        "Salvador",
        "Belo Horizonte",
        "Manaus",
        "Curitiba",
        "Recife",
        "Goiânia",
        "Porto Alegre",
        "Belém",
        "Guarulhos",
        "Campinas",
        "São Luís",
        "Maceió",
        "Campo Grande",
        "São Gonçalo",
        "Teresina",
        "João Pessoa",
        "São Bernardo do Campo",
        "Duque de Caxias",
        "Nova Iguaçu",
        "Natal",
        "Santo André",
        "Osasco",
        "Sorocaba",
        "Uberlândia",
        "Ribeirão Preto",
        "São José dos Campos",
        "Cuiabá",
        "Jaboatão dos Guararapes",
        "Contagem",
        "Joinville",
        "Feira de Santana",
        "Aracaju",
        "Londrina",
        "Juiz de Fora",
        "Florianópolis",
        "Aparecida de Goiânia",
        "Serra",
        "Campos dos Goytacazes",
        "Belford Roxo",
        "Niterói",
        "São José do Rio Preto",
        "Ananindeua",
        "Vila Velha",
        "Caxias do Sul",
        "Porto Velho",
        "Mogi das Cruzes",
        "Jundiaí"
    ]
    
    city_with_weather_dict = {}
    
    print('Carregando dados')
    for city_name in city_list:
        weather_by_city = find_weather_by_city_name(city_name)
        city_with_weather_dict[city_name] = weather_by_city
    print('Dados carregados com sucesso!')
    
    write_city_and_weather_in_txt_file(city_with_weather_dict)
    write_city_and_weather_in_pdf_file(city_with_weather_dict)
    
    print('\tDigite (exit) para sair')
    while True:
        city_name_search =  input('Digite o nome de uma cidade que você queira saber o clima:')
        if city_name_search == 'exit':
            break
        if city_name_search in city_with_weather_dict:
            print(f'Clima: {city_with_weather_dict[city_name_search]}')
        else:
            print('Cidade não está na base de dados!')
        
main()