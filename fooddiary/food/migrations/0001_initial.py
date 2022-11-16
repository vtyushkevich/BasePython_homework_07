# Generated by Django 4.1.3 on 2022-11-16 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('manufacturer', models.CharField(max_length=200)),
                ('unit', models.CharField(max_length=20)),
                ('calory', models.PositiveIntegerField()),
                ('fat_contents', models.PositiveIntegerField()),
                ('carb_contents', models.PositiveIntegerField()),
                ('protein_contents', models.PositiveIntegerField()),
            ],
        ),
    ]