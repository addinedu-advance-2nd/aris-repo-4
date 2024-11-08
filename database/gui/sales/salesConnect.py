#pip3 install mysql-connector-python
from urllib.parse import ParseResultBytes

import mysql.connector
from database.connect.connectMysql import *

# MySQL 서버에 연결
# (재고설정) 아이스크림 종류 가져 오기
def selectSaleIceCream():
    tmpResult =""
    cursor = conn.cursor()
    sql = "SELECT REPLACE( REPLACE( REGEXP_REPLACE(json_keys(iceCodes), '[\"]', ''), \"[\",\"\"),\"]\",\"\") FROM INVENTORY ORDER BY inventoryNum DESC LIMIT 1"
    print(sql)
    cursor.execute(sql)
    tmpResult = cursor.fetchone()[0]
    conn.commit()
    cursor.close()


    result = []
    cursor = conn.cursor()
    sql = "SELECT iceName FROM ICECREAM WHERE iceCode IN ("+tmpResult+")"
    print(sql)
    cursor.execute(sql)
    while (True):
        row = cursor.fetchone()
        if row == None:
            break;
        result.append(row[0])
    conn.commit()
    cursor.close()
    return result


# (재고설정) 토핑 종류 가져 오기
def selectSaleTopping():
    tmpResult = ""
    cursor = conn.cursor()
    sql = "SELECT REPLACE( REPLACE( REGEXP_REPLACE(toppingCodes, '[\"]', ''), \"[\",\"\"),\"]\",\"\") FROM INVENTORY ORDER BY inventoryNum DESC LIMIT 1"
    print(sql)
    cursor.execute(sql)
    tmpResult = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    print(tmpResult)

    result = []
    cursor = conn.cursor()
    sql = "SELECT toppingName FROM TOPPING WHERE toppingCode IN (" + tmpResult + ")"
    print(sql)
    cursor.execute(sql)
    while (True):
        row = cursor.fetchone()
        if row == None:
            break;
        result.append(row[0])
    conn.commit()
    cursor.close()
    return result

#from database.gui.inventory.inventoryConnect import insertInventory
#invertoryInfo = {}from database.gui.inventory.inventoryConnect import insertInventory
#invertoryInfo['ice'] = "'{0}','{1}','{2}','{3}','{4}','{5}'".format(selected_menu,0,selected_menu,10,selected_menu,8)
#invertoryInfo['topping'] = "4,5,6"
#insertInventory(invertoryInfo)
