
from django import template

register = template.Library()

@register.filter(name='are_equal')
def are_equal(value1, value2):
    print(str(value1),'====')
    print(str(value2),'====')
    return str(value1) == str(value2)