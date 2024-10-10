import requests
soles = input("¿Cuántos soles tienes?: ")
soles = float(soles)
tipo_cambio = requests.get('https://api.apis.net.pe/v1/tipo-cambio-sunat')
# 'https://api.apis.net.pe/v1/tipo-cambio-sunat?fecha=2021-06-23'
# 'https://api.apis.net.pe/v1/tipo-cambio-sunat?month=6&year=2021'
valor_dolar = tipo_cambio.json().get("compra") if tipo_cambio.status_code == 200 else 3.88
dolares = round(soles / valor_dolar, 2)
dolares = str(dolares)
print("Tienes $", dolares, "dólares")