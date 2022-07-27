from django import template

register = template.Library()
@register.filter(name='saludo')
def saludo(valor):
    return f"<h1 style='backgraud:green; color:white;'>Bienvenidos,(valor)</h1>"