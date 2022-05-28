from rest_framework import serializers

from .models import Generation, Load, Prosumer, Storage


class GenerationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Generation
        fields = (
            "url",
            "prosumer",
            "primary_energy",
            "conversion_technique",
            "installed_capacity",
            "efficiency",
            "asset_value",
            "payback_period",
        )


class LoadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Load
        fields = (
            "url",
            "prosumer",
            "max_power",
            "is_dr_adaptive",
        )


class ProsumerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prosumer
        fields = (
            "url",
            "user",
            "geolocation",
            "max_import_power",
            "max_export_power",
            "is_dr_adaptive",
            "total_asset_value",
            "mean_payback_period",
        )
        read_only_fields = ("user",)


class StorageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Storage
        fields = (
            "url",
            "prosumer",
            "technology",
            "installed_capacity",
            "usable_capacity",
            "health",
        )
