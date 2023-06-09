# Generated by Django 4.1.7 on 2023-03-19 15:13

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0004_alter_ad_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=['top', 'left'], force_format=None, keep_meta=True, quality=-1, scale=None, size=[500, 550], upload_to='images/'),
        ),
    ]
