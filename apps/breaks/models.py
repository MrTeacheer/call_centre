from django.db import models
from django.contrib.auth.models import User


class Organization(models.Model):
    name = models.CharField(verbose_name='Название',max_length=255)
    director= models.ForeignKey(User,
                                on_delete=models.RESTRICT,
                                related_name='organizations_director',
                                verbose_name='Директор')
    employees = models.ManyToManyField(User,
                                       related_name='organizations_employee',
                                       verbose_name='Сотрудники',
                                       blank=True)
    class Meta:
        verbose_name='Организация'
        verbose_name_plural='Организации'
        ordering=('name',)

    def __str__(self):
        return self.name


class Group(models.Model):
    organization = models.ForeignKey(Organization,
                                     on_delete=models.CASCADE,
                                     related_name='groups_organization',
                                     verbose_name='Организация')
    name = models.CharField(verbose_name='Название', max_length=255)
    manager = models.ForeignKey(User,
                                 on_delete=models.RESTRICT,
                                 related_name='organizations_manager',
                                 verbose_name='Менеджер')
    employees = models.ManyToManyField(User,
                                       related_name='groups_employee',
                                       verbose_name='Сотрудники',
                                       blank=True)
    min_active=models.PositiveSmallIntegerField(verbose_name='мин колич активных сотрдн',
                                                null=True,
                                                blank=True)
    break_start=models.TimeField(verbose_name='время начала обеда',
                                 null=True,
                                 blank=True)
    break_finish=models.TimeField(verbose_name='время окончания обеда',
                                  null=True,
                                  blank=True)
    break_max_duration=models.PositiveSmallIntegerField(verbose_name='макс длит обеда',
                                                        null=True,
                                                        blank=True)
    class Meta:
        verbose_name='Группа'
        verbose_name_plural='Группы'
        ordering=('name',)

    def __str__(self):
        return self.name




