from pymongo import MongoClient


client_test = MongoClient('localhost', 27017)

db = client_test.pymongo_test

# Test 1: insert one record
posts = db.posts
post_data = {
	'title': 'Pymongo',
	'content': 'Test message of pymongo',
	'author': 'Eason'
}

result = posts.insert_one(post_data)
print('Posts result: {0}'.format(result.inserted_id))

# Test 2: insert multiplt records
po1 = {
	'title': 'VM',
	'content': 'virtual env',
	'author': 'Eason'
}

po2 = {
	'title': 'Docker',
	'content': 'Container is best',
	'author': 'Jackson'
}
post_data_set = [po1, po2]
result = posts.insert_many(post_data_set)
print('Posts result: {0}'.format(result.inserted_ids))

# Test 3: find results
eason_post = posts.find({'author': 'Eason'})
for post in eason_post:
	print(post)