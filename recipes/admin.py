from django.contrib import admin
from .models import Recipe

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_ingredients', 'created_by')
    search_fields = ('title', 'ingredients')

    def short_ingredients(self, obj):
        return obj.ingredients[:50] + ('...' if len(obj.ingredients) > 50 else '')
    short_ingredients.short_description = 'Ingredients'

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)
