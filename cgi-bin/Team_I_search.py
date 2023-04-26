#!/usr/bin/env python3

import pymysql
import cgi
import cgitb
import json
from collections import OrderedDict

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
    sortby = form.getvalue("sortby", 0)
    timepoint = form.getvalue("timepoint", 0)
    chromosome = form.getvalue("chromosome", "")
    start_pos = form.getvalue("start_pos", 0)
    stop_pos = form.getvalue("stop_pos", 0)
    cell_line = form.getvalue("cell_line", "")
    
    if (selector == "genetable"): 
        query = f"""
        SELECT symbol, description, cid, g.start, g.end, count(distinct pid), max(fold_enrichment)
        FROM gene g JOIN PEAK p USING (cid)
            JOIN SAMPLE USING (sid)
            JOIN gene_set USING (gsid)
        WHERE abs_summit BETWEEN g.start AND g.end AND timepoint = %s AND cell_line = %s
        GROUP BY gid 
        ORDER BY {sortby}
        """

        try: 
             cursor.execute(query, [int(timepoint), cell_line])
        except pymysql.Error as e: 
            print(e,query)
        
        results = cursor.fetchall()
        print(json.dumps(results))


    if (selector == "summarytable"):

        query1 = """
        SELECT cell_line, replicate, start, end, abs_summit, fold_enrichment, pvalue
        FROM PEAK JOIN SAMPLE USING (sid) 
        WHERE timepoint = %s AND cid= %s AND start > %s AND end < %s AND cell_line = %s
        ORDER BY start;
        """

        try: 
            cursor.execute(query1, [int(timepoint), chromosome, int(start_pos), int(stop_pos), cell_line])
        except pymysql.Error as e: 
            print(e,query1)
        
        results = cursor.fetchall()
        print(json.dumps(results))
    