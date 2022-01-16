# Generated by Django 4.0.1 on 2022-01-16 01:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='spot',
            name='description',
            field=models.TextField(default='parking spot', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='spot',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startdate', models.DateField(verbose_name='start date')),
                ('enddate', models.DateField(verbose_name='end date')),
                ('spot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.spot')),
            ],
            options={
                'ordering': ['-startdate'],
            },
        ),
        migrations.AddField(
            model_name='spot',
            name='Features',
            field=models.ManyToManyField(to='main_app.Feature'),
        ),
    ]