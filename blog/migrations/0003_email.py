# Generated by Django 2.0 on 2019-11-08 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20191107_0104'),
    ]

    operations = [
        migrations.CreateModel(
            name='email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.EmailField(max_length=254)),
            ],
        ),
    ]