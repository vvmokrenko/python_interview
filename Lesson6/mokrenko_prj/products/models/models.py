from django.db import models
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager

# Create your models here.


class Category(models.Model):
    name = models.CharField(
        verbose_name='имя',
        max_length=64,
        unique=True,
    )

    description = models.TextField(
        verbose_name='описание',
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    slug = models.SlugField(unique=True, blank=True, null=True)

    site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    objects = CurrentSiteManager('site')

    @property
    def get_products(self):
        return Good_Item.objects.filter(category=self.id)

class Good_Item(models.Model):
    category = models.ManyToManyField(Category,
                                      'category_rel_name')

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

    site = models.ManyToManyField(Site, 'site_rel_name')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'Карточка товара'
        verbose_name_plural = u'Карточки товаров'

    objects = CurrentSiteManager('site')
#
#
# class CustomManager(models.Manager):
#     def get_queryset(self):
#         return CustomQuerySet(self.model, using=self._db)
#
#     def value_filter(self):
#         return self.get_queryset().value_filter()
