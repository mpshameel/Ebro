from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class profile(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    phone = models.BigIntegerField(null=True,blank=True,default='0000000000',editable=True)
    # PhoneNumberField(null=False, blank=False,default='0000000000',editable=True,unique=False)
    # models.BigIntegerField(null=True,blank=True,default='0000000000',editable=True)
    alternative_phone = models.BigIntegerField(null=True,blank=True)
    dob = models.CharField(max_length=100,null=True,blank=True)
    adhar_id = models.CharField(max_length=100,null=True,blank=True)
    qualification = models.CharField(max_length=100,null=True,blank=True)
    hobbies = models.CharField(max_length=100,null=True,blank=True)
    summary = models.CharField(max_length=500,null=True,blank=True)
    image = models.ImageField(upload_to='profile-pic',null=True,blank=True)
    refferalcode = models.CharField(max_length=100,null=True,blank=True)
    usertype = models.CharField(max_length=100,null=False,blank=True)
    profession = models.CharField(max_length=100,null=False,blank=True)
    location = models.CharField(max_length=100,null=False,blank=True)
    wallet = models.FloatField(null=True,blank=True,default='0',editable=True)
    coins = models.BigIntegerField(null=True,blank=True,default='0',editable=True)
    myrefferalid = models.CharField(max_length=100,null=False,blank=True,editable=True)
    myrefferalcount = models.BigIntegerField(null=True,blank=True,default='0',editable=True)




class category(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    profile = models.ForeignKey(profile,on_delete=models.CASCADE)
    category = models.CharField(max_length=100,null=False,blank=True)
    subcategorycount = models.BigIntegerField(null=True,blank=True,default='0',editable=True)


class subcategory(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    profile = models.ForeignKey(profile,on_delete=models.CASCADE)
    category = models.ForeignKey(category,on_delete=models.CASCADE)
    subcategory = models.CharField(max_length=100,null=False,blank=True)



class categorys(models.Model):
    name                = models.CharField(max_length=200)
    slug                = models.SlugField(max_length=200, null=True, blank=True)
    main_category       = models.BooleanField(default=True, blank=True, null=True)
    parent              = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True ,related_name='children')
    domain_name         = models.CharField(max_length=200, default='www.bichatravels.com')
    status              = models.BooleanField(default=True, blank=False, null=False)
    is_deleted          = models.BooleanField(default=False, blank=False, null=False)
    created_at          = models.DateTimeField(auto_now_add=True,blank=False, null=False)
    updated_at          = models.DateTimeField(auto_now=True, blank=False, null=False)




class ads(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    profile = models.ForeignKey(profile,on_delete=models.CASCADE)
    adname = models.CharField(max_length=100,null=False,blank=True)
    clicksall = models.IntegerField(null=True,blank=True,default='0')
    image = models.ImageField(upload_to='ads/ads_pic',null=True,blank=True)
    adsize = models.CharField(max_length=100,null=False,blank=True)


class adclicks(models.Model):
    profile = models.ForeignKey(profile,on_delete=models.CASCADE)
    ad = models.ForeignKey(ads,on_delete=models.CASCADE)
    userclicks = models.IntegerField(null=True,blank=True,default='0')







class address(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    profile = models.ForeignKey(profile,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100,null=True,blank=True)
    last_name = models.CharField(max_length=100,null=True,blank=True)
    country = models.CharField(max_length=100,null=True,blank=True)
    state = models.CharField(max_length=100,null=True,blank=True)
    district = models.CharField(max_length=100,null=True,blank=True)
    postalcode = models.BigIntegerField(null=True,blank=True)
    phone = models.BigIntegerField(null=True,blank=True)
    alternative_phone = models.BigIntegerField(null=True,blank=True)
    address_line_1 = models.CharField(max_length=300,null=True,blank=True)
    address_line_2 = models.CharField(max_length=300,null=True,blank=True)


class delivery_address(models.Model):
    address = models.ForeignKey(address,on_delete=models.CASCADE)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    profile = models.ForeignKey(profile,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100,null=True,blank=True)
    last_name = models.CharField(max_length=100,null=True,blank=True)
    country = models.CharField(max_length=100,null=True,blank=True)
    state = models.CharField(max_length=100,null=True,blank=True)
    district = models.CharField(max_length=100,null=True,blank=True)
    postalcode = models.BigIntegerField(null=True,blank=True)
    phone = models.BigIntegerField(null=True,blank=True)
    alternative_phone = models.BigIntegerField(null=True,blank=True)
    address_line_1 = models.CharField(max_length=300,null=True,blank=True)
    address_line_2 = models.CharField(max_length=300,null=True,blank=True)




  



class deals(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    publish = models.CharField(max_length=100,null=True,blank=True)
    deal_name = models.CharField(max_length=100,null=True,blank=True)
    price = models.FloatField(null=True,blank=True)
    category = models.ManyToManyField(categorys)
    email = models.CharField(max_length=100,null=True,blank=True)
    contact = models.BigIntegerField(null=True,blank=True)
    location = models.CharField(max_length=100,null=True,blank=True)
    deal_type = models.CharField(max_length=100,null=True,blank=True)
    brand_name = models.CharField(max_length=100,null=True,blank=True)
    picture = models.ImageField(upload_to='deals/deals_pic',null=True,blank=True)
    # attachments = models.FileField(upload_to='deals/deals_attachments',null=True,blank=True)
    details = models.CharField(max_length=500,null=True,blank=True)

class deal_attachments(models.Model):
    deal = models.ForeignKey(deals,on_delete=models.CASCADE)
    attachment = models.FileField(upload_to='deals/deals_attachments',null=True,blank=True)


class assign_deal(models.Model):
    deal = models.ForeignKey(deals,on_delete=models.CASCADE)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    assigns = models.ForeignKey(profile,on_delete=models.CASCADE)




class deal_wish(models.Model):
    deal = models.ForeignKey(deals,on_delete=models.CASCADE)
    username = models.ForeignKey(User,on_delete=models.CASCADE)

####
class deal_cart(models.Model):
    deal = models.ForeignKey(deals,on_delete=models.CASCADE)
    username = models.ForeignKey(User,on_delete=models.CASCADE)



class jobs(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    publish = models.CharField(max_length=100,null=True,blank=True)
    job_name = models.CharField(max_length=100,null=True,blank=True)
    price = models.FloatField(null=True,blank=True)
    category = models.ManyToManyField(categorys)
    email = models.CharField(max_length=100,null=True,blank=True)
    contact = models.BigIntegerField(null=True,blank=True)
    location = models.CharField(max_length=100,null=True,blank=True)
    job_type = models.CharField(max_length=100,null=True,blank=True)
    brand_name = models.CharField(max_length=100,null=True,blank=True)
    picture = models.ImageField(upload_to='jobs/jobs_pic',null=True,blank=True)
    # attachments = models.FileField(upload_to='deals/deals_attachments',null=True,blank=True)
    details = models.CharField(max_length=500,null=True,blank=True)

class job_attachments(models.Model):
    job = models.ForeignKey(jobs,on_delete=models.CASCADE)
    attachment = models.FileField(upload_to='jobs/jobs_attachments',null=True,blank=True)


class assign_job(models.Model):
    job = models.ForeignKey(jobs,on_delete=models.CASCADE)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    assigns = models.ForeignKey(profile,on_delete=models.CASCADE)


class job_wish(models.Model):
    job = models.ForeignKey(jobs,on_delete=models.CASCADE)
    username = models.ForeignKey(User,on_delete=models.CASCADE)




class products(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    publish = models.CharField(max_length=100,null=True,blank=True)
    product_name = models.CharField(max_length=100,null=True,blank=True)
    price = models.FloatField(null=True,blank=True)
    category = models.ManyToManyField(categorys)
    email = models.CharField(max_length=100,null=True,blank=True)
    contact = models.BigIntegerField(null=True,blank=True)
    location = models.CharField(max_length=100,null=True,blank=True)
    product_type = models.CharField(max_length=100,null=True,blank=True)
    brand_name = models.CharField(max_length=100,null=True,blank=True)
    picture = models.ImageField(upload_to='products/products_pic',null=True,blank=True)
    # attachments = models.FileField(upload_to='deals/deals_attachments',null=True,blank=True)
    details = models.CharField(max_length=500,null=True,blank=True)
    stock = models.BigIntegerField(null=True,blank=True,default='1',editable=True)
    offer = models.BigIntegerField(null=True,blank=True,default='0',editable=True)
    oldprice = models.FloatField(null=True,blank=True,editable=True)


    class Meta:
        ordering=['location']

    def __str__(self):
        return self.location




class product_attachments(models.Model):
    product = models.ForeignKey(products,on_delete=models.CASCADE)
    attachment = models.FileField(upload_to='products/products_attachments',null=True,blank=True)



class product_wish(models.Model):
    product = models.ForeignKey(products,on_delete=models.CASCADE)
    username = models.ForeignKey(User,on_delete=models.CASCADE)


# class Order(models.Model):
#     username = models.ForeignKey(User,on_delete=models.CASCADE)
#     quantity = models.BigIntegerField(null=True,blank=True,default='1',editable=True)


class product_cart(models.Model):
    product = models.ForeignKey(products,on_delete=models.CASCADE)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    quantity = models.BigIntegerField(null=True,blank=True,default='1',editable=True)

# class Order(models.Model):
#     customer = models.ForeignKey(products,on_delete=models.CASCADE)
#     username = models.ForeignKey(User,on_delete=models.CASCADE)
#     quantity = models.BigIntegerField(null=True,blank=True,default='1',editable=True)







class notifications(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    notification = models.CharField(max_length=500,null=True,blank=True)


class feedbacks(models.Model):
    username = models.ForeignKey(profile,on_delete=models.CASCADE)
    feedback = models.CharField(max_length=500,null=True,blank=True)









class orders(models.Model):
    address = models.ForeignKey(delivery_address,on_delete=models.CASCADE)

    username = models.ForeignKey(User,on_delete=models.CASCADE)
    profile = models.ForeignKey(profile,on_delete=models.CASCADE)

    product = models.ForeignKey(products,on_delete=models.CASCADE)
    product_count = models.IntegerField(null=True,blank=True)

    cart_count =  models.IntegerField(null=True,blank=True)

    amount = models.FloatField(default=0)

    status = models.CharField(max_length=100,null=True,blank=True,default="ordered")

    payment_status = models.CharField(max_length=100,null=True,blank=True,default="pending")

    delivery_date = models.IntegerField(null=True,blank=True,default="10")

    # created = models.DateTimeField(auto_now_add=True)

    product_name = models.CharField(max_length=100,null=True,blank=True)
    price = models.BigIntegerField(null=True,blank=True)
    email = models.CharField(max_length=100,null=True,blank=True)
    contact = models.BigIntegerField(null=True,blank=True)
    brand_name = models.CharField(max_length=100,null=True,blank=True)
    picture = models.ImageField(upload_to='orders/orders_pic',null=True,blank=True)


    first_name = models.CharField(max_length=100,null=True,blank=True)
    last_name = models.CharField(max_length=100,null=True,blank=True)
    country = models.CharField(max_length=100,null=True,blank=True)
    state = models.CharField(max_length=100,null=True,blank=True)
    district = models.CharField(max_length=100,null=True,blank=True)
    postalcode = models.BigIntegerField(null=True,blank=True)
    phone = models.BigIntegerField(null=True,blank=True)
    alternative_phone = models.BigIntegerField(null=True,blank=True)
    address_line_1 = models.CharField(max_length=300,null=True,blank=True)
    address_line_2 = models.CharField(max_length=300,null=True,blank=True)









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