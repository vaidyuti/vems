from django.contrib import admin

from .models import P2PTransaction


class P2PTransactionAdmin(admin.ModelAdmin):
    model = P2PTransaction
    list_display = ["producer"]
    list_select_related = True


admin.site.register(P2PTransaction, P2PTransactionAdmin)
