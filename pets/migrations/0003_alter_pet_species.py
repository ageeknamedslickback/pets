# Generated by Django 4.0.3 on 2022-03-11 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_alter_pet_year_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='species',
            field=models.CharField(choices=[('cat', 'Cat'), ('dog', 'Dog'), ('hamster', 'Hamster')], max_length=10),
        ),
    ]
