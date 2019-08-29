from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from src.models.channel.models import Channel
from src.models.message.models import Message
import json



class ConsumerComment(AsyncConsumer):

    async def websocket_connect(self, event):
        self.id_channel = self.scope['url_route']['kwargs']['pk']
        self.current_channel = Channel.objects.get(id=self.id_channel)

        self.channel_pk = str(self.current_channel.pk)

        await self.channel_layer.group_add(
            self.channel_pk,
            self.channel_name,
        )

        await self.send({
            "type": "websocket.accept",
        })


    async def websocket_receive(self, event):
        print('RECEIVE : ', event)
        text_comment = event.get('text', None)
        if text_comment is not None:
            load_data   = json.loads(text_comment)
            message     = load_data.get('message')
            user        = self.scope['user']
            response = {
                'message': message,
                'username': user.username,
            }
            await self.create_comment(user, message)
            await self.channel_layer.group_send(
                    self.channel_pk,
                {
                    "type": "msg_comment",
                    "text": json.dumps(response),
                }
            )

    async def msg_comment(self, event):
        await self.send({
            "type": "websocket.send",
            "text": event["text"]
        })


    @database_sync_to_async
    def create_comment(self, user, msg):
        Message.objects.create(who=user, text=msg, channel=self.current_channel)

    async def websocket_disconnect(self, event):
         await self.channel_layer.group_discard(
            self.channel_pk,
            self.channel_name,
        )
