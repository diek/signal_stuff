from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save

from .utils import unique_text_msg_code_generator


class UserTextMessage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user) + ":" + str(self.code)


def pre_save_txt_msg_code(instance, sender, *args, **kwargs):
    instance.code = unique_text_msg_code_generator(instance)


pre_save.connect(pre_save_txt_msg_code, sender=UserTextMessage)
