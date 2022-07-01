from django.db import models
from django.urls import reverse


class Tag(models.Model):
    slug = models.SlugField(max_length=150, unique=True, verbose_name='Уникальное имя')
    title = models.CharField(max_length=150, verbose_name='Наименование')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def get_absolute_url(self):
        return reverse('tag_view', kwargs={'tag_slug': self.slug})


class Category(models.Model):
    slug = models.SlugField(max_length=150, unique=True, verbose_name='Уникальное имя')
    title = models.CharField(max_length=150, verbose_name='Наименование')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('category_view', kwargs={'category_slug': self.slug})


class Recipe(models.Model):
    slug = models.SlugField(max_length=255, unique=True, verbose_name='Уникальное имя')
    title = models.CharField(max_length=255, verbose_name='Наименование')
    short_desc = models.CharField(max_length=255, verbose_name='Примечание')
    proportions = models.TextField(verbose_name='Ингредиенты')
    content = models.TextField(verbose_name='Пошаговый рецепт')
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True, verbose_name='Изображение')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    author = models.CharField(max_length=50, verbose_name='Автор')
    views = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')
    published = models.BooleanField(default=False, verbose_name='👀')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')
    tags = models.ManyToManyField(Tag, verbose_name='Ключевые слова', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def get_absolute_url(self):
        return reverse('recipe_view', kwargs={'recipe_slug': self.slug})


class Quote(models.Model):
    quote = models.CharField(max_length=255, verbose_name='Цитата')

    def __str__(self):
        return self.quote

    class Meta:
        verbose_name = 'Цитата'
        verbose_name_plural = 'Цитаты'