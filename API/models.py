from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum


class Wallet(models.Model):
    name = models.CharField('Name', max_length=200)
    balance = models.DecimalField('Balance', max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.name

    def calculate_balance(self, new_balance):
        self.balance=new_balance
        self.save()


class Transaction(models.Model):
    wallet = models.ForeignKey(Wallet, related_name='txs', on_delete=models.CASCADE)
    tx_comment = models.TextField('Comment')
    tx_date = models.DateTimeField('Date')
    tx_sum = models.DecimalField('Sum', max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.tx_sum)


@receiver([post_save, post_delete], sender=Transaction)
def update_calculated_fields(sender, instance, **kwargs):
    wallet_id = instance.wallet_id
    new_balance = sender.objects.filter(wallet_id=int(wallet_id)).aggregate(balance=Sum('tx_sum')).get('balance')
    if new_balance is None:
        new_balance = 0
    Wallet.objects.get(id=wallet_id).calculate_balance(new_balance)