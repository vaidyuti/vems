from django.db import models


class Generation(models.Model):
    """
    The generation subsystem model of prosumer
    """

    CATEGORY_GROUP_OIL = "OIL"
    CATEGORY_GROUP_COAL = "COAL"
    CATEGORY_GROUP_OTHER = "OTHER"
    CATEGORY_GROUP_BIOMASS = "BIOMASS"
    CATEGORY_GROUP_NUCLEAR = "NUCLEAR"
    CATEGORY_GROUP_RENEWABLES = "RENEWABLES"
    CATEGORY_GROUP_NATURAL_GAS = "NATURAL_GAS"
    CATEGORY_GROUP_CHOICES = [
        (CATEGORY_GROUP_OIL, "Oil"),
        (CATEGORY_GROUP_COAL, "Coal"),
        (CATEGORY_GROUP_OTHER, "Other"),
        (CATEGORY_GROUP_BIOMASS, "Biomass"),
        (CATEGORY_GROUP_NUCLEAR, "Nuclear"),
        (CATEGORY_GROUP_RENEWABLES, "Renewables"),
        (CATEGORY_GROUP_NATURAL_GAS, "Natural Gas"),
    ]

    CATEGORY_FBR = "FBR"
    CATEGORY_GCC = "GCC"
    CATEGORY_LWR = "LWR"
    CATEGORY_IGCC = "IGCC"
    CATEGORY_SOFC = "SOFC"
    CATEGORY_WIND = "WIND"
    CATEGORY_HYDRO = "HYDRO"
    CATEGORY_OTHER = "OTHER"
    CATEGORY_SOLAR = "SOLAR"
    CATEGORY_LWR_PU = "LWR_Pu"
    CATEGORY_GEOTHERMAL = "GEOTHERMAL"
    CATEGORY_CONVENTIONAL = "CONVENTIONAL"
    CATEGORY_CHOICES = [
        (CATEGORY_FBR, "Fast Breeder"),
        (CATEGORY_GCC, "GCC"),
        (CATEGORY_LWR, "LWR"),
        (CATEGORY_IGCC, "IGCC"),
        (CATEGORY_SOFC, "SOFC"),
        (CATEGORY_WIND, "Wind Power"),
        (CATEGORY_HYDRO, "Hydro Power"),
        (CATEGORY_OTHER, "Other"),
        (CATEGORY_SOLAR, "Photo Voltaic"),
        (CATEGORY_LWR_PU, "Pu-thermal"),
        (CATEGORY_GEOTHERMAL, "Geothermal"),
        (CATEGORY_CONVENTIONAL, "Conventional"),
    ]

    asset_value = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="asset_value",
        help_text="The value of the generation subsystem asset in local currency",
    )
    category = models.CharField(
        max_length=255,
        blank=False,
        choices=CATEGORY_CHOICES,
        verbose_name="conversion_technique",
        help_text="The conversion technique of the generation subsystem",
    )
    category_group = models.CharField(
        max_length=255,
        blank=False,
        choices=CATEGORY_GROUP_CHOICES,
        verbose_name="primary_energy_type",
        help_text="The primary energy type of the generation subsystem.",
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
    prosumer = models.ForeignKey(
        "prosumer.Prosumer",
        related_name="generations",
        null=False,
        on_delete=models.PROTECT,
        verbose_name="prosumer",
        help_text="The prosumer of this generation subsystem.",
    )


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

    CATEGORY_MUNCIPAL = "MUNCIPAL"
    CATEGORY_MICROGRID = "MICROGRID"
    CATEGORY_COMMERCIAL = "COMMERCIAL"
    CATEGORY_INDUSTRIAL = "INDUSTRIAL"
    CATEGORY_RESIDENTIAL = "RESIDENTIAL"
    CATEGORY_AGRICULTURAL = "AGRICULTURAL"
    CATEGORY_CHOICES = [
        (CATEGORY_MUNCIPAL, "Muncipal"),
        (CATEGORY_MICROGRID, "Microgrid"),
        (CATEGORY_COMMERCIAL, "Commercial"),
        (CATEGORY_INDUSTRIAL, "Industrial"),
        (CATEGORY_RESIDENTIAL, "Residential"),
        (CATEGORY_AGRICULTURAL, "Agricultural"),
    ]

    category = models.CharField(
        max_length=255,
        blank=True,
        choices=CATEGORY_CHOICES,
    )
    is_dr_adaptive = models.BooleanField(
        blank=False,
        null=False,
        default=False,
        verbose_name="is_demand_response_adaptive",
        help_text="Whether the prosumer is adaptive to Demand Response signals.",
    )
    location = models.JSONField(
        blank=False,
        null=False,
        verbose_name="location_coordinates",
        help_text="Geographic location coordinates of the prosumer",
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

    CATEGORY_OTHER = "OTHER"
    CATEGORY_LEAD_ACID = "LEAD_ACID"
    CATEGORY_LITHIUM_ION = "LITHIUM_ION"
    CATEGORY_CHOICES = [
        (CATEGORY_OTHER, "Other"),
        (CATEGORY_LEAD_ACID, "Lead Acid"),
        (CATEGORY_LITHIUM_ION, "Li-Ion"),
    ]

    category = models.CharField(
        max_length=255,
        blank=False,
        choices=CATEGORY_CHOICES,
        verbose_name="storage_technology",
        help_text="The type of technology used for energy storage",
    )
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
    usable_capacity = models.DecimalField(
        max_digits=3,
        decimal_places=3,
        blank=False,
        null=False,
        verbose_name="usable_capacity",
        help_text="The depth of discharge allowed for export.",
    )
