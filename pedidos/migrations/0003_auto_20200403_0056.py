# Generated by Django 3.0.1 on 2020-04-03 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0002_auto_20200115_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='addres',
            field=models.CharField(max_length=50, verbose_name='Dir.'),
        ),
    ]