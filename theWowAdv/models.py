from datetime import datetime, timedelta

from django.db import models
from django.contrib.auth.models import User

from django_ckeditor_5.fields import CKEditor5Field


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


class Profile(models.Model):
    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True,upload_to="images/profile/")
    website_url = models.CharField('Веб-сайт',max_length=255,null=True, blank=True)
    mail_url = models.CharField('Ссылка на Mail аккаунт',max_length=255,null=True, blank=True)
    vk_url = models.CharField('Ссылка на Вконтакте аккаунт',max_length=255,null=True, blank=True)
    ok_url = models.CharField('Ссылка на Одноклассники аккаунт',max_length=255,null=True, blank=True)

    def __str__(self):
        return str(self.user)

class Advertisement(models.Model):    
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
    isApproved = models.BooleanField('Принято', default=False)
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
        
class CategorySubscription(models.Model):
    class Meta:
        verbose_name = 'Подписки по категориям'
        verbose_name_plural = 'Подписки по категориям'
    name = models.CharField(verbose_name='Категория', max_length=3, choices=CATEGORIES, default='T')
    user = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):        
        return f'{self.name} - {self.user.username}'
    
class NewsLetterSubscribedUsers(models.Model):
    class Meta:
        verbose_name = 'Новостная подписка'
        verbose_name_plural = 'Новостные подписки'

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=100)
    dateCreation = models.DateTimeField('Date created', auto_now_add=True)

    def __str__(self):
        return self.email