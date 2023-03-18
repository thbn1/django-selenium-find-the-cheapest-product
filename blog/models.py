from django.db import models

class Products(models.Model):

    id=models.BigAutoField(auto_created=True,primary_key=True,unique=True)
    Product_name=models.TextField(max_length=250,verbose_name="Ürün Adı",null=False,help_text="Ürün adını giriniz.")
    Product_price=models.DecimalField(max_digits=10,verbose_name="Ürün Fiyatı",null=True,decimal_places=2)
    Product_link=models.URLField(max_length=250,verbose_name="Ürün Link",null=False,unique=True)
    Product_image=models.URLField(max_length=250,verbose_name="Ürünün Resmi",null=True)
    Product_site=models.CharField(max_length=30,verbose_name="Ürünün Satıcısı",null=False )
    Product_control=models.DateTimeField(auto_now_add=True)
    active=models.BooleanField(default=True)
class Site(models.Model):
    name = models.CharField(null=False, blank=False, max_length=256, unique=True)
    script = models.CharField(null=False, blank=False, max_length=256)
    def __unicode__(self):
       return u"{0}".format(self.name)
