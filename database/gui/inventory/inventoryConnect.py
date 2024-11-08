#pip3 install mysql-connector-python
import mysql.connector
from database.connect.connectMysql import *

# MySQL 서버에 연결
def insertInventory(param):
    cursor = conn.cursor()
    print(param['ice'])
    print(param['topping'])
    sql = "INSERT INTO `ROBOPALZ`.`INVENTORY`(`iceCodes`,`toppingCodes`,`inventoryDate`,`userCode`) VALUES (json_object( "+str(param['ice'])+" ),json_array("+str(param['topping'])+"),now(),0)"
    print(sql)
    cursor.execute(sql)
    conn.commit()
    #conn.close()


# 아이스크림(마스터) 리스트 가져오기
def selectIceCreamList():
    result=[]
    cursor = conn.cursor()
    sql = "SELECT iceName FROM ICECREAM WHERE useYN = 'Y'"
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




# 아이스크림(마스터) 딕셔너리 가져오기
def selectIceCreamDict():
    result={}
    cursor = conn.cursor()
    sql = "SELECT iceName, iceCode FROM ICECREAM WHERE useYN = 'Y'"
    print(sql)
    cursor.execute(sql)
    while (True):
        row = cursor.fetchone()
        if row == None:
            break;
        result[row[0]] = row[1]
    conn.commit()
    cursor.close()
    return result


# 토핑(마스터) 리스트 가져오기
def selectToppingList():
    result=[]
    cursor = conn.cursor()
    sql = "SELECT toppingName FROM TOPPING WHERE useYN = 'Y'"
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


 #토핑(마스터) 딕셔너리 가져오기
def selectToppingDict():
    result={}
    cursor = conn.cursor()
    sql = "SELECT toppingName, toppingCode FROM TOPPING WHERE useYN = 'Y'"
    print(sql)
    cursor.execute(sql)
    while (True):
        row = cursor.fetchone()
        if row == None:
            break;
        result[row[0]] = row[1]
    conn.commit()
    cursor.close()
    return result



#from database.gui.inventory.inventoryConnect import insertInventory
#invertoryInfo = {}
#invertoryInfo['ice'] = "'{0}','{1}','{2}','{3}','{4}','{5}'".format(selected_menu,0,selected_menu,10,selected_menu,8)
#invertoryInfo['topping'] = "4,5,6"
#insertInventory(invertoryInfo)
