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


class Replacement(models.Model):
    group = models.ForeignKey(Group,
                                    on_delete=models.CASCADE,
                                    related_name='replacements_group',
                                    verbose_name='Группа')
    date=models.DateField(verbose_name='Дата смены')
    break_start=models.TimeField(verbose_name='время начала обеда')
    break_finish=models.TimeField(verbose_name='время окончания обеда')
    break_max_duration=models.PositiveSmallIntegerField(verbose_name='макс длит обеда')
    class Meta:
        verbose_name='Смена'
        verbose_name_plural='Смены'
        ordering=('-date',)

    def __str__(self):
        return f'смена для: {self.group}'


class ReplacementStatus(models.Model):
    code=models.CharField(max_length=16,
                          verbose_name='Код')
    name=models.CharField(max_length=255,
                          verbose_name='Название')
    sort= models.PositiveIntegerField(verbose_name='Сортировка',
                                      null=True,
                                      blank=True)
    is_active=models.BooleanField(default=True,
                                  verbose_name='Активность')

    class Meta:
        verbose_name='Статус смены'
        verbose_name_plural='Статусы смены'
        ordering=('sort',)

    def __str__(self):
        return f'{self.code} для {self.name}'


class ReplacementEmployee(models.Model):
    replacement = models.ForeignKey(Replacement,
                                    on_delete=models.CASCADE,
                                    related_name='employees',
                                    verbose_name='смена')
    employee = models.ForeignKey(User,
                                 on_delete=models.CASCADE,
                                 related_name='replacements',
                                 verbose_name='Сотрудник')
    status = models.ForeignKey(ReplacementStatus,
                               on_delete=models.RESTRICT,
                               related_name='replacement_employees',
                               verbose_name='Статус')

    class Meta:
        verbose_name='Смена-работника'
        verbose_name_plural='Смены-работников'

    def __str__(self):
        return f'{self.replacement} для {self.employee}'
