from django.db import models

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
class Advertisement(models.Model):
    title = models.CharField("Заголовок", max_length=150)
    category= models.SmallIntegerField("Категория")
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    creatied_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author= models.CharField("Автор", max_length=20)
    location= models.CharField("Локация", max_length=255)
    auction = models.BooleanField("Торг", help_text="Отметьте, если торг уместен")
class Advertisement(models.Model):
   class Meta: 
        db_table = 'advertisements' 
 

  