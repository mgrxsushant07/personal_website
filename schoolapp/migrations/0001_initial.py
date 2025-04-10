# Generated by Django 5.1.6 on 2025-02-18 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='student_photos/')),
                ('name', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('class_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
    ]
