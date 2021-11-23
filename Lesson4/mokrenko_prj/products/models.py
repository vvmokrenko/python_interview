from django.db import models

# Create your models here.


class Good_Item(models.Model):
    created_at = models.DateTimeField(
        verbose_name=u'Дата поступления',
        auto_created=True,
        auto_now_add=True
    )

    title = models.CharField(
        verbose_name=u'Название',
        max_length=255
    )

    price = models.PositiveIntegerField(
        verbose_name=u'Цена',
        default=0
    )

    unit = models.CharField(
        verbose_name=u'Единица измерения',
        max_length=16,
        default='шт.'
    )

    vendor = models.CharField(
        verbose_name=u'Поставщик',
        max_length=255
    )

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'Карточка товара'
        verbose_name_plural = u'Карточки товаров'
