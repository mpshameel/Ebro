from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class profile(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    phone = models.BigIntegerField(null=True,blank=True)
    alternative_phone = models.BigIntegerField(null=True,blank=True)
    dob = models.CharField(max_length=100,null=True,blank=True)
    adhar_id = models.CharField(max_length=100,null=True,blank=True)
    qualification = models.CharField(max_length=100,null=True,blank=True)
    hobbies = models.CharField(max_length=100,null=True,blank=True)
    summary = models.CharField(max_length=100,null=True,blank=True)
    image = models.ImageField(upload_to='profile-pic',null=True,blank=True)
    refferalcode = models.CharField(max_length=100,null=True,blank=True)
    usertype = models.CharField(max_length=100,null=False,blank=True)
    profession = models.CharField(max_length=100,null=False,blank=True)
    location = models.CharField(max_length=100,null=False,blank=True)




class deals(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    publish = models.CharField(max_length=100,null=True,blank=True)
    deal_name = models.CharField(max_length=100,null=True,blank=True)
    price = models.BigIntegerField(null=True,blank=True)
    category = models.CharField(max_length=100,null=True,blank=True)
    email = models.CharField(max_length=100,null=True,blank=True)
    contact = models.BigIntegerField(null=True,blank=True)
    location = models.CharField(max_length=100,null=True,blank=True)
    deal_type = models.CharField(max_length=100,null=True,blank=True)
    brand_name = models.CharField(max_length=100,null=True,blank=True)
    picture = models.ImageField(upload_to='deals/deals_pic',null=True,blank=True)
    # attachments = models.FileField(upload_to='deals/deals_attachments',null=True,blank=True)
    details = models.CharField(max_length=100,null=True,blank=True)

class deal_attachments(models.Model):
    deal = models.ForeignKey(deals,on_delete=models.CASCADE)
    attachment = models.FileField(upload_to='deals/deals_attachments',null=True,blank=True)


class assign_deal(models.Model):
    deal = models.ForeignKey(deals,on_delete=models.CASCADE)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    assigns = models.CharField(max_length=100,null=True,blank=True)



class jobs(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    publish = models.CharField(max_length=100,null=True,blank=True)
    job_name = models.CharField(max_length=100,null=True,blank=True)
    price = models.BigIntegerField(null=True,blank=True)
    category = models.CharField(max_length=100,null=True,blank=True)
    email = models.CharField(max_length=100,null=True,blank=True)
    contact = models.BigIntegerField(null=True,blank=True)
    location = models.CharField(max_length=100,null=True,blank=True)
    job_type = models.CharField(max_length=100,null=True,blank=True)
    brand_name = models.CharField(max_length=100,null=True,blank=True)
    picture = models.ImageField(upload_to='jobs/jobs_pic',null=True,blank=True)
    # attachments = models.FileField(upload_to='deals/deals_attachments',null=True,blank=True)
    details = models.CharField(max_length=100,null=True,blank=True)

class job_attachments(models.Model):
    job = models.ForeignKey(jobs,on_delete=models.CASCADE)
    attachment = models.FileField(upload_to='jobs/jobs_attachments',null=True,blank=True)


class assign_job(models.Model):
    job = models.ForeignKey(jobs,on_delete=models.CASCADE)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    assigns = models.CharField(max_length=100,null=True,blank=True)



class products(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    publish = models.CharField(max_length=100,null=True,blank=True)
    product_name = models.CharField(max_length=100,null=True,blank=True)
    price = models.BigIntegerField(null=True,blank=True)
    category = models.CharField(max_length=100,null=True,blank=True)
    email = models.CharField(max_length=100,null=True,blank=True)
    contact = models.BigIntegerField(null=True,blank=True)
    location = models.CharField(max_length=100,null=True,blank=True)
    product_type = models.CharField(max_length=100,null=True,blank=True)
    brand_name = models.CharField(max_length=100,null=True,blank=True)
    picture = models.ImageField(upload_to='products/products_pic',null=True,blank=True)
    # attachments = models.FileField(upload_to='deals/deals_attachments',null=True,blank=True)
    details = models.CharField(max_length=100,null=True,blank=True)

class product_attachments(models.Model):
    product = models.ForeignKey(products,on_delete=models.CASCADE)
    attachment = models.FileField(upload_to='products/products_attachments',null=True,blank=True)


class notifications(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    notification = models.CharField(max_length=100,null=True,blank=True)


class feedbacks(models.Model):
    username = models.ForeignKey(profile,on_delete=models.CASCADE)
    feedback = models.CharField(max_length=100,null=True,blank=True)



# class LoggedUser(models.Model):
#     user = models.ForeignKey(User, primary_key=True)

#     def __unicode__(self):
#         return self.user.username

#     def login_user(sender, request, user, **kwargs):
#         LoggedUser(user=user).save()

#     def logout_user(sender, request, user, **kwargs):
#         try:
#             u = LoggedUser.objects.get(user=user)
#             u.delete()
#         except LoggedUser.DoesNotExist:
#             pass

#     user_logged_in.connect(login_user)
#     user_logged_out.connect(logout_user)
#     on_delete=models.DO_NOTHING,