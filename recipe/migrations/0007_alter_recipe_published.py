# Generated by Django 4.0.5 on 2022-06-28 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0006_alter_recipe_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='published',
            field=models.BooleanField(default=False, verbose_name='👀'),
        ),
    ]
