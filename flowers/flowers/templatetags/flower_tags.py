from django import template
from ..models import *

register = template.Library()


@register.simple_tag
def all_categories():
    return Categories.objects.all()
