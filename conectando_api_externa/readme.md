# Exercício

Faça um programa para ler dados de clima de uma API externa para as 50 maiores
cidades do Brasil. As 50 maiores cidades do Brasil de acordo com o Senso de 2022
estão listadas nesta URL da Wikipedia:
https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Brasil_por_popula%C
3%A7%C3%A3o_(2022)
A API de clima que será utilizada é a da Open Weather. Você deve se registrar para ter
acesso a uma chave de API gratuita usando esta URL - selecione a opção Current
weather and forecasts collection - Free: https://openweathermap.org/price
Aqui está a documentação da API: https://openweathermap.org/current
Aqui temos uma lista de todos os valores de latitude e longitude das cidades
brasileiras:
https://edisciplinas.usp.br/pluginfile.php/6160610/mod_resource/content/2/latitude
-longitude-cidades.csv
Seu programa deve gerar uma saída em tela e também salvar em um arquivo pdf os
seguintes dados: lista de todas as 50 maiores cidades e o tempo principal atual na
cidade (pegar o campo "weather" / "main").
Extra: permitir que o usuário digite o nome de uma cidade, para que o seu programa
retorne para ele as diversas informações de tempo retornadas pela API.