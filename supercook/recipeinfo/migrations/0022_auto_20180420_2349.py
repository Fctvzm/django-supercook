# Generated by Django 2.0.4 on 2018-04-20 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeinfo', '0021_category_descriptor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='descriptor',
            field=models.CharField(default='Assem', max_length=20),
        ),
    ]