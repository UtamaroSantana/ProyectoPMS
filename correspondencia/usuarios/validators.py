from django.core.exceptions import ValidationError


def valor_minimo_subtitulo(value):
    if not len(value) >= 2:
        raise ValidationError('Mínimo 2 caracteres')

def solo_Alphabeto(value):
    print(type(value))
    if not value.isalpha():
        raise ValidationError('Solo se permiten caracteres')

def valor_minimo_titulo(value):
    if not len(value) >= 4:
        raise ValidationError('Mínimo 4 caracteres')