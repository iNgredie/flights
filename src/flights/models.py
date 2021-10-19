from django.db import models


class Flight(models.Model):
    """ Модель рейсов """

    departure_time = models.DateTimeField(verbose_name='Время вылета', blank=True, null=True)
    departure_airport = models.CharField(max_length=4, verbose_name='Аэропорт вылета', blank=True, null=True)
    arrival_time = models.DateTimeField(verbose_name='Время прилета', blank=True, null=True)
    arrival_airport = models.CharField(max_length=4, verbose_name='Аэропорт прилета', blank=True, null=True)

    class Meta:
        ordering = ('-departure_time',)
        unique_together = (('departure_time', 'departure_airport', 'arrival_time', 'arrival_airport'),)

    def __str__(self) -> str:
        return f'Из аэропорта {self.departure_airport}: {self.departure_time} ' \
               f'в аэропорт {self.arrival_airport}: {self.arrival_time}'

