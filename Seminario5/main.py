#!/usr/bin/python
# -*- coding: utf-8 -*

__author__ ='Julian'

#importamos los paquetes que necesitemos
from flask import Flask, render_template
from flask import request
from flask.ext.googlemaps import GoogleMaps
from flask.ext.googlemaps import Map

import twitterAPI
import json


app = Flask(__name__)
GoogleMaps(app)


#Nos conectamos a mi cuenta


#Creamos el Mapa con los valores que queramos
@app.route("/buscar", methods=['POST'])
def buscar():
	twitter_api = twitterAPI.oauth_login() 

	q=request.form['text']
	coordenadas=[]
	lista=[]
#Almacenos los tweets que tengan estas caracteristicas
	Contenedor_tweet = twitter_api.search.tweets(q=q,count=100,geocode='40.45,-3.75,1000km') 

#Guardamos en archivo JSON los tweets
	twitterAPI.save_json('contenedor', Contenedor_tweet) 

#Cargamos el archivo JSON
	tweetsjson = json.loads(open('contenedor.json').read()) 

#Analizamos los tweets y guardamos los validos
	for result in tweetsjson["statuses"]:
		if result["geo"]:
			latitud=result["geo"]["coordinates"][0]
			longitud=result["geo"]["coordinates"][1]
			coordenadas=[latitud,longitud]
			lista.append(coordenadas)
			
	print coordenadas
	mymap = Map(
		identifier="view-side",
		lat=40.3450396,
		lng=-3.6517684,
		zoom=6,
		markers=lista,
		style="height:800px;width:800px;margin:0;"
	) 
	return render_template('mapa.html', mymap=mymap)

@app.route("/")
def index():
	return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

