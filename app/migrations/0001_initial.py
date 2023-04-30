# Generated by Django 4.2 on 2023-04-26 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(max_length=20)),
                ('Lname', models.CharField(max_length=20, null=True)),
                ('Age', models.IntegerField(null=True)),
                ('Bloodgroup', models.CharField(choices=[('A+', 'A+'), ('B+', 'B+'), ('AB+', 'AB+'), ('O+', 'O+')], max_length=10, null=True)),
            ],
        ),
    ]
