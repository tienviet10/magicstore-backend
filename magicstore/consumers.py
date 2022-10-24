import json

from asgiref.sync import sync_to_async
from channels.consumer import AsyncConsumer
from TicTacToe.models import TicTacToe
from TicTacToe.serializers import TicTacToeSerializer


class BoardConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        board_room = "boardroom1"
        self.board_room = board_room
        await self.channel_layer.group_add(
            board_room, self.channel_name
        )
        await self.send({
            "type" : "websocket.accept"
        })

    async def websocket_receive(self , event):
        data = json.loads(event["text"])
        await self.channel_layer.group_send(
            self.board_room,{
                "type": "board_message",
                "text" : event["text"]

            }
        )
        await self.save_board(data)     

    async def board_message(self ,event):
        await self.send({
            "type" : "websocket.send",
            "text" : event['text']
        })

    
    async def websocket_disconnect(self , event):
        print('Disconnect' , event)   

    @sync_to_async
    def save_board(self, savedData):
        board = TicTacToe.objects.get(TicTacToeId=5)
        board_serializer = TicTacToeSerializer(board, data={
            "CurrentBoard": savedData["marks"],
            "PlayerX": savedData["playerX"],
            "PlayerO": savedData["playerO"],
            "CurrentPlayer" : savedData["marker"],
        })
        if board_serializer.is_valid():
            board_serializer.save()
      
