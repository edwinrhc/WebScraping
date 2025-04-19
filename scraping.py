import requests
import time
import random
from fake_useragent import UserAgent

url = "#"

ua = UserAgent()  # Generador de User-Agents aleatorios

for i in range(20):
    try:
        # Configuración de headers aleatorios
        headers = {
            'User-Agent': ua.random,
            'Accept-Language': 'en-US,en;q=0.9',
            'Referer': 'https://google.com/'
        }

        # Delay aleatorio entre 2 y 5 segundos
        delay = random.uniform(2, 5)
        time.sleep(delay)

        # Envío de petición
        response = requests.get(url, headers=headers)

        print(f"Vista {i + 1}: Status {response.status_code} | Delay: {delay:.2f}s")

    except Exception as e:
        print(f"Error en vista {i + 1}: {str(e)}")

print("✅ Proceso completado. 20 visitas enviadas.")