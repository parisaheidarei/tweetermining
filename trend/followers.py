import simplejson as json
import urllib

followers = json.load(open("followers.json"))["ids"]
offset = 100

alldata = []
csv = "name\tfollowers\tfriends\tstatuses\tfollowing\n"

for i in range(1+len(followers) / offset):
	idx = i * offset
	users = followers[idx:idx+offset]
	user_id = ','.join(str(x) for x in users)

	#print 'loading'+str(len(users))+' users from '+str(idx)

	url = 'https://api.twitter.com/1/users/lookup.json'
	params = urllib.urlencode({'user_id': user_id})
	data = urllib.urlopen(url, params).read()
	alldata += json.loads(data)
	for user in alldata:
		csv += '\t'.join(str(x) for x in [
			user['screen_name'],
			user['followers_count'],
			user['friends_count'],
			user['statuses_count'],
			user['following']]) + '\n'
	open('cache/'+str(i)+'.json','w').write(data)

	open('all-followers.csv','w').write(csv)
	open('all-followers.json','w').write(json.dumps(alldata))