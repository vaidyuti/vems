from django.db import models
from django.utils.timezone import now


class P2PTransaction(models.Model):
    """
    Peer-to-peer transaction model
    """

    amount_payable = models.DecimalField(
        max_digits=10,
        decimal_places=4,
        blank=False,
        null=False,
        verbose_name="amount_payable_by_consumer",
        help_text="The amount debted to the producer by the consumer in this trade.",
    )
    closing = models.DateTimeField(
        blank=False,
        null=False,
        verbose_name="closing_datetime",
        help_text="The date time at which the transaction closed.",
    )
    consumer = models.ForeignKey(
        "prosumer.Prosumer",
        related_name="p2_p_transactions_consumer",
        null=False,
        on_delete=models.PROTECT,
        verbose_name="energy_consumer",
        help_text="The prosumer which imported the energy after transmission and other losses.",
    )
    exported_energy = models.IntegerField(
        blank=False,
        null=False,
        verbose_name="exported_energy",
        help_text="The energy exported by the producer in kWh",
    )
    meta = models.JSONField(
        blank=False,
        null=False,
        verbose_name="metadata",
        help_text="Metadata for the transaction",
    )
    opening = models.DateTimeField(
        blank=False,
        null=False,
        default=now,
        verbose_name="opening_datetime",
        help_text="The date time at which the transaction opened.",
    )
    producer = models.ForeignKey(
        "prosumer.Prosumer",
        related_name="p2_p_transactions_producer",
        null=False,
        on_delete=models.PROTECT,
        verbose_name="energy_producer",
        help_text="The prosumer which exported the energy.",
    )
    transmission_distance = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="transmission_distance",
        help_text="The transmission distance in metres.",
    )
    transmission_efficiency = models.DecimalField(
        max_digits=4,
        decimal_places=4,
        blank=False,
        null=False,
        verbose_name="transmission_efficiency",
        help_text="How efficiently the energy trade made between the prosumers.",
    )
    unit_price = models.DecimalField(
        max_digits=10,
        decimal_places=4,
        blank=False,
        null=False,
        verbose_name="weighted_avg_unit_price",
        help_text="The weighted average unit price for the exported energy",
    )
    upi_payment_url = models.CharField(
        max_length=255,
        blank=False,
        verbose_name="upi_payment_url",
        help_text="The URL for initiating UPI payment.",
    )
