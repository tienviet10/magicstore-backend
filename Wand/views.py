from datetime import date

from django.db import connection
from django.db.models import Q, Sum
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from Wand import serializers
from Wand.models import Endcaps, Shafts, Tips, Topcaps
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
            return Response(tips_serializer.data, status=status.HTTP_201_CREATED)
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
        # return JsonResponse("Deleted Successfully",safe=False)
        return Response(status=status.HTTP_204_NO_CONTENT)

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


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

@api_view(['GET', "PUT", "DELETE"])
@csrf_exempt
def tips_detail(request, id):
    # list(Tips.objects.values('TipName'))
    # list(Tips.objects.values('TipName').distinct())
    # list(Tips.objects.all().filter(~Q(TipName="green")).values())
    # list(Tips.objects.all().filter(TipName__contains='orange').values())
    # list(Tips.objects.all().filter(TipName__contains='orange').values().order_by('TipId'))
    # tips = list(Tips.objects.all().filter(TipName__contains='orange').values() | Tips.objects.all().filter(TipName__startswith='o').values())
    # tips = list(Tips.objects.all().filter(Q(TipName__contains='orange') | Q(TipName__startswith='o')).values())
    # tips = list(Tips.objects.all().filter(Q(TipId=9) & Q(TipName__startswith='w')).values())
    # tips = list(Tips.objects.all().values_list("TipName").union(Shafts.objects.all().values_list("ShaftName")))
    # tips = list(Tips.objects.exclude(TipName='orange').values())
    # tips = list(Tips.objects.exclude(TipId__gt=5).values())
    # tips = list(Tips.objects.filter(TipId=5).only("TipName"))
    # tips = Tips.objects.filter(TipId__gt=5).aggregate(totalID=Sum('TipId'))['totalID']
    
    # tips = Tips.objects.all()
    # print(tips.query)  

    # tips = Shafts.objects.raw('SELECT * FROM "Wand_shafts"')[:2]
    # for p in tips:
    #     print(p)
    

    ###------------------------------------------------------------------------------------
    # cursor = connection.cursor()
    # cursor.execute('SELECT "TipName" FROM "Wand_tips" WHERE NOT ("TipId" > 5)')
    # # r = cursor.fetchone()
    # # r = cursor.fetchall()
    # r = dictfetchall(cursor)
    # print(r)  
    # print(connection.queries)


    ###------------------------------------------------------------------------------------
    # p1 = Endcaps(MadeOf='woof', Color='brown')
    # p1.save()

    # p2 = Topcaps(endcaps = p1, SerialNumber=90324278)
    # p2.save()

    # print(p2.endcaps)
    # print(p1.topcaps)

    # endcaps = Endcaps.objects.all()
    # for p in endcaps:
    #     print(p.topcaps.SerialNumber)

    # topcaps = Topcaps.objects.all()
    # for t in topcaps:
    #     print(t.endcaps.Color)

    ###------------------------------------------------------------------------------------
    for t in Endcaps.objects.all().select_related('topcaps'): 
        print(t)
        print(t.topcaps)

    try:
        tip = Tips.objects.get(TipId=id)
    except Tips.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = TipsSerializer(tip)
        return Response(serializer.data)

