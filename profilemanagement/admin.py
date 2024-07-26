from django.contrib import admin
from .models import Wallet, Order, CartItem

@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance', 'transaction_history')
    search_fields = ('user__username',)
    readonly_fields = ('transaction_history',)
    fieldsets = (
        (None, {'fields': ('user', 'balance', 'transaction_history')}),
    )

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'item_name', 'quantity', 'total_price', 'order_date', 'start_date', 'end_date', 'rental_duration_days')
    list_filter = ('order_date', 'user')
    search_fields = ('user__username', 'item_name')
    readonly_fields = ('total_price', 'rental_duration_days', 'order_date')

    def item_name(self, obj):
        if obj.item:
            return obj.item.name
        return 'No item'

    item_name.admin_order_field = 'item'  # Allows column sorting
    item_name.short_description = 'Item Name'  # Column header name

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Prefetch related data to optimize performance
        return qs.select_related('user', 'content_type')
    
@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'item', 'quantity', 'get_item_price')
    search_fields = ('item', 'user__username')
    list_filter = ('user',)

    def get_item_price(self, obj):
        return obj.item.price if obj.item else 'N/A'
    get_item_price.short_description = 'Price'