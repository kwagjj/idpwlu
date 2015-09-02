#!/usr/bin/python

import sys
import MySQLdb as mdb

def op1(con):
	cur=con.cursor()
	cur.execute("select website,id,pw from list1")
	rows=cur.fetchall()
	for row in rows:
		print("%s | %s | %s\n" % (row[0],row[1],row[2]))
	cur.close()


def op2(con):
	var1=raw_input("search keyword for website field:")
	cur=con.cursor()
	var2="%"+var1+"%"
	print (var2,)
	cur.execute("""select website,id,pw from list1 where website like %s;""",(var2,))
	rows=cur.fetchall()
	for row in rows:
		print("%s | %s | %s\n" % row)
	cur.close()


def op3(con):
	print("delimiter is comma.finish by writing exit")
	while True:
		inp=raw_input();
		if inp=='exit':
			break
		set1=inp.split(',')
		cur=con.cursor()
		cur.execute("""insert into list1(website,id,pw) values(%s,%s,%s);""",(set1[0],set1[1],set1[2]))
		con.commit()
		cur.close()


con=mdb.connect('localhost','user1','user1pw','idpw')

while True:
	print("=======================================")
	sel=raw_input("select operation. 1) show all list // 2) search for item // 3) insert record // 4)exit\n")
	if sel=='1':
		op1(con)
	elif sel=='2':
		op2(con)
	elif sel=='3':
		op3(con)
	elif sel=='4':
		print("goodbye")
		break
	else:
		print("invalid input. retry.")


