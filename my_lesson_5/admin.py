from django.contrib import admin
from .models import Advertisment
from django.utils import timezone
# Register your models here.

class AdvertismentAdmin(admin.ModelAdmin):
    list_display=["id","title","description","price","author","created_date","updated_date","action"]
    list_filter=["action"]
    actions=["forbid_the_auction"]
    # fieldsets=(
    # ('Общее',{
    # 'fields':('title','description'),
    # 'classes':["collapse"]
    # }),
    # )

    @admin.action(description="убрать возможность торга")
    def forbid_the_auction(self,request,queryset):
        queryset.update(action=False)

    # @admin.display(description="Дата создания")
    # def created_date(self):
    #     if self.created_at == timezone.now().date():
    #         create_time=self.created_at.strftime("%H:%M.%S")
    #         return form_html("""<span>Сегодня в {} </span>""",create_time)
    #     return self.created_at.strftime("%d.%m.%Y в %H:%M.%S")
        
admin.site.register(Advertisment,AdvertismentAdmin)