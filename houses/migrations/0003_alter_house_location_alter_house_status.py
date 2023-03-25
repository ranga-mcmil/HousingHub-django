# Generated by Django 4.1.7 on 2023-03-12 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0002_alter_house_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='location',
            field=models.CharField(choices=[('Harare', 'Harare'), ('Gweru', 'Gweru'), ('Bulawayo', 'Bulawayo'), ('Chinhoyi', 'Chinhoyi')], max_length=50),
        ),
        migrations.AlterField(
            model_name='house',
            name='status',
            field=models.CharField(choices=[('Available', 'Available'), ('Not Available', 'Not Available')], max_length=50),
        ),
    ]