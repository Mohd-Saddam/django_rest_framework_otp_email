from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    father_name = models.CharField(max_length=100)

class Category(models.Model):
    name = models.CharField(max_length=100)

    # @staticmethod
    # def get_all_categories():
    #     return Category.objects.all()

    def __str__(self):
        return self.name
  

class Book(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    book_title = models.CharField(max_length=100)

class Size(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=255)
    fabric = models.CharField(max_length=255)
    sku = models.CharField(max_length=255)
    fitting_type = models.CharField(max_length=255)
    imported_brand = models.BooleanField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.item_id


class Price(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.price
