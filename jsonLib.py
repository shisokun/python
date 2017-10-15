from urllib.request import urlopen
import json

def getJson(url):
	ret = urlopen(url)
	retJson = json.loads(ret.read().decode("utf-8"))
	return retJson

