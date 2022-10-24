import json

from asgiref.sync import async_to_sync
from channels.consumer import AsyncConsumer
from channels.generic.websocket import WebsocketConsumer


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
        print(event["text"])
        await self.channel_layer.group_send(
            self.board_room,{
                "type": "board_message",
                "text" : event["text"]

            }
        )

    async def board_message(self ,event):
        print("Once")
        await self.send({
            "type" : "websocket.send",
            "text" : event['text']
        })

    
    async def websocket_disconnect(self , event):
        print('Disconnect' , event)    
