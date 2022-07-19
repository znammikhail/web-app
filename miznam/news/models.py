from django.db import models

class Article(models.Model):
    title = models.CharField('Названме', max_length=40)
    anons = models.CharField('Анонс', max_length=256)
    full_text = models.TextField('Статья')
    data = models.DateTimeField('Дата публикации')

    def __str__(self):  # чтобы отображались названия красиво
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'



