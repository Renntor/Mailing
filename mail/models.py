from django.db import models

# Create your models here.

NULLABLE = {'null': True, 'blank': True}


class Client(models.Model):
    email = models.EmailField(unique=True, verbose_name='почта')
    full_name = models.CharField(max_length=100, verbose_name='фио')
    comment = models.TextField(**NULLABLE, verbose_name='комментарий')

    def __str__(self):
        return f'{self.email}, {self.full_name}, {self.comment}'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class SettingMail(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='клиент')

    mailing_time = models.TimeField(verbose_name='время рассылки')
    period = models.PositiveIntegerField(verbose_name='периодичность', default=1)
    status = models.CharField(max_length=20, verbose_name='статус')

    def __str__(self):
        return f'{self.mailing_time}, {self.period}, {self.status}'

    class Meta:
        verbose_name = 'настройка'
        verbose_name_plural = 'настройки'


class Mailing(models.Model):
    setting = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='настройки')

    subject = models.TextField(default='no subject', verbose_name='тема')
    text = models.TextField(verbose_name='текст')

    def __str__(self):
        return f'{self.subject}, {self.text}'

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class Log(models.Model):
    mail = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='сообщение')

    date_last_try = models.DateTimeField(verbose_name='время последний попытки')
    status_try = models.CharField(max_length=50, verbose_name='статус')
    answer = models.TextField(**NULLABLE, verbose_name='ответ')

    def __str__(self):
        return f'{self.date_last_try}, {self.status_try}, {self.answer}'

    class Meta:
        verbose_name = 'лог'
        verbose_name_plural = 'логи'
