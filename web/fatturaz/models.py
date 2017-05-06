# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Invoice(models.Model):
	"""An Invoice"""
	invoice_date = models.DateTimeField(auto_now_add=False)
	invoice_number = models.CharField(max_length=2)
	text=models.CharField(max_length=400)

	def __str__(self):
		"""Return a string representation of the model."""
		return self.text
