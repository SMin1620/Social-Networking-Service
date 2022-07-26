from django.db import models

from user.models import User


# Create your models here.
class Room(models.Model):
    title = models.CharField('채팅방 이름', max_length=100, blank=True, default='')
    user = models.ManyToManyField(User)

    created_at = models.DateTimeField('생성 날짜', auto_now_add=True)

    class Meta:
        db_table = 'room'

    def __str__(self):
        return f'{self.id}, {self.title}'


class Message(models.Model):
    content = models.TextField('채팅 내용', blank=True)

    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField('생성 날짜', auto_now_add=True)

    class Meta:
        db_table = 'message'

    def __str__(self):
        return f'{self.id} // room : {self.room.title} // sender : {self.sender.email}'



