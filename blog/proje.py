import os
import re
import sys
import time
import sys

import mysql.connector
import pandas as pd
from numpy import r_

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="products"
)

productn2=sys.argv[1:]
if len(productn2)==1:


    productn1=str(productn2[0]).lower()

else:

    for indx,i in enumerate(productn2):
        productn2[indx] = str(i)
    productn1=str(" ".join(productn2)).lower()

cursor=mydb.cursor()

productn=""
list1=productn1.replace(","," ").replace("'"," ").replace('"'," ").replace("-"," ").replace("+"," ").replace(";"," ").replace("."," ").replace("*"," ").split()
while("" in list1):
    list1.remove("")
while(" " in list1):
    list1.remove(" ")
lst2element="""" '" , - + ; . *"""
list2=lst2element.split(" ")
for x1 in list1:
    for x2 in list2:
        if x2 in x1:
            list1.remove(x1)
for x,pd1 in enumerate(list1):
    productn+='"%'+pd1
    if x+1!=len(list1):
        productn+="""%" and Product_name LIKE """
    else:
        productn+='%"'

productcompare=re.split("[\/\"()-+;.,\s]\s*",productn1)

cursor.execute("SELECT * FROM productstable2 WHERE Product_name LIKE "+productn)

products2_df= pd.DataFrame(cursor.fetchall())

try:
    products2_df.columns=[x[1]for x in cursor.description]
except:
    pass
products2_df
mainlist=[]
productslist=products2_df.values.tolist()
for x in productslist:
    z = re.split("[\/\"()\'-+;.,\s]\s*",x[1])
    for n,y in enumerate(productcompare):     
        if y not in z:
            break
        elif n+1==len(productcompare):
            mainlist.append(x)
    
mainlist=sorted(mainlist, key = lambda x: x[2])
panda=pd.DataFrame(mainlist)

for m in mainlist:
    source="img/"+m[5]+".jpg"
    print('<tr>')
    print('<td class="isim"><a target="_blank" href="'+str(m[3])+'">'+str(m[1])+'<a></td>')

    print('<td class="fiyat">'+str(m[2])+"TL"+'</td>')

    print('<td class="ürün"><img  src="'+str(m[4])+'"></td>')
    print('<td><img  class="resim" src='+source+'></td>')
    print('</tr>')

print('</table>')
