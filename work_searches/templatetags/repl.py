from django import template

register = template.Library()


@register.filter
def repl(self):
    return self.replace(", "," • ")