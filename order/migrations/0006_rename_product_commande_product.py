# Generated by Django 4.1.7 on 2023-03-18 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_commande_product_commande_users_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commande',
            old_name='Product',
            new_name='product',
        ),
    ]
