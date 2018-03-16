from pymongo import MongoClient


client = MongoClient('localhost', 27017)

db = client.pokemon_test
posts = db.posts

# Test 1: insert multiplt records
pokemon1 = {
	'cell_id': 10,
	'id': 1,
	'lng': -71.8063,
	'lat': 42.2746,
	'expr': 1539734400
}

pokemon2 = {
	'cell_id': 10,
	'id': 2,
	'lng': -71.8063,
	'lat': 42.2846,
	'expr': 1539734400
}

post_data_set = [pokemon1, pokemon2]
result = posts.insert_many(post_data_set)
print('Posts result: {0}'.format(result.inserted_ids))

# Test 2: find results
pogo_result = posts.find({'cell_id': 10})
for post in pogo_result:
	print(post)