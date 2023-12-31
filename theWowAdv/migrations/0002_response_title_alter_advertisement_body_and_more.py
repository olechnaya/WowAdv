# Generated by Django 4.2.3 on 2023-07-18 10:38

from django.db import migrations, models
import django.db.models.deletion
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('theWowAdv', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='title',
            field=models.CharField(default='Заголовок коммента', max_length=255),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='body',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='Содержание'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='response',
            name='responseAdvertisement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responses', to='theWowAdv.advertisement'),
        ),
    ]
