import json
from django.db import models
from django.contrib.auth.models import User
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync, sync_to_async

# Create your models here.
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    notification = models.TextField(default="asdklfasdk")
    is_seen = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        print('entered save()')
        channel_layer = get_channel_layer()
        # notification_objs = Notification.objects.filter(is_seen=False)
        data = {'count':1}
        breakpoint()
        async_to_sync(channel_layer.send)(
            "lobby", {
                "type": 'chat.message',
                "message": data
            }
        )

        super(Notification, self).save(*args, **kwargs)