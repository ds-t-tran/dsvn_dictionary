# Generated by Django 3.2.4 on 2021-07-07 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dsvn_dictionary', '0007_vi_dictionary_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ja_Dictionary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hiragana_text', models.CharField(blank=True, default='', max_length=200)),
                ('kanji_text', models.CharField(blank=True, default='', max_length=200)),
                ('katakana_text', models.CharField(blank=True, default='', max_length=200)),
                ('vi_text', models.CharField(blank=True, default='', max_length=200)),
                ('description', models.CharField(blank=True, default='', max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]