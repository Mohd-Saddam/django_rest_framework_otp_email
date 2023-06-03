from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student,Book
from .serializers import StudentSerializer,UserSerializer
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.


# @api_view(['GET'])
# def get_book(request):
#     book_obj = Book.objects.all()
#     serializer  = BookSerializer(book_obj,many=True)
#     return Response({"status":200,"data":serializer.data})



class RegisterUser(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            print(serializer.error_messages)
            return Response({"status":403,"error":serializer.errors,"messgae":"someting went wrong"})
        serializer.save()

        user = User.objects.get(username = serializer.data['username'])
        refresh = RefreshToken.for_user(user)

        return Response({"status":200,'refresh': str(refresh),'access': str(refresh.access_token),"data":serializer.data,"message":"user login successfully"})

class StudentAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


    def get(self,request):
        print(request.user)
        student_ob = Student.objects.all()
        serializer  = StudentSerializer(student_ob,many=True)
        return Response({"status":200,"data":serializer.data})


    def post(self,request):
        serializer = StudentSerializer(data=request.data)

        if not serializer.is_valid():
            print(serializer.error_messages)
            return Response({"status":403,"message":serializer.errors})
        serializer.save()

        return Response({"status":200,"data":serializer.data,"message":"data saved successfully"})


    def put(self,request):
        pass

    def patch(sefl,request):
        try:
            print("id=",id)
            student_obj = Student.objects.get(id = request.data['id'])
            serializer = StudentSerializer(student_obj,data=request.data,partial=True)

            if not serializer.is_valid():
                print("eror==",serializer.error_messages)
                return Response({"status":403,"message":serializer.errors})
            serializer.save()

            return Response({"status":200,"data":serializer.data,"message":"data updated successfully"})
        except Exception as e:
            print(e)
            return Response({"status":403,"messgae":"invalid id"})


    def delete(self,request):
        try:
            id = request.GET.get('id')
            stu_ob = Student.objects.get(id=id)
            stu_ob.delete()
            
            return Response({"status":200,"message":"deleted"})
        except Exception as e:
            return Response({"status":403,"messgae":"invalid id"})





































# @api_view(['GET'])
# def home(request):
#     student_ob = Student.objects.all()
#     serializer  = StudentSerializer(student_ob,many=True)
#     return Response({"status":200,"data":serializer.data})


# @api_view(['POST'])
# def post_student(request):
#     data = request.data
#     serializer = StudentSerializer(data=request.data)

#     if not serializer.is_valid():
#         print(serializer.error_messages)
#         return Response({"status":403,"message":serializer.errors})
#     serializer.save()

#     return Response({"status":200,"data":serializer.data,"message":"data saved successfully"})

# @api_view(['PUT'])
# def update_student(request,id):
#     try:
#         print("id=",id)
#         student_obj = Student.objects.get(id = id)
#         serializer = StudentSerializer(student_obj,data=request.data,partial=True)

#         if not serializer.is_valid():
#             print("eror==",serializer.error_messages)
#             return Response({"status":403,"message":serializer.errors})
#         serializer.save()

#         return Response({"status":200,"data":serializer.data,"message":"data updated successfully"})
#     except Exception as e:
#         print(e)
#         return Response({"status":403,"messgae":"invalid id"})

# @api_view(['DELETE'])
# def delete_student(request,id):
#     try:
#         # id = request.GET.get('id')
#         stu_ob = Student.objects.get(id=id)
#         stu_ob.delete()
        
#         return Response({"status":200,"message":"deleted"})
#     except Exception as e:
#         return Response({"status":403,"messgae":"invalid id"})


from rest_framework.views import APIView
from rest_framework import status

from rest_framework import generics
from .models import Item
from .serializers import ItemSerializer
from rest_framework.response import Response

class ItemListCreateView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        response_data = {
            'message': 'Item created successfully',
            'data': serializer.data
        }
        return Response(response_data, status=status.HTTP_201_CREATED)

class ItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer




    
class StudentGeneric(generics.ListAPIView,generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentGeneric1(generics.UpdateAPIView,generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'id'