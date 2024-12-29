from django.db import migrations

def create_default_category(apps, schema_editor):
    Category = apps.get_model('inventory', 'Category')
    Category.objects.create(id=1, name='Generic')

class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_category_product_category'),
    ]

    operations = [
        migrations.RunPython(create_default_category),
    ]