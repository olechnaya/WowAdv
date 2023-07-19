from datetime import datetime, timedelta

from django.db import models
from django.contrib.auth.models import User

from django_ckeditor_5.fields import CKEditor5Field

class Advertisement(models.Model):
    CATEGORIES = [
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
    ]

    title = models.CharField('Заголовок',max_length=255)
    category = models.CharField(verbose_name='Категория', max_length=3, choices=CATEGORIES, default='T')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Создатель', related_name='advert', null=True)
    body = CKEditor5Field('Содержание', blank=True, null=True,  config_name='extends')
    # body = models.TextField('Содержание',max_length=1024)
    pub_date = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')
    exp_date = models.DateTimeField('Актуально до', null=True, blank=True)
    # responders = models.ManyToManyField(User, blank= True)
    

    class Meta:
            verbose_name = 'Объявление'
            verbose_name_plural = 'Объявления'

    def get_absolute_url(self):
        return f'/advert/{self.id}'
        # не получается работать
        #  return reverse('view_adv', args=(str(self.id)))

    def __str__(self):
        return self.title + ' | ' + str(self.author)


class Response(models.Model):
    class Meta:
        verbose_name = 'Отклик'
        verbose_name_plural = 'Отклики'
    advert = models.ForeignKey(Advertisement, related_name="responses", on_delete=models.CASCADE)
    responseUser = models.ForeignKey(User, on_delete=models.CASCADE)
    approved = models.BooleanField('Принято', default=False)
    title = models.CharField('Заголовок', max_length=255, default="", blank=True)
    text = models.TextField('Сообщение', max_length=512)
    dateCreation = models.DateTimeField(auto_now_add=True)

    # как добраться до промежуточных моделей
    # вывод имени автора

    def __str__(self): 
        try:
            return '%s - %s' % (self.advert.title, self.title)
        except:
            return self.title