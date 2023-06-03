from django.contrib import admin

# Register your models here.
from .models import Student,Book,Category,Item,Size,Price


admin.site.register(Student)
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Item)
admin.site.register(Size)
admin.site.register(Price)

