# Generated by Django 4.1.6 on 2023-05-14 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_alter_review_description_alter_review_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='customer',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='store.customer'),
        ),
    ]
