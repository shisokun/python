import mysql.connector

def getBondInfoByDate(date):
	conn = mysql.connector.connect(user='ec2-user', password='Pass_1234', host='localhost', database='unit1')
	cur = conn.cursor()

	cur.execute("select * from bondinfo where updatedate = %s;", [date]);
	cur.fetchall()

	size = cur.rowcount

	cur.close()
	conn.close()

	return size

def insertBondInfo(response):
	conn = mysql.connector.connect(user='root', password='Pass_1234', host='localhost', database='unit1')
	cur = conn.cursor()
	updatedate = response.get("data003_01").get("updatedate")
	for data in response.get("data003_01").get("data"):
		sql = "insert into bondinfo values(" \
			+ "\"" + updatedate + "\"" \
			+ ",\"" + data.get("title") + "\"" \
			+ ",\"" + data.get("tuuka") + "\"" \
			+ ",\"" + data.get("syokanbi") + "\"" \
			+ ",\"" + data.get("riritsu") + "\"" \
			+ ",\"" + data.get("ribaraibi") + "\"" \
			+ ",\"" + data.get("ukewatashibi") + "\"" \
			+ ",\"" + data.get("rimawari") + "\"" \
			+ ",\"" + data.get("kakaku") + "\"" \
			+ ",\"" + data.get("tanni") + "\"" \
			+ ");"
		cur.execute(sql)
	conn.commit()
	cur.close()
	conn.close()
