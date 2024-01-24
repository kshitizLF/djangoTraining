from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .serializers import CarSerializer
from .models import Car
from .forms import CarForm
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
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
def carDelete(request,model):
    try:
        obj = Car.objects.get(model = model) 
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