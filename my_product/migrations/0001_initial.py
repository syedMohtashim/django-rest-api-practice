# Generated by Django 4.0.5 on 2022-06-22 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, default=99.99, max_digits=15)),
            ],
        ),
    ]
