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


# MySQL 서버에 연결
def selectIceCream():
    cursor = conn.cursor()
    sql = "SELECT GROUP_CONCAT(iceName) FROM ICECREAM WHERE useYN = 'Y'"
    print(sql)
    cursor.execute(sql)
    result = cursor.fetchone()
    cursor.close()
    #conn.close()
    return result

#from database.gui.inventory.inventoryConnect import insertInventory
#invertoryInfo = {}
#invertoryInfo['ice'] = "'{0}','{1}','{2}','{3}','{4}','{5}'".format(selected_menu,0,selected_menu,10,selected_menu,8)
#invertoryInfo['topping'] = "4,5,6"
#insertInventory(invertoryInfo)
