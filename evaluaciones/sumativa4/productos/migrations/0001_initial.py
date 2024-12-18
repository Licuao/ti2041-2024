# Generated by Django 5.1.1 on 2024-12-11 13:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Caracteristica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Característica',
                'verbose_name_plural': 'Características',
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
            },
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Marca',
                'verbose_name_plural': 'Marcas',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=20, unique=True)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField(blank=True)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='productos.categoria')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.marca')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'ordering': ['-fecha_actualizacion'],
            },
        ),
        migrations.CreateModel(
            name='ProductoCaracteristica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.CharField(max_length=100)),
                ('caracteristica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.caracteristica')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.producto')),
            ],
            options={
                'verbose_name': 'Característica de producto',
                'verbose_name_plural': 'Características de productos',
                'unique_together': {('producto', 'caracteristica')},
            },
        ),
        migrations.AddField(
            model_name='producto',
            name='caracteristicas',
            field=models.ManyToManyField(related_name='productos', through='productos.ProductoCaracteristica', to='productos.caracteristica'),
        ),
    ]
