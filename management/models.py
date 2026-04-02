from django.db import models

class Branch(models.Model):
    name = models.CharField(max_length=255, verbose_name="Назва філії")
    address = models.TextField(verbose_name="Адреса")
    city = models.CharField(max_length=100, verbose_name="Місто")
    STATUS_CHOICES = (
        ('ACTIVE', 'Активна'),
        ('ARCHIVED', 'Архівна'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ACTIVE')

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=255, verbose_name="Назва предмета")
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, verbose_name="Філія")
    status = models.CharField(max_length=10, default='ACTIVE')

    class Meta:
        unique_together = ('name', 'branch') 

    def __str__(self):
        return f"{self.name} ({self.branch.name})"

class Student(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Ім'я")
    last_name = models.CharField(max_length=100, verbose_name="Прізвище")
    date_of_birth = models.DateField(null=True, blank=True, verbose_name="Дата народження")
    phone = models.CharField(max_length=15, verbose_name="Телефон студента")
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, verbose_name="Філія")
    
    parent_name = models.CharField(max_length=255, verbose_name="ПІБ батьків")
    parent_phone = models.CharField(max_length=15, verbose_name="Телефон батьків")
    
    status = models.CharField(max_length=10, default='ACTIVE')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"