# Generated by Django 4.0.5 on 2022-06-27 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0003_alter_recipe_author_alter_recipe_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.CharField(max_length=255, verbose_name='Цитата')),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=150, unique=True, verbose_name='Уникальное имя'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='published',
            field=models.BooleanField(default=True, verbose_name='👀'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(max_length=150, unique=True, verbose_name='Уникальное имя'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Наименование'),
        ),
    ]
