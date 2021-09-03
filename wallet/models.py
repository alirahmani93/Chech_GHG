from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count, Sum, Q
from django.db.models.functions import Coalesce


class Transaction(models.Model):
    CHARGE = 1
    PURCHASE = 2
    TRANSFER_RECEIVED = 3
    TRANSFER_SENT = 4

    TRANSACTION_TYPE_CHOICES = (
        (CHARGE, "Charge"),
        (PURCHASE, "Purchase"),
        (TRANSFER_RECEIVED, "Transfer_received"),
        (TRANSFER_SENT, "Transfer_sent"),
    )
    #change related name
    user = models.ForeignKey(User, related_name='transaction', on_delete=models.RESTRICT)
    transaction_type = models.PositiveSmallIntegerField(choices=TRANSACTION_TYPE_CHOICES, default=CHARGE)
    amount = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.get_transanction_type_display()} - {self.amount}"

    @classmethod
    def get_report(cls):
        positive_transactions = Sum('transaction__amount', filter=Q(transaction__transaction_type=[1, 3]))
        negative_transactions = Sum('transaction__amount', filter=Q(transaction__transaction_type=[2, 4]))
        users = User.objects.all.annotate(
            transantion_count=Count('transactions__id'),
            # balance=Sum('transactions__amount')
            balance=Coalesce(positive_transactions, 0) - Coalesce(negative_transactions, 0)
        )
        return users

    @classmethod
    def get_total_balance(cls, user):
        # User.objects.all().aggregate(
        # transaction_count=Count('transaction__id'),
        # total_balance=Sum('transactions__amount'))
        queryset = cls.get_report()
        return queryset.aggregate(Sum('balance'))

    @classmethod
    def balance(cls, user):
        positive_transactions = Sum('amount', filter=Q(transaction_type=[1, 3]))
        negative_transactions = Sum('amount', filter=Q(transaction_type=[2, 4]))

        user_balance = User.transactions.all().aggregate(
            balance=Coalesce(positive_transactions, 0) - Coalesce(negative_transactions, 0)
        )
        return user_balance.get('balance', 0)


class UserBalance(models.Model):
    user = models.ForeignKey(User, related_name='balance_records', on_delete='model.PROTECT')
    balance = models.BigIntegerField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.balance} - {self.created_time}"

    @classmethod
    def record_user_balance(cls, user):
        balance = Transaction.user_balance(user)
        instance = cls.objects.create(user=user, balance=balance)
        return instance

    @classmethod
    def record_all_users_balance(cls):
        for user in User.objects.all():
            record = cls.record_user_balance(user)
            print(record)
    #return??


class TransferTransactions(models.Model):
    sender_transactions = models.OneToOneField(Transaction, related_name='sent_transfer', on_delete=models.RESTRICT())
    receiver_transactions = models.OneToOneField(Transaction, related_name='received_transfer',
                                                 on_delete=models.RESTRICT())

    def __str__(self):
        return f'{self.sender_transactions} >> {self.receiver_transactions}'

    @classmethod
    def transfer(cls, sender, receiver, amount):
        if Transaction.user_balance(sender) < amount:
            return "not allowed"

        send_transaction = Transaction.objects.create(
            user=sender, amount=amount, transaction_type=Transaction.TRANSFER_SENT
        )
        receiver_transaction = Transaction.objects.create(
            user=receiver, amount=amount, transaction_type=Transaction.TRANSFER_SENT
        )

        instance = cls.objects.create(sender_transactions=send_transaction, receiver_transactions=receiver_transaction)
        return instance