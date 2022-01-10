# Generated by Django 4.0.1 on 2022-01-10 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('count', models.IntegerField()),
                ('featured_product', models.BooleanField(default=False)),
                ('category', models.CharField(choices=[('SPORT', 'Спортивные товары'), ('SHOES', 'Обувь'), ('PHONE', ' Мобильные телефоны')], default='phone', max_length=5)),
            ],
        ),
    ]