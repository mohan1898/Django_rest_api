from django.db import models
class Mobile(models.Model):
    mobile_price=models.IntegerField()
    mobile_brand=models.CharField(max_length=50)
    mobile_spec=models.TextField(max_length=200)
    mobile_img=models.ImageField(upload_to='pics')
    def __str__(self):
        return self.mobile_brand
    

