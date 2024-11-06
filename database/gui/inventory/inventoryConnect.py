#pip3 install mysql-connector-python
import mysql.connector
from database.connect.connectMysql import *

# MySQL 서버에 연결
def insertInventory():
    cursor = conn.cursor()
    #sql = "insert into (`iceCodes`,`toppingCodes`,`userCode`) INVENTORY values(%s, %s,  %s)"
    #vals = (vo.iceNum , vo.pwd, vo.name, vo.email)
    #vals = ('{ "1" : 30, "2" :20 ,"3": 40 }','[1,3,4]', '0')
    #cursor.execute(sql, vals)
    sql = "INSERT INTO `ROBOPALZ`.`INVENTORY`(`iceCodes`,`toppingCodes`,`inventoryDate`,`userCode`)VALUES ('{ ""1"" : 30, ""2"" :20 ,""3"": 40 }','[1,3,4]',now(),0)"
    cursor.execute(sql)
    conn.commit()
    conn.close()


insertInventory()