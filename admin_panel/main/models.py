from django.db import models
from .validator import phone_validator


class ForexSignal(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    price = models.CharField(max_length=20)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "forex signal"
        verbose_name_plural = "forex signals"


class GetStart(models.Model):
    full_name = models.CharField(verbose_name="Ism Familya", max_length=255)
    username = models.CharField(verbose_name="Foydalanuvchi nomi", max_length=50)
    user_id = models.PositiveBigIntegerField(verbose_name="ID", unique=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Bot foydalanuvchisi"
        verbose_name_plural = "Bot foydalanuvchilari"



class HumanInfo(models.Model):
    phone = models.CharField(max_length=20, verbose_name="Telefon raqam", validators=[phone_validator, ])

    def __str__(self):
        return self.phone

    class Meta:
        db_table = 'main_humaninfo'
        verbose_name = "Kursga yozilganlar"
        verbose_name_plural = "Kursga yozilganlar"
        ordering = '-id',