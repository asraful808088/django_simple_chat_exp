import json

from channels.consumer import AsyncConsumer
from channels.exceptions import StopConsumer


class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        await self.channel_layer.group_add("x",self.channel_name)
        await self.send({
            'type':'websocket.accept',
        })

    async def websocket_disconnect(self,event):
        await self.channel_layer.group_discard("x",self.channel_name)
        raise StopConsumer()

    async def websocket_receive(self,event):
        parseJson = json.loads(event['text'])
        userId = self.channel_name
        print(userId)
        if parseJson["type"] == "get_id":
            await self.send({
             'type':'websocket.send',
             'text': json.dumps({
                    'type':"init",
                    'userId':userId
                      })
            })
        else:
            
            await self.channel_layer.group_send('x',{
                'type':'chat.message',
                'message':parseJson['message'],
                'senderId':parseJson['sender']

            })



    async def chat_message(self,event):
            await self.send({
             'type':'websocket.send',
             'text':json.dumps({
                'type':"send_message",
                'sender':event['senderId'],
                'message':event['message']
             })
            })





