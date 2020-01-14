from django import template

register = template.Library()


@register.filter(name='add_class')
def add_class(value, arg):
    return value.as_widget(attrs={'class': arg})


@register.filter(name='add_attributes')
def add_attributes(value, arg):
    attrs = value.field.widget.attrs

    data = arg.replace(' ', '')

    kvs = data.split(',')

    for string in kvs:
        kv = string.split(':')
        attrs[kv[0]] = kv[1]
    # rendered = str(value)
    return value.as_widget(attrs=attrs)


@register.filter(name='add_placeholder')
def add_placeholder(value, arg):
    return value.as_widget(attrs={'placeholder': arg})
