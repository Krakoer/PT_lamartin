from django import template

register = template.Library()

@register.filter(name="range")
def my_range(value, arg):
    return list(range(int(value), int(arg)))