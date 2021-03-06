# Generated by Django 4.0.5 on 2022-06-30 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0007_alter_recipe_published'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quote',
            options={'verbose_name': 'Цитата', 'verbose_name_plural': 'Цитаты'},
        ),
        migrations.AlterField(
            model_name='recipe',
            name='tags',
            field=models.ManyToManyField(blank=True, to='recipe.tag', verbose_name='Ключевые слова'),
        ),
    ]
