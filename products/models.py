from django.db import models

def product_photo_dir(instance, filename):
	# MEDIA_ROOT/ ID_/_FILENAME_
	return 'porduct_photos/'+instance.id + '/' + filename


class Product(models.Model):
	# Модель товаров
	SPORT = 'sport'
	SHOES = 'shoes'
	PHONE = 'phone'
	CATEGORIES = (
		# первое значение хранится в БД
		# второе видно пользователю
		('SPORT', 'Спортивные товары'),
		('SHOES', 'Обувь'),
		('PHONE', ' Мобильные телефоны'),

	)
	name = models.CharField(max_length=100, verbose_name='Название')
	description = models.TextField(verbose_name='Описание')
	# для автоматического добавления значения при создании
	created = models.DateTimeField(auto_now_add=True)
	# для автоматического изменения значения при обновлении записи
	updated = models.DateTimeField(auto_now=True)   
	# для десятичных дробей, пример: 125, 50
	price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Цена')   
	count = models.IntegerField(verbose_name='Количество на складе')
	featured_product = models.BooleanField(default=False, verbose_name='Продвигать товар')
	category = models.CharField(max_length=5, choices=CATEGORIES, default=PHONE, verbose_name='Котегория')	
	# поле для сохранения картинки, аргумент upload_to для обозначения конкретной папки
	photo = models.ImageField(upload_to='porduct_photos', default='default.png')


	def __str__(self):
		return f"{self.name} - {self.category}"

	class Meta:
		verbose_name='Товар'
		verbose_name_plural='Товар'