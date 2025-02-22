from django import template
import datetime

register = template.Library()

@register.filter
def datetime_local_format(value):
    if isinstance(value, datetime.datetime):
        return value.strftime('%Y-%m-%dT%H:%M')
    return value