from rest_framework import serializers
from .models import Student,Category,Book
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username","password"]

    def create(self,validated_data):
        user = User.objects.create(username = validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # fields = ["name","age"]
        # exclude = ['id']
        fields = '__all__'

    def validate(self, data):
        if data['age']<18:
            raise serializers.ValidationError({"error":"Age can't be less then 18"})
        
        if data['name']:
            for n in data['name']:
                if n.isdigit():
                    raise serializers.ValidationError({"error":"Name Can't be numeric"})
        
        return data


# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = "__all__"


# class BookSerializer(serializers.ModelSerializer):
#     category = CategorySerializer()
#     class Meta:
#         model = Book
#         fields = "__all__"



from rest_framework import serializers
from .models import Item, Category, Size, Price

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'

class PriceSerializer(serializers.ModelSerializer):
    size = serializers.SlugRelatedField(slug_field='name', queryset=Size.objects.all())

    class Meta:
        model = Price
        fields = ('size', 'price')

class ItemSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', queryset=Category.objects.all())
    prices = PriceSerializer(many=True, write_only=True)


    class Meta:
        model = Item
        fields = '__all__'

    def create(self, validated_data):
        prices_data = validated_data.pop('prices')
        category_name = validated_data.pop('category')
        category = Category.objects.get(name=category_name)
        item = Item.objects.create(category=category, **validated_data)

        for price_data in prices_data:
            size_name = price_data['size']

            print(type(size_name.name))
            size = Size.objects.filter(name=size_name.name).first()  # Use filter and first to handle non-existent size
            print(size.id)
            if size is None:
                raise serializers.ValidationError(f"Size matching query does not exist: {size_name}")
            Price.objects.create(item=item, size=size, price=price_data['price'])

        return item





