# Generated by Django 4.0.3 on 2022-03-11 06:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('species', models.CharField(choices=[('Cat', 'cat'), ('Dog', 'dog'), ('Hamster', 'hamster')], max_length=10)),
                ('year_of_birth', models.IntegerField(validators=[django.core.validators.MinValueValidator(1950, message='Year of birth must be before 1950'), django.core.validators.MaxValueValidator(2023, message="Year of birth can't be in the future")])),
            ],
        ),
    ]
