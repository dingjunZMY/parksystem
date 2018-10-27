from django.db import models

# Create your models here.
import uuid
class Company(models.Model):

    company_id=models.CharField(primary_key=True,max_length=32,default=uuid.uuid1().hex)
    company_name=models.CharField(max_length=50,null=True,db_index=True)
    updated_time=models.DateTimeField(auto_now=True,null=True)
    created_time=models.DateTimeField(auto_now_add=True,db_index=True,null=True)



    class Meta:
        db_table='Company'

    def detail_info(self):
        return{
            'company_id':self.company_id,
            'company_name':self.company_name,
            'updated_time':str(self.updated_time),
            'create_time':str(self.created_time)
        }

    def __str__(self):
        return '%s,%s,%s,%s'%(self.company_id,self.company_name,self.updated_time,self.created_time)