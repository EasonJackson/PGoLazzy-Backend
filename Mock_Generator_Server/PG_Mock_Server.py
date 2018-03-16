#!/PokemonGo-Project
# Pokemon GoLazzy mock generator server
# Server runs on localhost:50007
# Connection with mongodb on socket 27017
# The server listens 1 client connected to port 50007
# and accept text based streams of request parameters
# The server takes format of input stream as
# left-up-lat, left-up-lng, right-down-lat, right-down-lng
# All lats and lngs are in float format with 8 digits accuracy


import json
import time
import math
import random
from pymongo import MongoClient
import s2sphere
import socket
from s2sphere import CellId, math, Cap, LatLng, Angle
from s2sphere import RegionCoverer

HOST = ''
PORT = 50007

MAX_NUMBER_OF_SIMULATION = 100
POKEMON_NUMBER = 493
EXPIRATION_DURATION = 60 * 20 * 1000

client = MongoClient('localhost', 27017)
db = client.pokemon_golazzy_data
posts = db.posts

region = s2sphere.RegionCoverer()

class Pokemon:
	def __init__(self, pokemon_id, lng, lat, expire, cell_id):
		self.pokemon_id = pokemon_id
		self.lng = lng
		self.lat = lat
		self.expire = expire
		self.cell_id = cell_id
		
	def __str__(self):
		return "id: {0}, lng: {1}, lat: {2}, expire: {3}".format(self.pokemon_id, self.lng, self.lat, self.expire)

def setupSocket():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((HOST, PORT))
	s.listen(1)
	print("Connections built successfully.")
	print("Mocking server runs on PORT " + str(PORT))
	return s

def handler(data):
	raw = data.split(',')
	left_up = {}
	right_down = {}
	left_up['lat'] = float(raw[0])
	left_up['lng'] = float(raw[1])
	right_down['lat'] = float(raw[2])
	right_down['lng'] = float(raw[3])
	print("Parse rectangle area successfully")
	
	res = []
	for _ in range(MAX_NUMBER_OF_SIMULATION):
		lng_rand = random.random()
		lat_rand = random.random()
		pokemon_id = int(1 + random.random() * (POKEMON_NUMBER - 1))
		position_lng = (1 - lng_rand) * left_up['lng'] + lng_rand * right_down['lng']
		position_lat = (1 - lat_rand) * right_down['lat'] + lat_rand * left_up['lat']
		cell_id = getCellId(position_lat, position_lng)[0]
		pokemon_instance = Pokemon(pokemon_id, position_lng, position_lat, EXPIRATION_DURATION, cell_id)
		res.append(pokemon_instance)
	print(res)
	#insert_to_db(res)

def getCellId(position_lat, position_lng):
    p1 = s2sphere.LatLng.from_degrees(position_lat, position_lng)
    p2 = p1
    cell_ids = region.get_covering(s2sphere.LatLngRect.from_point_pair(p1, p2))
    return cell_ids

def insert_to_db(list_of_data):
	try:
		result = posts.insert_many(list_of_data)
		print('Posts result: {0}'.format(result.inserted_ids))
	except Exception as e:
		raise e('MongoDB', 'Insertion error.')
	

sock = setupSocket()
while True:
	try:
		conn, addr = sock.accept()
		print("Server connected by client at " + str(addr))
		data = conn.recv(1024)
		handler(data)
	except Exception as e:
		print(e)
		pass
conn.close()