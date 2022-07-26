from django.db import models


# Create your models here.
class Tag(models.Model):
    name = models.CharField('태그 이름', max_length=50, unique=True)

    class Meta:
        db_table = 'tag'
        ordering = ['-id']
        verbose_name = '태그'
        verbose_name_plural = '태그들'

    def __str__(self):
        return self.name
