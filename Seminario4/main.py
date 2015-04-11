#!/usr/bin/python
# -*- coding: utf-8 -*

__author__ ='Julian'

#importamos los paquetes que necesitemos
from flask import Flask, render_template
from flask.ext.googlemaps import GoogleMaps
from flask.ext.googlemaps import Map

import twitterAPI
import json


app = Flask(__name__)
GoogleMaps(app)
lista=[]

#Nos conectamos a mi cuenta
twitter_api = twitterAPI.oauth_login() 

#Almacenos los tweets que tengan estas caracteristicas
Contenedor_tweet = twitter_api.search.tweets(q='RealMadrid',count=500,geocode='40.45,-3.75,1000km') 

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

#Creamos el Mapa con los valores que queramos
@app.route("/")
def mapview():
    mymap = Map(
        identifier="view-side",
        lat=40.45,
        lng=3.75,
        markers=lista,
        style="height:600px;width:600px;margin:0", 
        zoom=4
    )
    return render_template('template2.html', mymap=mymap)

#Ejecutamos la App
if __name__ == "__main__":
    app.run(debug=True)