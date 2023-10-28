from django import template

register = template.Library()

# value -> variable from context dictionary
# arg -> any additional arg
#@register.filter(name='cuts')
def cuts(value,arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg,'')

# First way to register filter
# Passing function "cuts" in another function call
register.filter('cuts',cuts)

# Second way to register filter
# Using decorators
# uncomment line 7
