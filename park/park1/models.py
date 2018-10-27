from django.db import models

# Create your models here.
import uuid

class Park1(models.Model):
    park_id = models.CharField(primary_key=True,max_length=32,default=uuid.uuid1().hex)
    park_name = models.CharField(max_length=200, null=True, db_index=True)
    updated_time = models.DateTimeField(auto_now=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True, db_index=True, null=True)

    company=models.ForeignKey(
        'company.Company',
        related_name='park1_company',
        on_delete=models.SET_NULL,null=True
    )


    class Meta:
        db_table='Park1'

    def __str__(self):
        return "%s----,%s----,%s----,%s----,%s" % (self.park_id, self.park_name, self.updated_time, self.created_time,self.company_id)



