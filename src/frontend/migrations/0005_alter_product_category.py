# Generated by Django 5.1.1 on 2024-10-05 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0004_remove_order_order_date_remove_order_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Coke', 'Coke'), ('pepsi', 'pepsi'), ('sprite', 'sprite'), ('Fanta', 'Fanta'), ('Coke Zero', 'Coke Zero')], max_length=50, null=True),
        ),
    ]
