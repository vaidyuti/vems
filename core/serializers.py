from rest_framework import serializers

from .models import P2PTransaction


class P2PTransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = P2PTransaction
        fields = (
            "url",
            "producer",
            "consumer",
            "opening",
            "closing",
            "exported_energy",
            "transmission_distance",
            "transmission_efficiency",
            "unit_price",
            "meta",
            "amount_payable",
            "upi_payment_url",
        )
