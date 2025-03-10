from django.contrib import admin
from django.contrib import messages

from .models import Master, Review, Service, Visit

def make_published(modeladmin, request, queryset):
    """Установить статус 'Опубликован' для выбранных отзывов"""
    updated = queryset.update(status=0)
    modeladmin.message_user(
        request, f"{updated} отзывов успешно опубликовано", messages.SUCCESS
    )


make_published.short_description = "Опубликовать выбранные отзывы"


def mark_as_unverified(modeladmin, request, queryset):
    """Установить статус 'Не проверен' для выбранных отзывов"""
    updated = queryset.update(status=1)
    modeladmin.message_user(
        request, f"{updated} отзывов отмечено как непроверенные", messages.SUCCESS
    )


mark_as_unverified.short_description = "Отметить как непроверенные"


def approve_reviews(modeladmin, request, queryset):
    """Установить статус 'Одобрен' для выбранных отзывов"""
    updated = queryset.update(status=2)
    modeladmin.message_user(request, f"{updated} отзывов одобрено", messages.SUCCESS)


approve_reviews.short_description = "Одобрить выбранные отзывы"


def reject_reviews(modeladmin, request, queryset):
    """Установить статус 'Отклонен' для выбранных отзывов"""
    updated = queryset.update(status=3)
    modeladmin.message_user(request, f"{updated} отзывов отклонено", messages.SUCCESS)


reject_reviews.short_description = "Отклонить выбранные отзывы"

class VisitInline(admin.TabularInline):
    model = Visit
    extra = 0
    readonly_fields = ("created_at",)
    fields = ("name", "phone", "status", "created_at")
    max_num = 10 
    ordering = ("-created_at",)



@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "contact_info")
    list_display_links = ("first_name", "last_name",)
    inlines = [VisitInline,]
    search_fields = ("first_name", "last_name",)

@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
     list_display = (
        "name",
        "phone",
        "created_at",
        "status",
        "master",
    )
     search_fields = ("name", "phone", "master", "status",)
     list_display_links = ("name", "phone",)
     list_filter = ("created_at", "status", "master",)
     list_editable = ("status",)
     
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "price")
    list_display_links = ("name",)
    list_filter = ("price",)
    search_fields = ("name",)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    # Эти поля будут закрыты на редактирование для ВСЕХ!
    readonly_fields = ("text", "rating", "master")
    # Поля которые будут учитываться в поиске
    search_fields = ("text", "name", "master")
    # Отображаемые столбцы в таблице
    list_display = ("name", "rating", "status", "created_at")
    # Сортировка по created_at сверху свежие
    ordering = ("-created_at",)
    # Сколько отзывов на странице?
    list_per_page = 10
    # Фильтры. По рейтингу, мастерам, статусу и дате
    list_filter = ("rating", "master", "status", "created_at")

    # Добавляем экшены для массового редактирования
    actions = [make_published, mark_as_unverified, approve_reviews, reject_reviews]

