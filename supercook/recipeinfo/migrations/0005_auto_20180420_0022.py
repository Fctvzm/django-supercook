# Generated by Django 2.0.4 on 2018-04-19 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipeinfo', '0004_auto_20180420_0020'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='shoplist',
            unique_together={('recipe', 'ingredient', 'amount')},
        ),
    ]