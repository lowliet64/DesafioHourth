# Generated by Django 4.0.2 on 2022-02-08 00:57

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
                ('product_url', models.TextField()),
                ('product_url_created_at', models.DateField()),
                ('consult_date', models.DateField()),
                ('c', models.IntegerField()),
            ],
        ),
    ]
