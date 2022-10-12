from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from Wand.models import Shafts, Tips
from Wand.serializers import ShaftsSerializer, TipsSerializer

# Create your views here.

@csrf_exempt
@api_view(['POST', 'GET', "PUT", "DELETE"])
def tipsApi(request,id=0):
    if request.method=="GET":
        tips = Tips.objects.all()
        tips_serializer=TipsSerializer(tips,many=True)
        return JsonResponse(tips_serializer.data,safe=False)
    elif request.method=="POST":
        tip_data = JSONParser().parse(request)
        tips_serializer = TipsSerializer(data=tip_data)
        if tips_serializer.is_valid():
            tips_serializer.save()
            return Response("Added Successfully", status=status.HTTP_201_CREATED)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=="PUT":
        tip_data = JSONParser().parse(request)
        tip = Tips.objects.get(TipId=tip_data['TipId'])
        tips_serializer = TipsSerializer(tip, data=tip_data)
        if tips_serializer.is_valid():
            tips_serializer.save()
            return JsonResponse("Modified Successfully",safe=False)
        return JsonResponse("Failed to Modify",safe=False)
    elif request.method=="DELETE":
        tip = Tips.objects.get(TipId=id)
        tip.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def shaftsApi(request,id=0):
    if request.method=="GET":
        shafts = Shafts.objects.all()
        shafts_serializer=ShaftsSerializer(shafts,many=True)
        return JsonResponse(shafts_serializer.data,safe=False)
    elif request.method=="POST":
        shaft_data = JSONParser().parse(request)
        shafts_serializer = ShaftsSerializer(data=shaft_data)
        if shafts_serializer.is_valid():
            shafts_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=="PUT":
        shaft_data = JSONParser().parse(request)
        shaft = Shafts.objects.get(ShaftId=shaft_data['ShaftId'])
        shafts_serializer = ShaftsSerializer(shaft, data=shaft_data)
        if shafts_serializer.is_valid():
            shafts_serializer.save()
            return JsonResponse("Modified Successfully",safe=False)
        return JsonResponse("Failed to Modify",safe=False)
    elif request.method=="DELETE":
        shaft = Shafts.objects.get(ShaftId=id)
        shaft.delete()
        return JsonResponse("Deleted Successfully",safe=False)
