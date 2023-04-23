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
            user='mkpannu',
            password='Sukh&Prab50', 
            db='Team_I',
            port = 4253) 
    except pymysql.Error as e: 
        print(e)
    
    cursor = connection.cursor()
    selector = form.getvalue("selector","")
    timepoint = form.getvalue("timepoint", 0)
    chromosome = form.getvalue("chromosome", "")
    
    if (selector == "plotpeaks"):

        query1 = """
        SELECT abs_summit, signalValue
        FROM PEAK JOIN SAMPLE USING(sid)
        WHERE timepoint = %s AND cid = %s
        ORDER BY abs_summit
        """

        try: 
            cursor.execute(query1, [int(timepoint), chromosome])
        except pymysql.Error as e: 
            print(e,query1)
        
        results = cursor.fetchall()
        print(json.dumps(results))
    