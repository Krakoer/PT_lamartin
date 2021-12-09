from django.core.exceptions import ValidationError
import string

specials="ôùàÀêÊéèÉÈâÂûïÏîÎ'()&/:,!\"-ç?\n .\r"

def validate_letters(value):
    for c in value:
        if c not in string.ascii_letters+specials:
            # print(c)
            raise ValidationError(
                ('%(value)s contains unauthorized characters'),
                params={'value': value},
            )

def validate_alpha(value):
    for c in value:
        if c not in (string.ascii_letters+string.digits+specials):
            print(ord(c))
            raise ValidationError(
                ('%(value)s contains unauthorized characters'),
                params={'value': value},
            )

def validate_contact(value):
    for c in value:
        if c not in string.ascii_letters+specials+"@.":
            # print(c)
            raise ValidationError(
                ('%(value)s contains unauthorized characters'),
                params={'value': value},
            )