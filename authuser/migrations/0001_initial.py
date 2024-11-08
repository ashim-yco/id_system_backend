# Generated by Django 5.1.3 on 2024-11-08 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='NAME', max_length=255)),
                ('username', models.CharField(db_column='USERNAME', max_length=255, unique=True)),
                ('email', models.EmailField(blank=True, db_column='EMAIL', max_length=254)),
                ('password', models.CharField(db_column='PASSWORD', max_length=255)),
                ('address', models.CharField(db_column='ADDRESS', max_length=255)),
                ('designation', models.CharField(db_column='DESIGNATION', max_length=255)),
                ('is_full_time', models.BooleanField(db_column='FULLTIME', default=True)),
                ('contact', models.CharField(blank=True, db_column='CONTACT', max_length=255, null=True, unique=True)),
            ],
            options={
                'db_table': 'USER',
            },
        ),
    ]
