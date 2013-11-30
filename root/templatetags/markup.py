
import markdown2
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(is_safe=True)
@stringfilter
def markdown(value, arg=None):
    return mark_safe(markdown2.markdown(value,safe_mode=True))

