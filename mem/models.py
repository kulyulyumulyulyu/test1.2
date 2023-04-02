from django.db import models

class About(models.Model):
    struktura = models.TextField(blank=True, verbose_name="Структура")
    dolzhnost = models.TextField(blank=True, verbose_name="Должность")
    nomer = models.CharField(max_length=255, verbose_name="Номер телефона")
    existence = models.BooleanField(default=True)



    def __str__(self):
        return self.struktura

    class Meta:
        verbose_name = 'Сотрудники'
        verbose_name_plural = 'Сотрудники'

class Contact(models.Model):
    name = models.TextField(blank=True, verbose_name="Имя")
    telephone = models.CharField(max_length=255, verbose_name="Номер телефона")