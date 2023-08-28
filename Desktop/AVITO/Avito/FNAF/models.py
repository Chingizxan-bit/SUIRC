from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth import get_user_model
# Create your models here.
#title-> Заголовок
#description->описание
#price->цена
#created_at->дата создания
#category->категория
#author->автор
#location->локация
#auction->торг (булевое значение)
#updated_at-> дата обновления
#{tupe} + Field -> нейминг типов джанго моделей
#Модель объявления
User = get_user_model()

class Advertisement(models.Model):
    title = models.CharField("Заголовок", null=True, max_length=150)
    category= models.SmallIntegerField("Категория",null=True)
    content = models.TextField("Описание", null=True )
    price = models.DecimalField("Цена", null=True, max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    user= models.ForeignKey(User, verbose_name="Автор", on_delete=models.CASCADE)
    location= models.CharField("Локация", null=True,  max_length=255)
    auction = models.BooleanField("Торг",null=True , help_text="Отметьте, если торг уместен")
    photo= models.ImageField("Изображение",upload_to="FNAF")
    
    @admin.display(description="дата создания")
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M.%S")
            return format_html('<span style="color: medium purple;font-weight:bold"> Cегодня в [] </span>',create_time)
        return self.created_at.strftime('%d.%m.%Y в %H:%M.%S')
   
   
   
