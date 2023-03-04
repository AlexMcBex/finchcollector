# Generated by Django 4.1.7 on 2023-03-04 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ribbon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Day of Gift')),
                ('color', models.CharField(choices=[('G', 'Golden Ribbon'), ('R', 'Red Ribbon'), ('B', 'Blue Ribbon')], default=0, max_length=1)),
                ('finch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.finch')),
            ],
        ),
    ]
