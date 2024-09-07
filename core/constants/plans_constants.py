from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

USERNAME_REGEX = RegexValidator(
    regex=r'^[\w._]+$',
    message=_(
        'El nombre de usuario solo puede contener letras, números, puntos y guiones bajos.'
    ),
)

FOLDER_PATH = [
    ('components', 'Components'),
    ('styles', 'Styles'),
]

FILE_TYPES = [
    ('.jsx', 'JavaScript XML'),
    ('.css', 'Cascading Style Sheets'),
]

PLANS = [
    ('free', 'Free'),
    ('basic', 'Basic'),
    ('expert', 'Expert'),
]
