<<<<<<< HEAD
# Generated by Django 4.0.4 on 2022-07-21 00:12
=======
# Generated by Django 4.0.4 on 2022-07-20 23:44
>>>>>>> 0b3823a (update)

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('material', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=255)),
                ('picture', models.ImageField(blank=True, upload_to='uploads/')),
                ('hardware', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(default=0)),
                ('picture', models.ImageField(blank=True, upload_to='profile_pics')),
                ('username', models.CharField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.case')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=250)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.case')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
        migrations.AddField(
            model_name='case',
            name='components',
            field=models.ManyToManyField(to='main_app.component'),
        ),
        migrations.AddField(
            model_name='case',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
