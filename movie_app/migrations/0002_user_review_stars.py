# Generated by Django 5.1.6 on 2025-02-22 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('is_active', models.BooleanField(default=False)),
                ('confirmation_code', models.CharField(blank=True, max_length=6)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='review',
            name='stars',
            field=models.IntegerField(default=1),
        ),
    ]
