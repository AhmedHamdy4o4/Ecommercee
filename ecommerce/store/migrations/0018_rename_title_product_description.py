# Generated by Django 4.2.1 on 2023-05-21 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_rename_sex_product_gender'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='title',
            new_name='description',
        ),
    ]
