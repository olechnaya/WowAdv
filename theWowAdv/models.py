from datetime import datetime, timedelta

from django.db import models
from django.contrib.auth.models import User

class Advertisement(models.Model):
    CATEGORIES = (
        ('T','Танки'),
        ('HM','Хилы'),
        ('DD','ДД'),
        ('TrM','Торговцы'),
        ('GM','Гилдмастеры'),
        ('QG','Квестгиверы'),
        ('FM','Кузнецы'),
        ('LM','Кожевники'),
        ('PM','Зельевары'),
        ('WM','Мастера заклинаний'),
    )

    title = models.CharField(max_length=255)
    category = models.CharField(verbose_name='Категория', max_length=3, choices=CATEGORIES, default='T')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Создатель', related_name='advert', null=True)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')
    exp_date = models.DateTimeField('Актуально до', null=True, blank=True)
    # responders = models.ManyToManyField(User, blank= True)
    

    class Meta:
            verbose_name = 'Объявление'
            verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.title + ' | ' + str(self.author)



class Response(models.Model):
    class Meta:
        verbose_name = 'Отклик'
        verbose_name_plural = 'Отклики'
    responseAdvertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    responseUser = models.ForeignKey(User, on_delete=models.CASCADE)
    approved = models.BooleanField('Принято', False)
    text = models.TextField(max_length=512)
    dateCreation = models.DateTimeField(auto_now_add=True)

    # как добраться до промежуточных моделей
    # вывод имени автора

    def __str__(self): 
        try:
            return self.commentPost.author.name.userName
        except:
            return self.commentUser.username