# Generated by Django 4.1 on 2022-11-10 00:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminisrtration', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_name',
            new_name='productname',
        ),
    ]
