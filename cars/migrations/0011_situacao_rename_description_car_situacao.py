# Generated by Django 5.1.2 on 2024-12-12 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0010_carinventory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Situacao',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.RenameField(
            model_name='car',
            old_name='description',
            new_name='situacao',
        ),
    ]
