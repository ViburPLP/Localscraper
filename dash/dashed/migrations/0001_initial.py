# Generated by Django 5.0.6 on 2024-06-19 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discharge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('payer', models.CharField(max_length=255)),
                ('membership_number', models.CharField(max_length=255)),
                ('relationship', models.CharField(max_length=255)),
                ('validity', models.CharField(max_length=255)),
                ('scheme', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Discharged',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('payer', models.CharField(max_length=255)),
                ('membership_number', models.CharField(max_length=255)),
                ('relationship', models.CharField(max_length=255)),
                ('validity', models.CharField(max_length=255)),
                ('scheme', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MemberDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('payer', models.CharField(max_length=255)),
                ('membership_number', models.CharField(max_length=255)),
                ('relationship', models.CharField(max_length=255)),
                ('validity', models.CharField(max_length=255)),
                ('scheme', models.CharField(max_length=255)),
            ],
        ),
    ]