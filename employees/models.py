from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Department(MPTTModel):
    """
    Модель отдела с поддержкой иерархии.
    """
    name = models.CharField(max_length=255, verbose_name='Департамент')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']
        verbose_name = 'Департамент'
        verbose_name_plural = 'Департаменты'

    def __str__(self):
        return self.name


class Employee(models.Model):

    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    position = models.CharField(max_length=255, verbose_name='Должность')
    hire_date = models.DateField(verbose_name='Дата трудоустройства')
    salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='З/п')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees', db_index=True,
                                   verbose_name='Департамент')
    objects = models.Model

    def __str__(self):
        return self.full_name

    class Meta:
        indexes = [
            models.Index(fields=['department']),
            models.Index(fields=['full_name']),
        ]
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
