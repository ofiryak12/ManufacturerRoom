from django.db import models

class pt(models.Model):
    client               = models.CharField(default='Capture',max_length=20)
    wiring               = models.BooleanField(null=False,default=False)
    wiring_detail        = models.TextField(blank=True,max_length=200)
    assembly             = models.BooleanField(null=False,default=False)
    assembly_detail      = models.TextField(blank=True,max_length=200)
    assembly_qa          = models.BooleanField(null=False,default=False)
    assembly_qa_detail   = models.TextField(blank=True,max_length=200)
    technosoft           = models.BooleanField(null=False,default=False)
    technosoft_detail    = models.TextField(blank=True,max_length=200)
    captrack             = models.BooleanField(null=False,default=False)
    captrack_detail      = models.TextField(blank=True,max_length=200)
    final_qa             = models.BooleanField(null=False,default=False)
    final_qa_detail      = models.TextField(blank=True,max_length=200)


# Create your models here.
