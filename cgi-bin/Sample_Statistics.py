#!/usr/bin/env python3

import pymysql
import cgi
import cgitb
import json

cgitb.enable()

form = cgi.FieldStorage()

print("Content-type: text/html\n")

if form:
    try:
        connection = pymysql.connect(
            host='bioed.bu.edu', 
            user='kamillan',
            password='kamillan', 
            db='Team_I',
            port = 4253) 
    except pymysql.Error as e: 
        print(e)
    
    cursor = connection.cursor()
    selector = form.getvalue("selector","")
    timepoint = form.getvalue("timepoint", 0)
    
    
    if (selector == "plotbox"):

        query1 = """
        SELECT score, cell_line
        FROM PEAK JOIN SAMPLE USING(sid)
        WHERE timepoint = %s AND cell_line IN ('2-7', '2-4')
        """

        try: 
            cursor.execute(query1, [int(timepoint)])
        except pymysql.Error as e: 
            print(e,query1)
        
        results = cursor.fetchall()
        print(json.dumps(results))