from __future__ import unicode_literals

from django.db import models

class Asset(models.Model):
	asset_name	=	models.CharField(max_length=254)
	date_created	=	models.DateTimeField('date created')
	device_count	=	models.IntegerField(default=1,max_ports=8)
	asset_latitude	=	models.IntegerField(default=0)
	asset_longitude =	models.IntegerField(default=0)
	asset_owner	=	models.ForeignKey(Owner, on_delete=models.CASCADE)
	asset_operator	=	models.ForeignKey(Employee, on_delete=models.CASCADE)

