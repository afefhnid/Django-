# Generated by Django 3.0.7 on 2020-06-06 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accueil', '0003_delete_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
