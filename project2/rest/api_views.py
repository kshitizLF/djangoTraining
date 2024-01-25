from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics,permissions
from .serializers import CarSerializer
from .models import Car
from .forms import CarForm
import json
from django.http import JsonResponse
from rest_framework.views import APIView

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin

from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser

@api_view()
def hello(request):
    return Response({"message":"This is my first api response"})

@api_view(['GET','POST'])
def getData(request):
    '''many option tells us that we expect more than 1 row
    safe allows us to pass anything that is not a dictionary
    cars = Car.objects.get(model = "City")'''
    if request.method == 'GET':    
        cars = Car.objects.all()
        serialized = CarSerializer(cars,many = True)
        # serialized = CarSerializer(cars)
        return JsonResponse(serialized.data,safe=False,json_dumps_params={'indent':3})
    # return JsonResponse(serialized.data)
    else:
        '''when recieving json data(encoded) in http body we need to use json.loads method
         json_data = json.loads(request.body.decode('utf-8'))'''
        formData = CarForm(request.data)
        if formData.is_valid():
            data = formData.cleaned_data
            serialized = CarSerializer(data=data)
            if serialized.is_valid():
                serialized.save()
            else:
                data = "Not serialized"
        else:
            data = "Not saved"
        return JsonResponse({"message" : data})
    
@api_view(['POST'])
def postData(request):
    print(request.data)
    # json string
    data = json.loads(request.data)
    print(type(data))
    # python dictionary
    serialized = CarSerializer(data=data)
    if serialized.is_valid():
        serialized.save()
    else:
        return JsonResponse({"message":"Not Done"})
    return JsonResponse({"message":"Done"})

# class GetData(generics.ListAPIView):
#     serializer_class = CarSerializer
#     queryset = Car.objects.filter(company__contains = "d")
@api_view()
def carDelete(request,id):
    try:
        obj = Car.objects.get(id = id) 
        c = {
            "model": obj.model,
            "company":obj.company
        }
        print(obj)
        obj.delete()
        return JsonResponse({"message" : "Deleted","obj" : c})
    except:
        return JsonResponse({"message":"Couldn't Delete"})

@api_view(['POST'])
def carUpdate(request,id):
    data = json.loads(request.data)
    obj = Car.objects.get(id = id)
    serialized = CarSerializer(instance=obj,data = data)
    if serialized.is_valid():
        serialized.save()
    else:
        return JsonResponse({"message":"Data not valid"})

    return JsonResponse(serialized.data)

class CarView(APIView):
    def get(self,request,id=None,format=None):
        cars = Car.objects.all()
        serialized = CarSerializer(cars,many = True)
        return Response(serialized.data)
    
    def post(self,request,format=None):
        formData = CarForm(request.data)
        if formData.is_valid():
            data = formData.cleaned_data
            serialized = CarSerializer(data=data)
            if serialized.is_valid():
                serialized.save()
            else:
                data = "Not serialized"
        else:
            data = "Not saved"
        return Response({"message" : data})
    
    def delete(self,request,id,format=None):
        try:
            obj = Car.objects.get(id = id) 
            c = {
                "model": obj.model,
                "company":obj.company
            }
            print(obj)
            obj.delete()
            return Response({"message" : "Deleted","obj" : c})
        except:
            return Response({"message":"Couldn't Delete"})
        pass

    def put(self,request,id,format=None):
        data = json.loads(request.data)
        obj = Car.objects.get(id = id)
        serialized = CarSerializer(instance=obj,data = data)
        if serialized.is_valid():
            serialized.save()
        else:
            return Response({"message":"Data not valid"})

        return Response(serialized.data)

class CustomPermission(permissions.BasePermission):
    '''
        This method is used to achieve permission :
        user should be logged in , username == "kshitiz" or method should be get
    '''
    def has_permission(self, request, view):
        return (request.user.is_authenticated and request.user.username == "kshitiz") or request.method == 'GET'

class CarView(GenericAPIView,ListModelMixin,CreateModelMixin,UpdateModelMixin):
    serializer_class = CarSerializer
    '''
    def get(self,request):
        serialized = self.serializer_class(self.get_queryset(),many=True)
        return Response(serialized.data)    
    '''
    '''
        post create from the CreateModelMixin is used to create and save a model instance and return 201
        status code
    '''
    authentication_classes = [BasicAuthentication]
    permission_classes = [CustomPermission]
    def get_queryset(self):
        id = self.kwargs.get("pk")
        if id is None:
            return Car.objects.all()
        else:
            return Car.objects.filter(id__gte = id)
    def get(self,request,*args,**kwargs):
        # print(kwargs["pk"])
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)   
    
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)


class CarOne(GenericAPIView,RetrieveModelMixin,DestroyModelMixin):
    serializer_class = CarSerializer
    queryset = Car.objects.all()

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    
    def put(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

    
    