import requests

r = requests.get('http://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/champions/110.json')
if r.status_code != 200:
	#This means something went wrong
	raise ApiError('GET raw {}'.format(r.status_code))

print(r.json())