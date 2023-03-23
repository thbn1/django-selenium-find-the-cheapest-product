from selenium import webdriver
from selenium.webdriver.common.by import By
from blog.models import Products


options = webdriver.ChromeOptions() 
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs)
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("--headless")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument('--window-size=1920,1080')

driver=webdriver.Chrome(options=options)


brands=["samsung", "apple", "xiaomi", "huawei", "oppo","lg","oneplus","jbl","sony","steelseries","sennheiser","msi","lenovo","razer","logitech","philips","monster","hp","asus","benq","casper",
"acer","aoc","dell","canon","anker","nikon","everest","gamepower","bosch","fakir","general mobile","htc","intel","microsoft","nokia","toshiba","kingston","hyperx","vestel","xp"]
brands=["samsung", "apple", "xiaomi", "huawei", "oppo","lg","msi","lenovo","razer","logitech","philips","monster","acer","aoc","dell","asus"]

products=[]
products=[]
product_data=[]
list1=[]  
list2=[]
list3=[]

    


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------


page1product1=""
for br in brands:
    x=0
    
    while True:
        x+=1
        pd2=br.replace(" ","+")
        link1="https://www.amazon.com.tr/s?k="+pd2+"&rh=n%3A12466496031%2Cp_89%3A"+pd2+"&dc&page="+str(x)
        "https://www.amazon.com.tr/s?k=casper&i=all&rh=n%3A12466496031%2Cp_89%3Acasper&dc&page=5"
        "https://www.amazon.com.tr/s?k=casper&i=all&rh=n%3A12466439031%2Cp_89%3ACasper&dc&page=6"
        driver.get(link1)
        print(link1)
        while True:
            try:

                p_class=driver.find_elements(By.XPATH,'//div[@data-component-type="s-search-result"]')

                break
            except:
                pass

        
        for product in p_class:

            try:
                print("2.5")
                price= product.find_element(By.XPATH,'.//span[@class="a-price"]').text[:-2].replace('\n',',').replace(".","").replace(",",".")
                print(price)
                info= product.find_element(By.XPATH,'.//span[@class="a-size-base a-color-base a-text-normal"]').text.lower()
                pic= product.find_element(By.XPATH,'.//div/div/div/div/div/span/a/div/img[@src]')
                picurl=pic.get_attribute('src')
                url=product.find_element(By.XPATH,'.//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]')
                link= url.get_attribute('href')
                link=link.split("/ref=")[0].split("%2Fref")[0]

                
                
            except:
                try:
                    price= product.find_element(By.XPATH,'.//span[@class="a-price"]').text[:-2].replace('\n',',').replace(".","").replace(",",".")
                    info= product.find_element(By.XPATH,'.//span[@class="a-size-base-plus a-color-base a-text-normal"]').text.lower()
                    pic= product.find_element(By.XPATH,'.//div/div/div/div/div/span/a/div/img[@src]')
                    picurl=pic.get_attribute('src')
                    url=product.find_element(By.XPATH,'.//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]')
                    link= url.get_attribute('href').split("/ref=")[0].split("%2Fref")[0]
                    


                except:
                    continue
            site="Amazon"
            print((info,price,link,picurl,site))
            print(link1)
            Products.objects.update_or_create(Product_link=link,defaults={"Product_name":info,"Product_price":price,"Product_link":link,"Product_image":picurl,"Product_site":site}) 
        if len(p_class)==0:
            break
            


