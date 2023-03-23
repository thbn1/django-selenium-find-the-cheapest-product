from django.shortcuts import render
from django.http.response import HttpResponse
from blog.forms import ProductForm
from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from blog.models import Products
from django.db.models import Q
import random
# http://127.0.0.1:8000/         =>index
# http://127.0.0.1:8000/index    =>index
# http://127.0.0.1:8000/blogs    =>blogs
# http://127.0.0.1:8000/blogs/3  =>blog-details

def index(request):

    

    
        rstphone = Products.objects.filter(Q(Product_name__contains='Galaxy s22') | Q(Product_name__contains='iphone 14')| Q(Product_name__contains='iphone 13')| Q(Product_name__contains='iphone 12')).filter(Product_price__gte=8000)
        
        listphone=random.choices(rstphone.values(), k=6)
        
        def a(price):
 
           
            plist=str(price).split(".")
            if len(plist[0])>3:
                try:
                    plist[0]= plist[0][:-3]+"."+plist[0][-3:] 
                except:
                    pass
                
            price=",".join(plist)+"TL"
            return price


        listpc=[]
        listpopular=[]
        listelectronic=[]

                
                
                    
        htmtext="""
        <div class="hometop">
        <div class="divpopular">
        <label class="lblpopular">Popüler Ürünler</label>
        </div>
        <div class="homeprdct">
            <div target="_blank" class="homeprd"><img src="""+listphone[0]["Product_image"]+"""><a href="""+listphone[0]["Product_link"]+""">"""+listphone[0]["Product_name"].title()+"""</a><div class="pricediv"><b class="pprice">"""+a(listphone[0]["Product_price"])+"""</b></div></div>
            <div class="homeprd"><img src="""+listphone[1]["Product_image"]+"""><a href="""+listphone[1]["Product_link"]+">"+listphone[1]["Product_name"].title()+"""</a><div class="pricediv"><label class="pprice">"""+a(listphone[0]["Product_price"])+"""</label></div></div>
            <div class="homeprd"><img src="""+listphone[2]["Product_image"]+"""><a href="""+listphone[2]["Product_link"]+">"+listphone[2]["Product_name"].title()+"""</a><div class="pricediv"><label class="pprice">"""+a(listphone[0]["Product_price"])+"""</label></div></div>
            <div class="homeprd"><img src="""+listphone[3]["Product_image"]+"""><a href="""+listphone[3]["Product_link"]+">"+listphone[3]["Product_name"].title()+"""</a><div class="pricediv"><label class="pprice">"""+a(listphone[0]["Product_price"])+"""</label></div></div>
            <div class="homeprd"><img src="""+listphone[4]["Product_image"]+"""><a href="""+listphone[4]["Product_link"]+">"+listphone[4]["Product_name"].title()+"""</a><div class="pricediv"><label class="pprice">"""+a(listphone[0]["Product_price"])+"""</label></div></div>
            <div class="homeprd"><img src="""+listphone[5]["Product_image"]+"""><a href="""+listphone[5]["Product_link"]+">"+listphone[5]["Product_name"].title()+"""</a><div class="pricediv"><label class="pprice">"""+a(listphone[0]["Product_price"])+"""</label></div></div>
        </div>
        <hr class="topline">
        <div class="divphone">
        <label class="lblphone">Telefon</label>
        </div>
        <div class="homeprdct"> 
            <div target="_blank" class="homeprd"><img src="""+listphone[0]["Product_image"]+"""><a href="""+listphone[0]["Product_link"]+""">"""+listphone[0]["Product_name"]+"""</a><div class="pricediv"><label class="pprice">"""+a(listphone[0]["Product_price"])+"""</label></div></div>
            <div class="homeprd"><img src="""+listphone[1]["Product_image"]+"""><a href="""+listphone[1]["Product_link"]+">"+listphone[1]["Product_name"].title()+"""</a><div class="pricediv"><label class="pprice">"""+a(listphone[1]["Product_price"])+"""</label></div></div>
            <div class="homeprd"><img src="""+listphone[2]["Product_image"]+"""><a href="""+listphone[2]["Product_link"]+">"+listphone[2]["Product_name"].title()+"""</a><div class="pricediv"><label class="pprice">"""+a(listphone[2]["Product_price"])+"""</label></div></div>
            <div class="homeprd"><img src="""+listphone[3]["Product_image"]+"""><a href="""+listphone[3]["Product_link"]+">"+listphone[3]["Product_name"].title()+"""</a><div class="pricediv"><label class="pprice">"""+a(listphone[3]["Product_price"])+"""</label></div></div>
            <div class="homeprd"><img src="""+listphone[4]["Product_image"]+"""><a href="""+listphone[4]["Product_link"]+">"+listphone[4]["Product_name"].title()+"""</a><div class="pricediv"><label class="pprice">"""+a(listphone[4]["Product_price"])+"""</label></div></div>
            <div class="homeprd"><img src="""+listphone[5]["Product_image"]+"""><a href="""+listphone[5]["Product_link"]+">"+listphone[5]["Product_name"].title()+"""</a><div class="pricediv"><label class="pprice">"""+a(listphone[5]["Product_price"])+"""</label></div></div>

        </div>
        
        </div>
            
        <div class="homebot">
        <div class="divcomputer">
        <label class="lblcomputer">Bilgisayar</label>
        </div>
        <div class="homeprdct">

            <div target="_blank" class="homeprd"><img src="""+listphone[0]["Product_image"]+"""><a href="""+listphone[0]["Product_link"]+""">"""+listphone[0]["Product_name"].title()+"""</a><div class="pricediv"><label class="pprice">"""+a(listphone[0]["Product_price"])+"""</label></div></div>
            <div class="homeprd"><img src="""+listphone[1]["Product_image"]+"""><a href="""+listphone[1]["Product_link"]+">"+listphone[1]["Product_name"].title()+"""</a><div class="pricediv"><label class="pprice">"""+a(listphone[1]["Product_price"])+"""</label></div></div>
            <div class="homeprd"><img src="""+listphone[2]["Product_image"]+"""><a href="""+listphone[2]["Product_link"]+">"+listphone[2]["Product_name"].title()+"""</a><div class="pricediv"><label class="pprice">"""+a(listphone[2]["Product_price"])+"""</label></div></div>
            <div class="homeprd"><img src="""+listphone[3]["Product_image"]+"""><a href="""+listphone[3]["Product_link"]+">"+listphone[3]["Product_name"].title()+"""</a><div class="pricediv"><label class="pprice">"""+a(listphone[3]["Product_price"])+"""</label></div></div>
            <div class="homeprd"><img src="""+listphone[4]["Product_image"]+"""><a href="""+listphone[4]["Product_link"]+">"+listphone[4]["Product_name"].title()+"""</a><div class="pricediv"><label class="pprice">"""+a(listphone[4]["Product_price"])+"""</label></div></div>
            <div class="homeprd"><img src="""+listphone[5]["Product_image"]+"""><a href="""+listphone[5]["Product_link"]+">"+listphone[5]["Product_name"].title()+"""</a><div class="pricediv"><label class="pprice">"""+a(listphone[5]["Product_price"])+"""</label></div></div>


        </div>
        
        <div class="divelectronic">
        <label class="lblelectronic">Elektronik</label>
        </div>
        <div class="homeprdct">
                <div target="_blank" class="homeprd"><img src="""+listphone[0]["Product_image"]+"""><a href="""+listphone[0]["Product_link"]+""">"""+listphone[0]["Product_name"].title()+"""</a><div class="pricediv"><label class="pprice">"""+a(listphone[0]["Product_price"])+"""</label></div></div>
            <div class="homeprd"><img src="""+listphone[1]["Product_image"]+"""><a href="""+listphone[1]["Product_link"]+">"+listphone[1]["Product_name"].title()+"""</a><div class="pricediv"><label class="pprice">"""+a(listphone[1]["Product_price"])+"""</label></div></div>
            <div class="homeprd"><img src="""+listphone[2]["Product_image"]+"""><a href="""+listphone[2]["Product_link"]+">"+listphone[2]["Product_name"].title()+"""</a><div class="pricediv"><label class="pprice">"""+a(listphone[2]["Product_price"])+"""</label></div></div>
            <div class="homeprd"><img src="""+listphone[3]["Product_image"]+"""><a href="""+listphone[3]["Product_link"]+">"+listphone[3]["Product_name"].title()+"""</a><div class="pricediv"><label class="pprice">"""+a(listphone[3]["Product_price"])+"""</label></div></div>
            <div class="homeprd"><img src="""+listphone[4]["Product_image"]+"""><a href="""+listphone[4]["Product_link"]+">"+listphone[4]["Product_name"].title()+"""</a><div class="pricediv"><label class="pprice">"""+a(listphone[4]["Product_price"])+"""</label></div></div>
            <div class="homeprd"><img src="""+listphone[5]["Product_image"]+"""><a href="""+listphone[5]["Product_link"]+">"+listphone[5]["Product_name"].title()+"""</a><div class="pricediv"><label class="pprice">"""+a(listphone[5]["Product_price"])+"""</label></div></div>
            
        </div>
        </div>
        <div class="spacediv"></div>
        <script>

            window.addEventListener("wheel", function(event) {
          if (event.deltaY < 0) {
    window.scroll({ top: 0, behavior: 'smooth' });
  } else if (event.deltaY > 0) {
    window.scroll({ top: document.body.scrollHeight, behavior: 'smooth' });
  }
            });
        </script>
        """

        return render(request,"blog/index.html",{'text':htmtext})

    
    
def blogs(request):
    return render(request,"blog/blog.html")
def blog_details(request,id):
    return render(request,"blog/blog-details.html",{"id":id})

def kayit(request):
    return render(request,"blog/kayit.html")


def urunara(request):

   
    context ={}
    context['form']= ProductForm()

    import os
    import re
    import sys      
    import time
    import sys

    import mysql.connector
    import pandas as pd
    from numpy import r_
    import sqlite3
   
    sqliteConnection = sqlite3.connect('db.sqlite3')
    cursor = sqliteConnection.cursor()
    
    try:
        productn1=request.GET["urun"].lower().strip()
        if len(productn1)==0:
            return render(request,'blog/urunara.html',{'form':context['form']})
    except:
        return render(request,'blog/urunara.html',{'form':context['form']})
    
    
    productn=""
    list1=productn1.strip().replace(","," ").replace("'"," ").replace('"'," ").replace("-"," ").replace("+"," ").replace(";"," ").replace("."," ").replace("*"," ").replace("  "," ").split()
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
    panda=pd.DataFrame(mainlist)
  
 


    if len(mainlist)==0:
        htmtext='<h2 class="alert-nostock">Üzgünüz, aradığınız ürünü bulamadık.</h2>\n<h3 class="alert-nostock">modeli doğru girdiğinizden emin olun.</h3>'

    else:
        htmtext="""<table class='table'>
        <tr>
        <th>Ürün Resim</th>
        <th>Ürün Adı</th>
        <th>Ürün Fiyatı</th>
        <th>Site</th>
        </tr>
        """
        def a(price):
 
           
            plist=str(price).split(".")
           

            if len(plist[0])>3:
                try:
                    plist[0]= plist[0][:-3]+"."+plist[0][-3:] 
                except:
                    pass
                
            price=",".join(plist)+"TL"
            return price

        for m in mainlist:
            forcontrol=False
            stm=m[1].lower().replace("ı","i").replace("ü","u").replace("ö","o").replace("ç","c").replace("ğ","g").replace("ş","s")
            if "kayis" in stm or "kordon" in stm or  "koruyucu" in stm or "cover" in stm  or "donusturucu" in stm  or "kilif" in stm or "case" in stm or "kablo" in stm or "kapak" in stm or "tutucu" in stm or "sarj" in stm or "icin" in stm or "kilif" in stm or "adaptor" in stm: 
            
                continue
            if "saat" not in list1:
                if "saat" in stm:
                    continue
            #{% static 'logo/image.ext' %}
            cntname=m[1].replace(","," ").replace("'"," ").replace('"'," ").replace("-"," ").replace("+"," ").replace(";"," ").replace("."," ").replace("*"," ").split()
            wordcontrol=False
            linklist=["https://www.trendyol.com/","https://www.hepsiburada.com/","https://www.amazon.com.tr/","https://cdn.dsmcdn.com/","https://productimages.hepsiburada.net/","https://m.media-amazon.com/","https://adservice.hepsiburada.com/"]
            breakfor=False
            for i in linklist:
                if i in str(m[4][0:46]):
                    break
                if i==linklist[-1]:
                    if i not in str(m[4][0:46]):
                        breakfor=True
                    

                

            if breakfor==True:
                continue
                        
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
                  
            source="/static/logo/"+m[5]+".jpg"
            htmtext+='<tr>\n'
            htmtext+='<td class="productimg"><img id="myImg" onclick="replyclick(this.src)"  src="'+str(m[4])+'"></td>\n'
            htmtext+='<td class="prdname"><a target="_blank" href="'+str(m[3])+'">'+str(m[1]).title()+'<a></td>\n'

            htmtext+='<td    class="price">'+a(m[2])+'</td>\n'

           
            htmtext+='<td class="seller"><img width="100" height="75"  src="'+source+'"></td>\n'
            htmtext+='</tr>\n'

    htmtext+='</table>\n'

    try:
 
        
        return render(request,"blog/urunara.html",{'form':context['form'],'text':htmtext})
    except:
        return render(request,'blog/urunara.html',{'form':context['form']})


def register_request(request):
    if request.user.is_authenticated:
        return redirect("/index")
    else:
        if request.method=="POST":
            username = request.POST['username']
        #   email = request.POST['email']
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            #password = request.POST['password']
            #repassword = request.POST['repassword']
            password="test123"
            repassword="test123"
            if password == repassword:
                if len(firstname)<2:
                    return render(request,"blog/register.html",{"error":"isim uygun değil"})
                if len(lastname)<2:
                    return render(request,"blog/register.html",{"error":"soyisim uygun değil"})
        #       if len(email)<8 and "@" not in email:
        #           return render(request,"blog/register.html",{"error":"mail adresiniz geçersiz"})
                if len(username)<5:
                    return render(request,"blog/register.html",{"error":"kullanıcı adınız 5 haneden kısa"})
                #if len(password)<8:
                #    return render(request,"blog/register.html",{"error":"Şifreniz 8 haneden kısa"})
                if User.objects.filter(username=username).exists():
                    return render(request,"blog/register.html",{"error":"Kullanıcı adı kullanımda."})
                else:
                    #if User.objects.filter(email=email).exists():
                    #    return render(request,"blog/register.html",{"error":"email kullanımda."})
                    
                        user =User.objects.create_user(username=username,email="test@test.com",first_name=firstname,last_name=lastname,password=password)
                        user.save()
                        return redirect("/login")
            else:
                return render(request,"blog/register.html",{"error":"parola eşleşmiyor."})
        else:
            return render(request,'blog/register.html')
def getproducts(request):
    pass

def login_request(request):
    if request.user.is_authenticated:
        return redirect("/index")
    else:
        print(str(request))
        print(type(request))
        if request.method =="POST":
            username = request.POST["username"]
            
            password = request.POST["password"]
            user = authenticate(request,username = username,password = "test123")
            if user is not None:
                login(request,user)
                return redirect("/index")
            else:
                return render(request,"blog/login.html",{"error":"Kullanıcı adı veya şifre yanlış."})
        return render(request,"blog/login.html")
        
def logout_request(request):
    logout(request)
    return redirect("/index")
def admin_change_list(request):
    return render(request,'blog/change_list.html')

def hepsiburada():
    from selenium import webdriver
    import time
    import pandas as pd
    from selenium.webdriver.common.by import By
    import re
    import mysql.connector
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver import Keys
    from blog.models import Products

    """
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="products"
    )

    cursor=mydb.cursor()
    def insertsql(v1,v2,v3,v4,v5):
        sql="INSERT INTO productstable2 (Product_name, Product_price, Product_link, Product_image, Product_site) VALUES (%s, %s, %s, %s, %s)"
        val=(v1,v2,v3,v4,v5)
        try:
            cursor.execute(sql, val)    
        except:
            sql2="UPDATE productstable2 SET Product_name=%s, Product_price=%s, Product_image=%s, Product_site=%s WHERE Product_link=%s"
            val2=(v1,v2,v4,v5,v3)
            cursor.execute(sql2, val2)
        mydb.commit()
    """
    b1="asdasdas"
    b2=500
    b3="sdfdsfsd"
    b4="dsfsdfsdfsdf344"
    b5="435gfhnbvnvb"

    options = webdriver.ChromeOptions() 
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    options.add_argument("--disable-gpu")
    options.add_argument("--headless")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument('--window-size=1920,1080')

    driver=webdriver.Chrome(options=options)
    driver.execute_script("document.body.style.zoom='50%'")

    brands=["samsung", "apple", "xiaomi", "huawei", "oppo","lg","oneplus","jbl","sony","steelseries","sennheiser","msi","lenovo","razer","logitech","philips","monster","hp","asus","benq","casper",
    "acer","aoc","dell","canon","anker","nikon","everest","gamepower","bosch","fakir","general mobile","htc","intel","microsoft","nokia","toshiba","kingston","hyperx","vestel","xp"]
    products=[]
    product_data=[]
    list1=[]  
    list2=[]
    list3=[]

        


    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    page1product1=""
    for br in brands:
        x=0
        z=1
        while z==1:
            x+=1
            pd2=br.replace(" ","%20")
            link="https://www.hepsiburada.com/ara?q="+pd2+"&sayfa="+str(x)
            driver.get(link)
            time.sleep(0.5)
            driver.execute_script("window.scrollTo(0,500)")
            time.sleep(0.2)
            driver.execute_script("window.scrollTo(500,1000)")
            time.sleep(0.2)
            driver.execute_script("window.scrollTo(1000,1500)")
            time.sleep(0.2)
            driver.execute_script("window.scrollTo(1500,2000)")
            time.sleep(0.2)
            driver.execute_script("window.scrollTo(2000,2500)")
            time.sleep(0.2)
            print("1")
                
        
            
            p_class= driver.find_elements(By.XPATH, '//li[@class="productListContent-zAP0Y5msy8OHn5z7T_K_"]')[0:24]


            
            if x==1:
                page1product1=driver.find_element(By.XPATH,'//ul/li/div/a[@href]').get_attribute('href')    
            l=0                                                  
            for product in p_class:
                print("---------------")
                l+=1
                try:
                    
                    price= product.find_element(By.XPATH,'.//div[@data-test-id="price-current-price"]').text[:-3].replace(".","").replace(",",".")
                    
                    info= product.find_element(By.XPATH,'.//h3[@data-test-id="product-card-name"]').text.lower() 
                    pic= product.find_element(By.XPATH,'.//div[@data-test-id="product-image-image"]/picture/img')
                    picurl=pic.get_attribute('src')
                    url=product.find_element(By.XPATH,'.//a[contains(@class,"moria-ProductCard")]')
                    link=url.get_attribute('href')  
                    site="HepsiBurada"
                    print(picurl)
                    print(link)
                    print(l)
                    if l==24:
                    
                        print("breaK")
                        break
                except:continue #
                #product = Products(Product_name=info,Product_price=price,Product_link=link,Product_image=picurl,Product_site=site) # create new model instance
                
                            #product = Products(Product_name=info,Product_price=price,Product_link=link,Product_image=picurl,Product_site=site) # create new model instance
                Products.objects.update_or_create(Product_link=link,defaults={"Product_name":info,"Product_price":price,"Product_link":link,"Product_image":picurl,"Product_site":site}) 
                
            print("3")
            print("3")






