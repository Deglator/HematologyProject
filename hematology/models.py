from django.conf import settings
from django.db import models
from django.utils import timezone


class Record(models.Model):
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name = "Врач")
    title = models.CharField("Заголовок", max_length=200)
    text = models.TextField("Текст")
    patient_firstname = models.CharField("Имя", max_length=50)
    patient_lastname = models.CharField("Фамилия", max_length=50)
    patient_patronymic = models.CharField("Отчество", max_length=50)
    patient_age = models.DateField("Дата рождения",blank=True, null=True)
    appointment_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
# Create your models here.
