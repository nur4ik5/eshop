from django.db import models

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
	name = models.CharField(max_length=100)
	description = models.TextField()
	# для автоматического добавления значения при создании
	created = models.DateTimeField(auto_now_add=True)
	# для автоматического изменения значения при обновлении записи
	updated = models.DateTimeField(auto_now=True)   
	# для десятичных дробей, пример: 125, 50
	price = models.DecimalField(max_digits=6, decimal_places=2)   

	count = models.IntegerField()
	featured_product = models.BooleanField(default=False)
	category = models.CharField(max_length=5, choices=CATEGORIES, default=PHONE)	

	def __str__(self):
		return f"{self.name} - {self.category}"