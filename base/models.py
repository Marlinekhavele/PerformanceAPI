import uuid
from django.urls import reverse
from django.core.validators import RegexValidator
from datetime import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _



# Create your models here.
class Performance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    channel= models.CharField(_("Channel"), max_length=25)
    country	= models.CharField(_("Channel"), max_length=25)
    os = models.CharField(_("Channel"), max_length=25)
    impressions = models.IntegerField(_("Impressions"), default=0)
    clicks = models.IntegerField(_("Clicks"), default=0)
    installs =models.IntegerField(_("Installs"), default=0)
    spend= models.DecimalField( _("Spend"),decimal_places=2, max_digits=15, default=1.0 )
    revenue = models.DecimalField(_("Revenue"), decimal_places=2, max_digits=15, default=1.0 )
    date = models.DateTimeField(auto_now_add=True, editable=False)


    def __str__(self):
        return self.channel
