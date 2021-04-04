# Generated by Django 3.1.7 on 2021-04-02 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_article_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('Food', 'Food'), ('Economy', 'Economy'), ('International', 'International'), ('News', 'News'), ('Music', 'Music'), ('Sport', 'Sport'), ('Technology', 'Technology'), ('Health', 'Health')], default=('Select a category', None), max_length=50),
        ),
    ]