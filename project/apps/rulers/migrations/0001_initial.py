# Generated by Django 2.0.1 on 2018-02-01 21:21

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ruler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='Имя')),
                ('url', models.TextField(db_index=True, unique=True, validators=[django.core.validators.URLValidator()], verbose_name='Ссылка на страницу в википедии')),
                ('succession_order', models.PositiveIntegerField(verbose_name='Порядок наследования')),
                ('predecessor', models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='successor', to='rulers.Ruler', verbose_name='Предшественник')),
            ],
            options={
                'ordering': ('succession_order',),
            },
        ),
    ]
