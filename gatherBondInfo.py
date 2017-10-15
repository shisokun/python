from BondInfo import getBondInfoByDate
from BondInfo import insertBondInfo
from jsonLib import getJson
import sys

response = getJson("http://www.sc.mufg.jp/json/data003-01.json")

updatedata = response.get("data003_01").get("updatedate")
size = getBondInfoByDate(updatedata)
if size != 0:
	sys.exit()

insertBondInfo(response)

