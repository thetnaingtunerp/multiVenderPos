# Generated by Django 5.1.1 on 2024-10-13 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_cart_branch_cartproduct_branch_ecommerceorder'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EcommerceOrder',
            new_name='Order',
        ),
    ]
