# Generated by Django 4.0.4 on 2022-05-10 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, db_index=True, max_length=255555, verbose_name='name')),
                ('age', models.IntegerField(blank=True, default=0, verbose_name='age')),
                ('salary', models.IntegerField(blank=True, default=0, verbose_name='salary')),
                ('skill', models.CharField(blank=True, db_index=True, max_length=255555, verbose_name='skill')),
                ('image', models.ImageField(blank=True, upload_to='image/%Y/%m/%d', verbose_name='Фотки')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('public', models.BooleanField(default=True, verbose_name='Опубликованно')),
            ],
        ),
    ]
