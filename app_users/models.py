# from django.db import models
# from django.contrib.auth.models import User
# from app_marketplace.models import Goods, Marketplace
# from django.utils.translation import gettext_lazy as _
# from django.db.models import Sum
# from django.core.cache import cache
# import logging
#
# logger = logging.getLogger(__name__)
#
#
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_("Пользователь"))
#     city = models.CharField(max_length=36, blank=True, verbose_name=_("Город"))
#     date_of_birth = models.DateField(null=True, blank=True, verbose_name=_("Дата рождения"))
#     number_phone = models.CharField(max_length=12, blank=True, verbose_name=_("Номер телефона"))
#     balance = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name=_('Баланс на счету'))
#     status = models.CharField(max_length=100, default='a', choices=CHOICES, verbose_name=_("Статус"))
#
#     class Meta:
#         verbose_name = _('Информация о пользователях')
#         verbose_name_plural = _('Информация о пользователях')
#         ordering = ['user']
#
#     def get_status(self):
#         total_amount = PurchaseHistory.objects.filter(user_id=self.user.id).aggregate(Sum('total_price'))
#         if 5000 <= total_amount['total_price__sum'] < 50000 and self.status != 'b':
#             self.status = 'b'
#         elif total_amount['total_price__sum'] >= 50000 and self.status != 'c':
#             self.status = 'c'
#         elif total_amount['total_price__sum'] <= 5000 and self.status != 'a':
#             self.status = 'a'
#
#         orig = Profile.objects.only('status').get(pk=self.pk)
#         if orig.status != self.status:
#             logger.info(f'Пользователь: {self.user.username}, ID: {self.user.id}'
#                         f' переведен в статус: {self.get_status_display()}')
#             self.save()
#         return self.get_status_display()
#
#
# class PurchaseHistory(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Пользователь'))
#     goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name=_('Товар'))
#     quantity = models.PositiveIntegerField(default=0, verbose_name=_("Количество товара"))
#     price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name=_('Цена товара'))
#     total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True,
#                                       verbose_name=_('Цена товара'))
#     purchase_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата покупки'))
#     shop = models.ForeignKey(Marketplace, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_("Магазин"))
#
#     class Meta:
#         verbose_name = _('История покупок')
#         verbose_name_plural = _('История покупок')
#         ordering = ['-purchase_date', ]
