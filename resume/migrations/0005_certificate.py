# Generated by Django 4.1.5 on 2023-01-06 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_portfolio_alter_client_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('group', models.CharField(max_length=30)),
            ],
        ),
    ]
