# django-selenium-find-the-cheapest-product

 Product information is extracted from shopping sites with Selenium.  On the django-based website, the cheapest of the searched product is fi
# How it works
We have a script name as "datascript".  
- [Hepsiburada script](https://github.com/thbn1/django-product-filter/blob/main/blog/datascript.py)
- [Amazon script](https://github.com/thbn1/django-product-filter/blob/main/blog/datascript2.py)
- [Trendyol script](https://github.com/thbn1/django-product-filter/blob/main/blog/datascript3.py)     
The script adds products from shopping site to Django's database with Selenium. If you search something in site, it filters products with tha
### Codes from filter([view.py](https://github.com/thbn1/django-product-filter/blob/main/blog/views.py)):
```sh
    cursor.execute("SELECT * FROM blog_products WHERE Product_name LIKE "+productn)
    products2_df= pd.DataFrame(cursor.fetchall())
    try:
        products2_df.columns=[x[1]for x in cursor.description]
    except:
        pass
  
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
```
```sh
    for index,cnn in enumerate(cntname):
        if forcontrol==True:
            break
        wordcontrol=False
        if cnn.strip()==list1[0].strip():
            for i in range(len(list1)):
                if cntname[index+int(i)].strip()==list1[i].strip():
                    wordcontrol=True
                    if int(i)==int(range(len(list1))[-1]):
                        forcontrol=True
                        break
                else:
                    wordcontrol=False
                    break
    if wordcontrol==False:
        continue
```
 
# Screenshots
### Homepage
![Screenshots](https://github.com/thbn1/django-product-filter/blob/main/readmepng/rm1.png)
### Searching page
![Screenshots](https://github.com/thbn1/django-product-filter/blob/main/readmepng/rm2.png)
### Login page
![Screenshots](https://github.com/thbn1/django-product-filter/blob/main/readmepng/rm3.png)
# How to set up local server
To run tests, run the following command
```
python manage.py runserver
```
Connect to http://localhost:8000
## Authors
- [@frknakbas65](https://www.github.com/frknakbas65)
- [@thbn1](https://www.github.com/thbn1)
