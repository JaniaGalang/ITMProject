from django import template

register = template.Library()

@register.filter
def chunks(value, size):
    """
    Break a list into chunks of a given size.
    """
    for i in range(0, len(value), size):
        yield value[i:i + size]

@register.filter
def dictkey(value, arg):
    """Gets the value of a dictionary key."""
    reservation = value.get(arg)
    if reservation:
        return reservation.plate_number
    return ""

