# Generated by Django 4.0.6 on 2022-07-14 16:55

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128)),
                ('preco', models.IntegerField()),
                ('desc_preco', models.TextField(max_length=255)),
                ('tamanho', models.IntegerField(default=0)),
                ('desc_produto', models.TextField(max_length=400)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='produtos.categoria')),
            ],
        ),
    ]