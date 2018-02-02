from django.contrib.postgres.search import TrigramSimilarity
from django.db import models
from django.core.validators import URLValidator


class RulerManager(models.Manager):
    def get_queryset(self):
        return super(RulerManager, self).get_queryset().select_related('predecessor', 'successor')


class Ruler(models.Model):
    name = models.CharField(
        'Имя',
        max_length=255,
        db_index=True,
    )
    url = models.TextField(
        'Ссылка на страницу в википедии',
        validators=[URLValidator()],
        unique=True,
        db_index=True,
    )
    predecessor = models.OneToOneField(
        'self',
        on_delete=models.SET_NULL,
        related_name='successor',
        verbose_name='Предшественник',
        default=None,
        null=True,
        blank=True,
    )
    succession_order = models.PositiveIntegerField(
        'Порядок наследования'
    )

    objects = models.Manager()
    objects_select_related = RulerManager()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('succession_order', )

    @property
    def all_successors(self):
        return Ruler.objects_select_related.filter(succession_order__gt=self.succession_order)


class RulerRequest(models.Model):
    datetime = models.DateTimeField(
        'Время запроса',
        auto_now_add=True
    )
    ruler = models.ForeignKey(
        Ruler,
        related_name='ruler_requests',
        verbose_name='Правитель',
        on_delete=models.SET_NULL,
        null=True,
    )
    ruler_successors = models.ManyToManyField(
        Ruler,
        related_name='ruler_requests_as_successor',
        verbose_name='Вычисленные наследники (на момент запроса)'
    )

    def __str__(self):
        return self.datetime.strftime("%Y-%m-%d %H:%M:%S")
