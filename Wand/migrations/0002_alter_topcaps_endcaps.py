# Generated by Django 4.1.2 on 2022-10-24 03:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Wand', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topcaps',
            name='endcaps',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Wand.endcaps'),
        ),
    ]
