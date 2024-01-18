from django.db import models
from ..devtools.models import DevTool

# Create your models here.
class Idea(models.Model):
    title = models.CharField('제목', max_length=24)
    photo = models.ImageField('이미지', blank=True)
    content = models.TextField('아이디어 설명', max_length=200)
    interest = models.IntegerField('아이디어 관심도', default=0)
    tool = models.ForeignKey(DevTool, on_delete=models.CASCADE, verbose_name='예상 개발 툴')
    created_date = models.DateTimeField(auto_now_add = True)

    def __str__ (self):
        return self.title