#encoding=utf8
from pymongo import MongoClient
import json
from bson import ObjectId
import datetime
import sys
import os


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

def main():
	while True:
		ip = raw_input('Link>> ').split(':')
		out = int(raw_input('Item>> '))
		port = 27017
		if len(ip)>1:
			port = ip[1]
			ip = ip[0]

		#连接mongo库
		con = MongoClient(ip,port)
		dbs = con.database_names()
		dbname = ''
		for db in xrange(len(dbs)):
			print "| DBIndex: %s tDB: %s"%(db,dbs[db])
		print '| Tips:(type "break" to exit)'
		while True:
			select =  raw_input('n| Select Index: ')
			if select == 'break':
				break
			else:
				dbname = dbs[int(select)]
			#选择数据库
			db = con[dbname]
			# 认证
			# auth = raw_input('| Auth: ').split(':')
			# print
			# if auth != ['']:
			# 	con.authenticate(auth[0],auth[1])
			#输出该库所有聚合名
			cols = db.collection_names()
			cols.sort()
			lens = {}
			print '_'*(8+4+10+13)+'n| dex  |   number   |  collection  n'+'-'*(8+4+10+13)
			for col in xrange(len(cols)):
				lens[cols[col]] = db[cols[col]].count()
				a = lens[cols[col]]
				print "| %s | %s | %s"%((str(col)+(4-len(str(col)))*' '),(str(a)+(10-len(str(a)))*' '),cols[col])
			print '-'*(8+4+10+13)
			dirs = "ddbs/%s/%s"%(ip[0],dbname)
			if not os.path.exists(dirs):
				os.makedirs(dirs)
			if lens:
				while True:
					use = cols
					mode = raw_input('n| [all] or [Index] :')
					if mode == 'all':
						pass
					elif mode == 'break':
						break
					else:
						lsl = []
						for x in mode.split():
							lsl.append(cols[int(x)])
						cols = lsl

					output = sys.stdout
					for i in xrange(len(cols)):
						#find().batch_size(i) 定时游标
						#find(no_cursor_timeout=True) 不超时
						ii = 1
						files = '%s/%s.json'%(dirs,cols[i])
						open(files,'w').write('[')
						finder = None
						if out >=0:
							finder = db[cols[i]].find().batch_size(out)
						else:
							finder = db[cols[i]].find(no_cursor_timeout=True)
						for x in finder :
							ii+=1
							enco = lambda obj: (obj.isoformat() if isinstance(obj, datetime.datetime) or isinstance(obj, datetime.date) else None)
							try:
								x = x.JSONEncoder().encode(x).encode('utf8')
							except Exception, e:
								x = json.dumps(x,default=enco).encode('utf8')
							open(files,'a').write(x)
							maxlen = lens[cols[i]]+1
							if ii!= maxlen:
								open(files,'a').write(',')
							output.write('r| Now: %s  | Index: %s %.15f%%  | Len: %s'%(cols[i],ii,(float(ii)/float(maxlen)*100),len(x)))
							######
							if ii>2000:
								break;
						open(files,'a').write(']')
					cols = use
			else:
				print '| None Info'
if __name__ == '__main__':
	main()