import requests
from bs4 import BeautifulSoup
import urllib


def run():
	for i in range(1,5):
		response = requests.get('https://xkcd.com/{}'.format(i))	#hace peticion al servidor
		soup = BeautifulSoup(response.content, 'html.parser')	#Parsea info a html
		image_container = soup.find(id='comic')	#Busca entre las etiquetas html la que tenga id comic

		image_url = image_container.find('img')['src'] 	#Busca las etiquetas img y almacena atributo src
		image_name = image_url.split('/')[-1]	#divide url por / y almacena la ultima posicion del arreglo
		print('Descargando imagen {}'.format(image_name))
		urllib.request.urlretrieve('https:{}'.format(image_url), image_name)	#descarga imagenes urlDeRecurso, nombreDeGuardado


if __name__ == '__main__':
	run()