from django.db import models
from django.core.validators import RegexValidator


# код, специальность, профили, уровень подготовки
# нужен валидатор

class Level(models.Model):
    level = models.TextField()


class Course(models.Model):
    code = models.CharField(
        max_length=8,
        validators=[
            RegexValidator(
                regex=r'^\d{2}\.\d{2}\.\d{2}$',
                message='Строка должна быть в формате "01.03.02".'
            )
        ]
    )
    speciality = models.TextField()
    profs = models.TextField()
    level = models.ForeignKey(
        Level,
        verbose_name='Уровень подготовки',
        on_delete=models.CASCADE,
        related_name='courses'
    )

