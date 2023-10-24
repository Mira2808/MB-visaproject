# Generated by Django 4.2.6 on 2023-10-24 06:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('visapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adviserprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.BigIntegerField()),
                ('date_of_birth', models.DateField()),
                ('experience', models.FloatField()),
                ('qualification', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('location', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Adviserprofile',
            },
        ),
        migrations.CreateModel(
            name='Clientprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.BigIntegerField()),
                ('date_of_birth', models.DateField()),
                ('current_education', models.CharField(choices=[('below 12', 'below 12'), ('12', '12'), ('diploma', 'diploma'), ('graduate', 'graduate'), ('masters', 'masters')], max_length=20)),
                ('IELTSAppeared', models.BooleanField()),
            ],
            options={
                'verbose_name_plural': 'clientprofile',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=128)),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'country',
            },
        ),
        migrations.CreateModel(
            name='document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marksheet', models.FileField(upload_to='')),
            ],
            options={
                'verbose_name_plural': 'document',
            },
        ),
        migrations.CreateModel(
            name='Inquirey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.BigIntegerField()),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'inquirey',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_no', models.CharField(max_length=50)),
                ('amount', models.BigIntegerField()),
                ('status', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'payment',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'service',
            },
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
        migrations.AddField(
            model_name='payment',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visapp.service'),
        ),
        migrations.AddField(
            model_name='payment',
            name='user_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='clientprofile',
            name='documnent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visapp.document'),
        ),
        migrations.AddField(
            model_name='clientprofile',
            name='user_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='adviserprofile',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visapp.service'),
        ),
        migrations.AddField(
            model_name='adviserprofile',
            name='user_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]