# Generated by Django 4.1.7 on 2023-03-11 18:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50)),
                ('location', models.CharField(choices=[('1', 'Harare'), ('2', 'Gweru'), ('3', 'Bulawayo'), ('4', 'Chinhoyi')], max_length=50)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('description', models.TextField(max_length=500)),
                ('status', models.CharField(choices=[('1', 'Available'), ('2', 'Not Available')], max_length=50)),
                ('beds_per_room', models.IntegerField(default=0)),
                ('baths_rooms', models.IntegerField(default=0)),
                ('girls_remaining_slots', models.IntegerField(default=0)),
                ('boys_remaining_slots', models.IntegerField(default=0)),
                ('image1', models.ImageField(upload_to='', verbose_name=models.ImageField(upload_to='images/'))),
                ('image2', models.ImageField(upload_to='', verbose_name=models.ImageField(upload_to='images/'))),
                ('image3', models.ImageField(upload_to='', verbose_name=models.ImageField(upload_to='images/'))),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('amenities', models.ManyToManyField(to='houses.amenity')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='houses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
