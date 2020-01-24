from django.core.exceptions import ValidationError

def validate_email(value):
    if not "@" in value:
        raise ValidationError("A valid email must be entered")
    else:
        return value
