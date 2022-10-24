
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from TicTacToe.models import TicTacToe
from TicTacToe.serializers import TicTacToeSerializer

# Create your views here.

@csrf_exempt
@api_view(['POST', 'GET', "PUT", "DELETE"])
def tictactoe(request,id=0):
    # TicTacToe.objects.create(CurrentPlayer="X", CurrentBoard=['', 'X', '','', '', '','', '', ''])
    # print(TicTacToe.objects.filter(TicTacToeId=1))

    if request.method=="GET":
        tictac = TicTacToe.objects.get(TicTacToeId=5)
        serializer = TicTacToeSerializer(tictac)
        return Response(serializer.data)
    elif request.method=="POST":
        tictactoe_data = JSONParser().parse(request)
        tictactoe_serializer = TicTacToeSerializer(data=tictactoe_data)
        if tictactoe_serializer.is_valid():
            tictactoe_serializer.save()
            return Response(tictactoe_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=="PUT":
        tictactoe_data = JSONParser().parse(request)
        tictactoe = TicTacToe.objects.get(TicTacToeId=5)
        tictactoe_serializer = TicTacToeSerializer(tictactoe, data=tictactoe_data)
        if tictactoe_serializer.is_valid():
            tictactoe_serializer.save()
            return JsonResponse("Modified Successfully",safe=False)
        return JsonResponse("Failed to Modify",safe=False)
    elif request.method=="DELETE":
        pass

