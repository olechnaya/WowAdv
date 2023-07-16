from django.db import models
from django.contrib.auth.models import User

class Advertisement(models.Model):
    # tanks: str = "TNK"
    # hills: str = "HL"
    # dds: str = "DD"
    # traders: str = "TRD"
    # gildmasters: str = "GLDM"
    # questgivers: str = "QTG"
    # blacksmith: str = "FM"
    # leathermaster: str = "LM" 
    # : str = "PM"
    # : str = "WM"
    
    # CATEGORIES = (
    #     (tanks, "Танки"),
    #     (hills, "Хилы"),
    #     (dds, "ДД"),
    #     (traders, "Торговцы"),
    #     (gildmasters, "Гилдмастеры"),
    #     (questgivers, "Квестгиверы"),
    #     (blacksmith, "Кузнецы"),
    #     (leathermaster, "Кожевники"),
    #     ('PM','Зельевары'),
    #     ('WM','Мастера заклинаний'),

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
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
            verbose_name = 'Объявление'
            verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.title + ' | ' + str(self.author)