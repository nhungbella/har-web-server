# Generated by Django 3.0.7 on 2020-06-26 14:54

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
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('altitude', models.FloatField()),
                ('accuracy', models.FloatField(blank=True, null=True)),
                ('creation_time', models.DateTimeField()),
                ('update_time', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'report',
            },
        ),
    ]