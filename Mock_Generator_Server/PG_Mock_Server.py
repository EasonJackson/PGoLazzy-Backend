#!/PokemonGo-Project
import json
import time
import math
import sys
import random
import s2sphere
from s2sphere import CellId, math, Cap, LatLng, Angle
from s2sphere import RegionCoverer

EARTH_RADIUS = 6371000 # Radius in meters

class Pokemon(Object):
	def __init__(self, pokemon_id, lng, lat, expire, spawn_point_id, encounter_id):
		self.pokemon_id = pokemon_id
		self.lng = lng
		self.lat = lat
		self.expire = expire
		self.spawn_point_id = spawn_point_id
		self.encounter_id = encounter_id

	def __str__(self):
		return "id: {0}, lng: {1}, lat: {2}, expire: {3}".format(self.pokemon_id, self.lng, self.lat, self.expire)

	def 

while True:
	