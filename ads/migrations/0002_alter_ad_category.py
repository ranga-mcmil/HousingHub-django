# Generated by Django 4.1.7 on 2023-03-11 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='category',
            field=models.CharField(choices=[('1', 'Men Collection'), ('2', 'Ladies Collection'), ('3', 'Kids Collection'), ('4', 'Phones and Tablets'), ('5', 'Laptops'), ('6', 'Appliances and Machinery'), ('7', 'Accessories'), ('8', 'Dining and Lounge'), ('9', 'Kitchen'), ('10', 'Bedroom'), ('11', 'Bathroom'), ('12', 'Skin Care'), ('13', 'Hair Products'), ('14', 'Fragrances'), ('15', 'Cars'), ('16', 'Trucks'), ('17', 'Vehicle Parts'), ('18', 'Event Services'), ('19', 'Food Services'), ('20', 'Other Services'), ('21', 'Other'), ('22', 'Other Electronics'), ('23', 'Other Beauty and Cosmetics'), ('24', 'Other Vehicles'), ('25', 'Other Homeware')], max_length=50),
        ),
    ]
