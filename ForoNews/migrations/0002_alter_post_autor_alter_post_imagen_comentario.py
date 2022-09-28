# Generated by Django 4.1 on 2022-09-28 09:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ForoNews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='pics'),
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('contenido', models.TextField()),
                ('fecha_creado', models.DateTimeField(auto_now_add=True)),
                ('activo', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='ForoNews.post')),
            ],
            options={
                'ordering': ['fecha_creado'],
            },
        ),
    ]
