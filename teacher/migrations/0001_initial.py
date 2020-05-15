# Generated by Django 2.2.12 on 2020-05-15 16:10

from django.db import migrations, models
import django.db.models.deletion
import teacher.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reference', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(max_length=40, verbose_name='имя')),
                ('name', models.CharField(max_length=255, verbose_name='полное имя')),
                ('image', models.FileField(upload_to=teacher.models.get_file_path, verbose_name='фотография')),
                ('position', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reference.Position', verbose_name='должность')),
            ],
            options={
                'verbose_name': 'тренер',
                'verbose_name_plural': 'тренеры',
            },
        ),
    ]
