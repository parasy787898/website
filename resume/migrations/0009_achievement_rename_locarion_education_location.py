# Generated by Django 4.1.5 on 2023-01-08 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0008_rename_current_loaction_about_me_current_loacation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('group', models.CharField(max_length=30)),
            ],
        ),
        migrations.RenameField(
            model_name='education',
            old_name='locarion',
            new_name='location',
        ),
    ]