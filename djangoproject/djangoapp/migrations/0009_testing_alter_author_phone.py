# Generated by Django 5.1.3 on 2024-12-13 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0008_author_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_lawn', models.ImageField(upload_to='image')),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='author',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
