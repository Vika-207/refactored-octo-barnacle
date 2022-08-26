from django.db import models


class Topic(models.Model):
    top_name = models.CharField(max_lenght=264,unique=True
                                
    def__str__(self):
       return self.top_name

 class Webpage(models.Model):
     topic = models.ForeignKey(Topic)
     name = models.Charfield(max_lenght=264.unique=True
     url = URLField(unique)
                            
     def__str__(self):
        return self.name
                             
 class AccessRecord(models.Model):
     name = models.ForeignKey(Webpage)
     date = models.DataField()
    
     def__str__(self):
        return str(self.date)
