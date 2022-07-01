from django import template
from recipe.models import Quote
from random import randint


register = template.Library()


@register.simple_tag()
def get_quote():
    return Quote.objects.get(pk=randint(1, Quote.objects.count())).quote
