# Generated by Django 4.1.7 on 2023-03-19 15:09

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_user_id_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pic',
            field=django_resized.forms.ResizedImageField(crop=['top', 'left'], force_format=None, keep_meta=True, quality=-1, scale=None, size=[500, 600], upload_to='images/'),
        ),
    ]
