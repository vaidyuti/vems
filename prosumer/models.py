from django.db import models


class Generation(models.Model):
    """
    The generation subsystem model of prosumer
    """

    PRIMARY_ENERGY_OIL = "OIL"
    PRIMARY_ENERGY_COAL = "COAL"
    PRIMARY_ENERGY_OTHER = "OTHER"
    PRIMARY_ENERGY_BIOMASS = "BIOMASS"
    PRIMARY_ENERGY_NUCLEAR = "NUCLEAR"
    PRIMARY_ENERGY_RENEWABLES = "RENEWABLES"
    PRIMARY_ENERGY_NATURAL_GAS = "NATURAL_GAS"
    PRIMARY_ENERGY_CHOICES = [
        (PRIMARY_ENERGY_OIL, "Oil"),
        (PRIMARY_ENERGY_COAL, "Coal"),
        (PRIMARY_ENERGY_OTHER, "Other"),
        (PRIMARY_ENERGY_BIOMASS, "Biomass"),
        (PRIMARY_ENERGY_NUCLEAR, "Nuclear"),
        (PRIMARY_ENERGY_RENEWABLES, "Renewables"),
        (PRIMARY_ENERGY_NATURAL_GAS, "Natural Gas"),
    ]

    CONVERSION_TECHNIQUE_FBR = "FBR"
    CONVERSION_TECHNIQUE_GCC = "GCC"
    CONVERSION_TECHNIQUE_LWR = "LWR"
    CONVERSION_TECHNIQUE_IGCC = "IGCC"
    CONVERSION_TECHNIQUE_SOFC = "SOFC"
    CONVERSION_TECHNIQUE_WIND = "WIND"
    CONVERSION_TECHNIQUE_HYDRO = "HYDRO"
    CONVERSION_TECHNIQUE_OTHER = "OTHER"
    CONVERSION_TECHNIQUE_SOLAR = "SOLAR"
    CONVERSION_TECHNIQUE_LWR_PU = "LWR_Pu"
    CONVERSION_TECHNIQUE_GEOTHERMAL = "GEOTHERMAL"
    CONVERSION_TECHNIQUE_CONVENTIONAL = "CONVENTIONAL"
    CONVERSION_TECHNIQUE_CHOICES = [
        (CONVERSION_TECHNIQUE_FBR, "Fast Breeder"),
        (CONVERSION_TECHNIQUE_GCC, "GCC"),
        (CONVERSION_TECHNIQUE_LWR, "LWR"),
        (CONVERSION_TECHNIQUE_IGCC, "IGCC"),
        (CONVERSION_TECHNIQUE_SOFC, "SOFC"),
        (CONVERSION_TECHNIQUE_WIND, "Wind Power"),
        (CONVERSION_TECHNIQUE_HYDRO, "Hydro Power"),
        (CONVERSION_TECHNIQUE_OTHER, "Other"),
        (CONVERSION_TECHNIQUE_SOLAR, "Photo Voltaic"),
        (CONVERSION_TECHNIQUE_LWR_PU, "Pu-thermal"),
        (CONVERSION_TECHNIQUE_GEOTHERMAL, "Geothermal"),
        (CONVERSION_TECHNIQUE_CONVENTIONAL, "Conventional"),
    ]

    asset_value = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="asset_value",
        help_text="The value of the generation subsystem asset in local currency",
    )
    conversion_technique = models.CharField(
        max_length=255,
        blank=False,
        choices=CONVERSION_TECHNIQUE_CHOICES,
        verbose_name="conversion_technique",
        help_text="The conversion technique of the generation subsystem",
    )
    efficiency = models.DecimalField(
        max_digits=4,
        decimal_places=4,
        blank=False,
        null=False,
        verbose_name="subsystem_efficiency",
        help_text="Efficiency of the subsystem (in %)",
    )
    installed_capacity = models.IntegerField(
        blank=False,
        null=False,
        verbose_name="installed_capacity_kw",
        help_text="Installed Capacity in KW",
    )
    payback_period = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="payback_period",
        help_text="Payback period of the generation subsystem asset in months",
    )
    primary_energy = models.CharField(
        max_length=255,
        blank=False,
        choices=PRIMARY_ENERGY_CHOICES,
        verbose_name="primary_energy_type",
        help_text="The primary energy type of the generation subsystem.",
    )
    prosumer = models.ForeignKey(
        "prosumer.Prosumer",
        related_name="generations",
        null=False,
        on_delete=models.PROTECT,
        verbose_name="prosumer",
        help_text="The prosumer of this generation subsystem.",
    )

    def __str__(self):
        return str(self.conversion_technique)


class Load(models.Model):
    """
    Prosumer's load model
    """

    is_dr_adaptive = models.BooleanField(
        blank=False,
        null=False,
        default=False,
        verbose_name="is_demand_response_adaptive",
        help_text="Whether the load subsystem is adaptive to demand response signals.",
    )
    max_power = models.IntegerField(
        blank=False,
        null=False,
        verbose_name="max_power_kw",
        help_text="The maximum power in kW that the load may demand at any instant.",
    )
    prosumer = models.ForeignKey(
        "prosumer.Prosumer",
        related_name="loads",
        null=False,
        on_delete=models.PROTECT,
        verbose_name="prosumer",
        help_text="The prosumer associated to the load subsystem.",
    )


class Prosumer(models.Model):
    """
    An energy prosumer is an entity which takes part in trading energy with other prosumers.
    """

    geolocation = models.JSONField(
        blank=False,
        null=False,
        verbose_name="location_coordinates",
        help_text="Geographic location coordinates of the prosumer",
    )
    is_dr_adaptive = models.BooleanField(
        blank=False,
        null=False,
        default=False,
        verbose_name="is_demand_response_adaptive",
        help_text="Whether the prosumer is adaptive to Demand Response signals.",
    )
    max_export_power = models.IntegerField(
        blank=False,
        null=False,
        verbose_name="max_export_power",
        help_text="Maximum Export Power in KW",
    )
    max_import_power = models.IntegerField(
        blank=False,
        null=False,
        verbose_name="max_import_power_kw",
        help_text="Maximum Import Power in KW",
    )
    mean_payback_period = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="mean_payback_period",
        help_text="Weighted average payback period in terms of months dervied from payback period and asset value of subsystems of the prosumer.",
    )
    total_asset_value = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="total_asset_value",
        help_text="The total asset value of the prosumer which shall be used to decide the energy export price.",
    )
    user = models.ForeignKey(
        "users.User",
        related_name="prosumers",
        null=False,
        on_delete=models.PROTECT,
        help_text="The user associated to the prosumer",
    )


class Storage(models.Model):
    """
    Prosumer's Energy Storage Subsystem model
    """

    TECHNOLOGY_OTHER = "OTHER"
    TECHNOLOGY_LEAD_ACID = "LEAD_ACID"
    TECHNOLOGY_LITHIUM_ION = "LITHIUM_ION"
    TECHNOLOGY_CHOICES = [
        (TECHNOLOGY_OTHER, "Other"),
        (TECHNOLOGY_LEAD_ACID, "Lead Acid"),
        (TECHNOLOGY_LITHIUM_ION, "Li-Ion"),
    ]

    health = models.DecimalField(
        max_digits=3,
        decimal_places=3,
        blank=True,
        null=True,
        verbose_name="storage_health_percentage",
        help_text="The health of the energy storage system (primarily for battery based storages)",
    )
    installed_capacity = models.IntegerField(
        blank=False,
        null=False,
        verbose_name="installed_capacity_kwh",
        help_text="The amount of energy storable by the system in kWh.",
    )
    prosumer = models.ForeignKey(
        "prosumer.Prosumer",
        related_name="storages",
        null=False,
        on_delete=models.PROTECT,
        verbose_name="prosumer",
        help_text="The prosumer associated with this",
    )
    technology = models.CharField(
        max_length=255,
        blank=False,
        choices=TECHNOLOGY_CHOICES,
        verbose_name="storage_technology",
        help_text="The type of technology used for energy storage",
    )
    usable_capacity = models.DecimalField(
        max_digits=3,
        decimal_places=3,
        blank=False,
        null=False,
        verbose_name="usable_capacity",
        help_text="The depth of discharge allowed for export.",
    )

    def __str__(self):
        return str(self.technology)
