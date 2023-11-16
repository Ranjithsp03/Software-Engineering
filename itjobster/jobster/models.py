from django.db import models

class administrator(models.Model):
    adminname=models.EmailField(max_length=100)
    adminpass=models.CharField(max_length=25)

class user(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=100,primary_key=True)
    age=models.IntegerField()
    phone=models.BigIntegerField()
    location=models.CharField(max_length=100)
    aadhar=models.BigIntegerField()
    password=models.CharField(max_length=100)


class company(models.Model):
    cid=models.AutoField(primary_key=True,unique=True)
    gstin=models.CharField(max_length=100,unique=True)
    companyname=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    contact=models.BigIntegerField()
    password=models.CharField(max_length=100)


class Resume(models.Model):
   
    name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    email = models.EmailField(primary_key=True,unique=True)
    phone = models.CharField(max_length=20)
    website = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    
    # Education
    degree = models.CharField(max_length=255)
    university = models.CharField(max_length=255)
    graduation_year = models.CharField(max_length=4)
    
    # Expertise
    skills = models.TextField()
    
    # Languages
    spoken_languages = models.TextField()
    
    # Experience
    job_experience = models.TextField()
    
    # Description
    personal_description = models.TextField()


class postjob(models.Model):
    cid=models.ForeignKey(company,on_delete=models.CASCADE)
    jid=models.AutoField(primary_key=True,unique=True)
    jtitle = models.CharField(max_length=255)
    jlocation = models.IntegerField()
    jtype = models.CharField(max_length=255)
    jskills = models.TextField()
    jexperience = models.TextField()
    jvacancies = models.IntegerField()

class cprofile(models.Model):
    cid=models.ForeignKey(company,on_delete=models.CASCADE)
    cname = models.CharField(max_length=255)
    cwebsite = models.URLField(default="https://")
    clocations = models.TextField()  # Assuming multiple locations will be stored as text
    jpostername = models.CharField(max_length=255)
    jposterdesignation = models.CharField(max_length=255)
    jposteremail = models.EmailField()
    jposterphone = models.CharField(max_length=20)
    description = models.TextField()
