# import numpy as np
from datbase import get_connect
from dotenv import load_dotenv
import random
import string
load_dotenv()
# conn =get_connect()
# if conn.is_connected():
#         print("connection extablished")

def gen_random_text(length):
    sets =string.ascii_letters+string.digits+'-_!'
    strs =""
    return strs.join(random.choices(sets,k =length))
def urlshort_fun(url,active,percent=50):
    conn =get_connect()
    if conn.is_connected():
        print("connection extablished")
    try:
        cursor = conn.cursor()
        query ="select id from url_table where url = %s limit 1"
        cursor.execute(query,(url,))
        prefix =url[0:7]
        result =cursor.fetchone()
        if result: return prefix+result[0]
        url_length =len(url)-8
        url_length =url_length-int(percent/100*url_length)
        random_part =gen_random_text(url_length)
        new_url ="https://"+random_part
        cursor.execute("insert into url_table(id,url,is_active) values(%s,%s,%s)",(random_part,url,active))
        conn.commit()
        return new_url
    finally:
        cursor.close()
        conn.close()
        
# print(urlshort_fun("https://leetcode.com/problems/maximize-sum-of-squares-of-digits/description/?envType=daily-question&envId=2026-10-14",78))
