# Generated by Django 4.2.3 on 2023-07-19 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theWowAdv', '0004_alter_response_approved_alter_response_text_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='response',
            old_name='approved',
            new_name='isApproved',
        ),
    ]
