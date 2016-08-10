# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0005_auto_20160809_2256'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='list',
            new_name='listx',
        ),
    ]
