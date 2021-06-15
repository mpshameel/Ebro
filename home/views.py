from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from admin_phase.models import *
from django.http import JsonResponse
import json
from django.db.models import Sum
from django.db.models import F
# from hitcount.views import HitCountDetailView
# import datetime
# from django.utils import timezone
# from datetime import datetime



def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId:', productId)

    customer = User.objects.get(id=request.user.id)
    product = products.objects.get(id=productId)


    # order, created = Order.objects.get_or_create(username=customer)

    if product.stock >= 1:
        orderItem, created = product_cart.objects.get_or_create(username=customer, product=product)
        products.objects.filter(id=productId).update(stock=F('stock')+0)


    if product.stock >= 1:
        if action == 'add':
            orderItem.quantity = (orderItem.quantity + 1)
            products.objects.filter(id=productId).update(stock=F('stock')-1)

        elif action == 'remove':
            orderItem.quantity = (orderItem.quantity - 1)
            products.objects.filter(id=productId).update(stock=F('stock')+1)



    orderItem.save()
    # order.save()

    if orderItem.quantity <= 0:
        orderItem.delete()




    return JsonResponse('It was added', safe=False)



def update_adcount(request):
    data = json.loads(request.body)
    adId = data['adId']
    action = data['action']

    print('Action:', action)
    print('adId:', adId)

    ad = ads.objects.get(id=adId)


    if action == 'add':

        adItem, created = ads.objects.get_or_create(id=adId)
        adItem.clicksall = (adItem.clicksall + 1)
        adItem.save()

    return JsonResponse('It was added', safe=False)


def update_useradcount(request):
    data = json.loads(request.body)
    adId = data['adId']
    action = data['action']

    print('Action:', action)
    print('adId:', adId)

    user = User.objects.get(id=request.user.id)
    ad = ads.objects.get(id=adId)

    if action == 'add':
        adItem, created = ads.objects.get_or_create(id=adId)
        adItem.clicksall = (adItem.clicksall + 1)
        adItem.save()

        adUserItem, created = adclicks.objects.get_or_create(ad_id=adId)
        adUserItem.userclicks = (adUserItem.userclicks + 1)
        # adUserItem.username = user
        # adUserItem.ad_id = ad
        adUserItem.save()




    return JsonResponse('It was added', safe=False)


# Create your views here.


def user_home(request):
    if request.user.is_authenticated:

        items = product_cart.objects.filter(username=request.user.id)
        cart_count = sum(items.values_list('quantity', flat=True))

        user_profile = profile.objects.get(username_id=request.user.id)
        allads = ads.objects.all()
        ad_xxxl = ads.objects.filter(adsize="xxxl")
        ad_xxl = ads.objects.filter(adsize="xxl")
        ad_xl = ads.objects.filter(adsize="xl")
        ad_l = ads.objects.filter(adsize="l")
        ad_s = ads.objects.filter(adsize="s")

        context = {'user_profile':user_profile,'cart_count':cart_count,'allads':allads,'ad_xxxl':ad_xxxl,'ad_xxl':ad_xxl,'ad_xl':ad_xl,'ad_l':ad_l,'ad_s':ad_s}
        return render(request, 'user_home.html',context)
    else:
        allads = ads.objects.all()
        ad_xxxl = ads.objects.filter(adsize="xxxl")
        ad_xxl = ads.objects.filter(adsize="xxl")
        ad_xl = ads.objects.filter(adsize="xl")
        ad_l = ads.objects.filter(adsize="l")
        ad_s = ads.objects.filter(adsize="s")
        context = {'allads':allads,'ad_xxxl':ad_xxxl,'ad_xxl':ad_xxl,'ad_xl':ad_xl,'ad_l':ad_l,'ad_s':ad_s}
        return render(request, 'user_home.html',context)


def user_login(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']

        user = auth.authenticate(username=name,password=password)
        if user is not None:
            auth.login(request,user)
            messages.info(request,'User Logged in')
            return redirect('user_home')
            

        else:
            messages.info(request,'Invalid credentials')
            return redirect('user_home')

    else:
        return redirect('user_home')




def user_signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        refferalcode = request.POST['refferalcode']
        password1 = request.POST['password1']
        password2 = request.POST['password2']



        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,"Email already exist")
                return redirect('user_home')
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=email,email=email,password=password1)
                user.save()

                userid = str(user.id)

                pr = profile(username=user,phone=phone,refferalcode=refferalcode,usertype="free",myrefferalid="EBWD"+userid,coins="25").save()

                profile_list = profile.objects.all()
                for i in profile_list:
                    if refferalcode == i.myrefferalid:
                        profile_list_refferal = profile.objects.filter(myrefferalid=refferalcode).update(myrefferalcount=F('myrefferalcount')+1)


                messages.info(request,"Registered Successfully")
                return redirect('user_home')

        else:
            messages.info(request,'Password not matching')
            return redirect('user_home')

    else:
        return redirect('user_home')



def register_social(request):
    user=User.objects.get(id=request.user.id)

    userid = str(user.id)

    pr, created = profile.objects.get_or_create(username=user,usertype="free",myrefferalid="EBWD"+userid,coins="25")


    messages.info(request,"Registered Successfully")
    return redirect('/home')



def premium_user_signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        refferalcode = request.POST['refferalcode']
        password1 = request.POST['password1']
        password2 = request.POST['password2']



        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,"Email already exist")
                return redirect('user_home')
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=email,email=email,password=password1)
                user.save()

                userid = str(user.id)

                pr = profile(username=user,phone=phone,refferalcode=refferalcode,usertype="free",myrefferalid="EBWD"+userid,coins="25").save()

                profile_list = profile.objects.all()
                for i in profile_list:
                    if refferalcode == i.myrefferalid:
                        profile_list_refferal = profile.objects.filter(myrefferalid=refferalcode).update(myrefferalcount=F('myrefferalcount')+1)


                if user is not None:
                    auth.login(request,user)
                    messages.info(request,"Registered Successfully")
                    return redirect('premium_signup_payment')
                

        else:
            messages.info(request,'Password not matching')
            return redirect('user_home')

    else:
        return redirect('user_home')




def premium_signup_payment(request):
    user = User.objects.get(id=request.user.id)
    user_profile = profile.objects.get(username_id=request.user.id)

    items = product_cart.objects.filter(username=request.user.id)
    cart_count = sum(items.values_list('quantity', flat=True))
    context = {'user_profile':user_profile,'cart_count':cart_count}
    return render(request, 'premium_signup_payment.html',context)



def complete_premium_signup_payment(request):
    user_payment_premium = profile.objects.get(username_id=request.user.id)
    user_payment_premium.usertype = "premium"
    user_payment_premium.coins = "50"
    user_payment_premium.save()

    messages.info(request,'Welcome premium user')
    return redirect('user_home')

   





def profiles(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        # email = request.POST['email']
        phone = request.POST['phone']
        alternative_phone = request.POST['alternative_phone']
        dob = request.POST['dob']
        adhar_id = request.POST['adhar_id']
        profession = request.POST['profession']
        location = request.POST['location']
        qualification = request.POST['qualification']
        hobbies = request.POST['hobbies']
        summary = request.POST['summary']

        user = User.objects.get(id=request.user.id)
        user.first_name = first_name
        user.last_name= last_name
        # user.email= email
        # user.username = email
        user.save()
        
        user_update_profile = profile.objects.get(username_id=request.user.id)
        user_update_profile.phone = phone
        user_update_profile.alternative_phone = alternative_phone
        user_update_profile.dob = dob
        user_update_profile.adhar_id = adhar_id
        user_update_profile.profession = profession
        user_update_profile.adhar_id = adhar_id
        user_update_profile.location = location
        user_update_profile.hobbies = hobbies
        user_update_profile.summary = summary
        user_update_profile.save()

        messages.info(request,'Profile Updated')
        return redirect('profiles')


    else:
        items = product_cart.objects.filter(username=request.user.id)
        cart_count = sum(items.values_list('quantity', flat=True))

        user_address = address.objects.filter(username_id=request.user.id)
        user_profile = profile.objects.get(username_id=request.user.id)
        all_profiles = profile.objects.all()
        print("-----------------------------------------------------------------------------------------------",user_profile.myrefferalid)
        my_refferals = profile.objects.filter(refferalcode=user_profile.myrefferalid)
        context = {'user_profile':user_profile,'cart_count':cart_count,'user_address':user_address,'all_profiles':all_profiles,'my_refferals':my_refferals}
        return render(request, 'user_profile.html',context)



def update_user_profile_pic(request):
    if request.method == 'POST':
        image = request.FILES.get('img')
        
        profile_pic = profile.objects.get(username_id=request.user.id)
        profile_pic.image = image
        profile_pic.save()

        messages.info(request,'Profile-Pic Updated')
        return redirect('profiles')
    else:
        messages.info(request,'Profile-Pic Not Updated')
        return redirect('profiles')



def topup_payment(request):
    if request.method == 'POST':
        username = request.POST['username']

        amount = request.POST['amount']
        
        if User.objects.filter(id=request.user.id,username=username):
            items = product_cart.objects.filter(username=request.user.id)
            cart_count = sum(items.values_list('quantity', flat=True))

            amount = amount

            request.session['amount'] = amount

            user_profile = profile.objects.get(username_id=request.user.id)
            context = {'user_profile':user_profile,'cart_count':cart_count,'amount':amount}
            return render(request, 'user_topup_payment.html',context)

        else:
            messages.info(request,'Invalid credentials')
            return redirect('profiles')
    else:
        return redirect('profiles')

def topupcomplete(request):
    amount = request.session['amount']
    user_profile = profile.objects.filter(username_id=request.user.id).update(wallet=F('wallet')+amount,coins=F('coins')+10)
    
    messages.info(request,'Amount added to your wallet') 
    return redirect('profiles')


def sendmoney(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        amount = request.POST['amount']
        
        user_profile = profile.objects.filter(username_id=user_id).update(wallet=F('wallet')+amount)

        my_wallet = profile.objects.filter(username_id=request.user.id).update(wallet=F('wallet')-amount,coins=F('coins')+10)

        messages.info(request,'Amount sent successfully')
        return redirect('profiles')
    else:
        return redirect('profiles')






def voucher_claim(request):
    if request.method == 'POST':
        coins = request.POST['coins']

        coinses = int(coins)
        amount = coinses/10
        
        user_profile = profile.objects.filter(username_id=request.user.id).update(wallet=F('wallet')+amount,coins=F('coins')-coinses)

        messages.info(request,'Voucher Claimed Successfully')
        return redirect('profiles')
    else:
        return redirect('profiles')






def add_address(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        country = request.POST['country']
        state = request.POST['state']
        district = request.POST['district']
        postalcode = request.POST['postalcode']
        phone = request.POST['phone']
        alternative_phone = request.POST['alternative_phone']
        address_line_1 = request.POST['address_line_1']
        address_line_2 = request.POST['address_line_2']


        user = User.objects.get(id=request.user.id)
        user_profile = profile.objects.get(username_id=request.user.id)

        user_address = address(username=user,profile=user_profile,first_name=first_name,last_name=last_name,country=country,state=state,district=district,postalcode=postalcode,phone=phone,alternative_phone=alternative_phone,address_line_1=address_line_1,address_line_2=address_line_2)
        user_address.save()

        messages.info(request,'Address Added')
        return redirect('profiles')


    else:
        return redirect('profiles')









def offers(request):
    if request.user.is_authenticated:

        items = product_cart.objects.filter(username=request.user.id)
        cart_count = sum(items.values_list('quantity', flat=True))

        user_profile = profile.objects.get(username_id=request.user.id)
        # user = User.objects.get(id=request.user.id)
        user_products_list = products.objects.filter(publish="public").exclude(offer="0")
        context = {'user_products_list':user_products_list,'user_profile':user_profile,'cart_count':cart_count}
        return render(request, 'user_offers.html',context)
    else:
        user_products_list = products.objects.filter(publish="public").exclude(offer="0")
        context = {'user_products_list':user_products_list}
        return render(request, 'user_offers.html',context)



def detail_offers(request,id):
    if request.user.is_authenticated:
        items = product_cart.objects.filter(username=request.user.id)
        cart_count = sum(items.values_list('quantity', flat=True))

        user_profile = profile.objects.get(username_id=request.user.id)
        # user = User.objects.get(id=request.user.id)
        user_product =  products.objects.get(id=id)
        user_products_list = products.objects.filter(publish="public").exclude(offer="0")

        category_details = categorys.objects.filter(is_deleted=False)
        trade = user_product.category.all()
        context = {'user_products_list':user_products_list,'user_profile':user_profile,'user_product':user_product,'cart_count':cart_count,'category_details':category_details,'trade':trade}
        return render(request, 'user_detail_offers.html',context)
    else:
        user_product =  products.objects.get(id=id)
        user_products_list = products.objects.filter(publish="public").exclude(offer="0")

        category_details = categorys.objects.filter(is_deleted=False)
        trade = user_product.category.all()
        context = {'user_products_list':user_products_list,'user_product':user_product,'category_details':category_details,'trade':trade}
        return render(request, 'user_detail_offers.html',context)
        











def deal(request):
    if request.method == 'POST':
        publish = request.POST['publish']
        deal_name = request.POST['deal_name']
        price = request.POST['price']
        category = request.POST.getlist('category')
        # email = request.POST['email']
        # contact = request.POST['contact']
        location = request.POST['location']
        deal_type = request.POST['deal_type']
        brand_name = request.POST['brand_name']
        picture = request.FILES.get('picture')
        attach = request.FILES.getlist('attachments')
        details = request.POST['details']


        user = User.objects.get(id=request.user.id)
        
        pr = profile.objects.get(username_id=request.user.id)
        email = user.email
        contact = pr.phone

        user_deals_add = deals(username=user,publish=publish,deal_name=deal_name,price=price,location=location,deal_type=deal_type,brand_name=brand_name,picture=picture,email=email,contact=contact,details=details)
        user_deals_add.save()

        for i in category:
            user_deals_add.category.add(categorys.objects.get(id=i))

        ids = user_deals_add.id

        deal_id = deals.objects.get(id=ids)
        print("-------------------------------------------------------------",attach)
        for i in attach:
            print("-------------------------------------------------------------",i,deal_id)
            deal_attachments(deal=deal_id,attachment=i).save()
        
        messages.info(request,'Deal Added')
        return redirect('deal')


    else:
        if request.user.is_authenticated:
            items = product_cart.objects.filter(username=request.user.id)
            cart_count = sum(items.values_list('quantity', flat=True))

            user_profile = profile.objects.get(username_id=request.user.id)
            # user = User.objects.get(id=request.user.id)
            user_deals_list = deals.objects.filter(publish="public")
            category_details = categorys.objects.filter(is_deleted=False)
            context = {'user_deals_list':user_deals_list,'user_profile':user_profile,'cart_count':cart_count,'category_details':category_details}
            return render(request, 'user_deals.html',context)
        else:
            user_deals_list = deals.objects.filter(publish="public")
            category_details = categorys.objects.filter(is_deleted=False)
            context = {'user_deals_list':user_deals_list,'category_details':category_details}
            return render(request, 'user_deals.html',context)






def detail_deal(request,id):
    if request.user.is_authenticated:

        items = product_cart.objects.filter(username=request.user.id)
        cart_count = sum(items.values_list('quantity', flat=True))

        user_profile = profile.objects.get(username_id=request.user.id)
        # user = User.objects.get(id=request.user.id)
        user_deal =  deals.objects.get(id=id)
        user_deals_list = deals.objects.filter(publish="public")

        category_details = categorys.objects.filter(is_deleted=False)
        trade = user_deal.category.all()
        context = {'user_deals_list':user_deals_list,'user_profile':user_profile,'user_deal':user_deal,'cart_count':cart_count,'category_details':category_details,'trade':trade}
        return render(request, 'user_detail_deals.html',context)
    else:
        user_deal =  deals.objects.get(id=id)
        user_deals_list = deals.objects.filter(publish="public")

        category_details = categorys.objects.filter(is_deleted=False)
        trade = user_deal.category.all()
        context = {'user_deals_list':user_deals_list,'user_deal':user_deal,'category_details':category_details,'trade':trade}
        return render(request, 'user_detail_deals.html',context)
        




def job(request):
    if request.method == 'POST':
        publish = request.POST['publish']
        job_name = request.POST['job_name']
        price = request.POST['price']
        category = request.POST.getlist('category')
        # email = request.POST['email']
        # contact = request.POST['contact']
        location = request.POST['location']
        job_type = request.POST['job_type']
        brand_name = request.POST['brand_name']
        picture = request.FILES.get('picture')
        attach = request.FILES.getlist('attachments')
        details = request.POST['details']

        user = User.objects.get(id=request.user.id)

        pr = profile.objects.get(username_id=request.user.id)

        email = user.email
        contact = pr.phone
        
        user_jobs_add = jobs(username=user,publish=publish,job_name=job_name,price=price,location=location,job_type=job_type,brand_name=brand_name,email=email,contact=contact,picture=picture,details=details)
        user_jobs_add.save()

        for i in category:
            user_jobs_add.category.add(categorys.objects.get(id=i))

        ids = user_jobs_add.id

        job_id = jobs.objects.get(id=ids)
        print("-------------------------------------------------------------",attach)
        for i in attach:
            print("-------------------------------------------------------------",i,job_id)
            job_attachments(job=job_id,attachment=i).save()
        
        messages.info(request,'Job Added')
        return redirect('job')


    else:
        if request.user.is_authenticated:
            items = product_cart.objects.filter(username=request.user.id)
            cart_count = sum(items.values_list('quantity', flat=True))

            user_profile = profile.objects.get(username_id=request.user.id)
            # user = User.objects.get(id=request.user.id)
            user_jobs_list = jobs.objects.filter(publish="public")

            category_details = categorys.objects.filter(is_deleted=False)
            context = {'user_jobs_list':user_jobs_list,'user_profile':user_profile,'cart_count':cart_count,'category_details':category_details}
            return render(request, 'user_jobs.html',context)
        else:
            user_jobs_list = jobs.objects.filter(publish="public")

            category_details = categorys.objects.filter(is_deleted=False)
            context = {'user_jobs_list':user_jobs_list,'category_details':category_details}
            return render(request, 'user_jobs.html',context)




def detail_job(request,id):
    if request.user.is_authenticated:
        items = product_cart.objects.filter(username=request.user.id)
        cart_count = sum(items.values_list('quantity', flat=True))

        user_profile = profile.objects.get(username_id=request.user.id)
        # user = User.objects.get(id=request.user.id)
        user_job =  jobs.objects.get(id=id)
        user_jobs_list = jobs.objects.filter(publish="public")

        category_details = categorys.objects.filter(is_deleted=False)
        trade = user_job.category.all()
        context = {'user_jobs_list':user_jobs_list,'user_profile':user_profile,'user_job':user_job,'cart_count':cart_count,'category_details':category_details,'trade':trade}
        return render(request, 'user_detail_jobs.html',context)
    else:
        user_job =  jobs.objects.get(id=id)
        user_jobs_list = jobs.objects.filter(publish="public")

        category_details = categorys.objects.filter(is_deleted=False)
        trade = user_job.category.all()
        context = {'user_jobs_list':user_jobs_list,'user_job':user_job,'category_details':category_details,'trade':trade}
        return render(request, 'user_detail_jobs.html',context)





def product(request):
    if request.method == 'POST':
        publish = request.POST['publish']
        product_name = request.POST['product_name']
        price = request.POST['price']
        category = request.POST.getlist('category')
        # email = request.POST['email']
        # contact = request.POST['contact']
        location = request.POST['location']
        product_type = request.POST['product_type']
        brand_name = request.POST['brand_name']
        stock = request.POST['stock']
        picture = request.FILES.get('picture')
        attach = request.FILES.getlist('attachments')
        details = request.POST['details']

        user = User.objects.get(id=request.user.id)

        pr = profile.objects.get(username_id=request.user.id)

        email = user.email
        contact = pr.phone
        
        user_products_add = products(username=user,publish=publish,product_name=product_name,price=price,oldprice=price,location=location,product_type=product_type,brand_name=brand_name,stock=stock,email=email,contact=contact,picture=picture,details=details)
        user_products_add.save()

        for i in category:
            user_products_add.category.add(categorys.objects.get(id=i))

        ids = user_products_add.id

        product_id = products.objects.get(id=ids)
        print("-------------------------------------------------------------",attach)
        for i in attach:
            print("-------------------------------------------------------------",i,product_id)
            product_attachments(product=product_id,attachment=i).save()
        
        messages.info(request,'Product Added')
        return redirect('product')

    else:
        if request.user.is_authenticated:

            items = product_cart.objects.filter(username=request.user.id)
            cart_count = sum(items.values_list('quantity', flat=True))

            user_profile = profile.objects.get(username_id=request.user.id)
            # user = User.objects.get(id=request.user.id)
            user_products_list = products.objects.filter(publish="public")

            category_details = categorys.objects.filter(is_deleted=False)
            context = {'user_products_list':user_products_list,'user_profile':user_profile,'cart_count':cart_count,'category_details':category_details}
            return render(request, 'user_products.html',context)
        else:
            user_products_list = products.objects.filter(publish="public")

            category_details = categorys.objects.filter(is_deleted=False)
            context = {'user_products_list':user_products_list,'category_details':category_details}
            return render(request, 'user_products.html',context)



def detail_product(request,id):
    if request.user.is_authenticated:
        items = product_cart.objects.filter(username=request.user.id)
        cart_count = sum(items.values_list('quantity', flat=True))

        user_profile = profile.objects.get(username_id=request.user.id)
        # user = User.objects.get(id=request.user.id)
        user_product =  products.objects.get(id=id)
        user_products_list = products.objects.filter(publish="public")

        category_details = categorys.objects.filter(is_deleted=False)
        trade = user_product.category.all()
        context = {'user_products_list':user_products_list,'user_profile':user_profile,'user_product':user_product,'cart_count':cart_count,'category_details':category_details,'trade':trade}
        return render(request, 'user_detail_products.html',context)
    else:
        user_product =  products.objects.get(id=id)
        user_products_list = products.objects.filter(publish="public")

        category_details = categorys.objects.filter(is_deleted=False)
        trade = user_product.category.all()
        context = {'user_products_list':user_products_list,'user_product':user_product,'category_details':category_details,'trade':trade}
        return render(request, 'user_detail_products.html',context)
        









def myads(request):
    items = product_cart.objects.filter(username=request.user.id)
    cart_count = sum(items.values_list('quantity', flat=True))

    user = User.objects.get(id=request.user.id)
    user_deals_list = deals.objects.filter(username_id=request.user.id)
    user_jobs_list = jobs.objects.filter(username_id=request.user.id)
    user_products_list = products.objects.filter(username_id=request.user.id)
    user_profile = profile.objects.get(username_id=request.user.id)
    context = {'user':user,'user_deals_list':user_deals_list,'user_jobs_list':user_jobs_list,'user_products_list':user_products_list,'user_profile':user_profile,'cart_count':cart_count}
    return render(request, 'user_myads.html',context)





def myorders(request):
    items = product_cart.objects.filter(username=request.user.id)
    cart_count = sum(items.values_list('quantity', flat=True))

    items_in_order = orders.objects.filter(username=request.user.id)
    order_count = sum(items_in_order.values_list('product_count', flat=True))

    price = 0
    total_order_price = 0
    for i in items_in_order:
        count = i.product_count
        price = count * i.product.price
        total_order_price += price


    user = User.objects.get(id=request.user.id)
    user_profile = profile.objects.get(username_id=request.user.id)
    my_orders = orders.objects.filter(username_id=request.user.id)
    context = {'user':user,'user_profile':user_profile,'cart_count':cart_count,'my_orders':my_orders,'order_count':order_count,'total_order_price':total_order_price}
    return render(request, 'user_myorders.html',context)








def daily_task(request):
    items = product_cart.objects.filter(username=request.user.id)
    cart_count = sum(items.values_list('quantity', flat=True))

    user = User.objects.get(id=request.user.id)
    daily_deals_list = assign_deal.objects.filter(assigns=request.user.id)
    daily_jobs_list = assign_job.objects.filter(assigns=request.user.id)
    # user_products_list = products.objects.filter(username_id=request.user.id)
    user_profile = profile.objects.get(username_id=request.user.id)
    context = {'user':user,'daily_deals_list':daily_deals_list,'daily_jobs_list':daily_jobs_list,'user_profile':user_profile,'cart_count':cart_count}
    return render(request, 'user_dailytask.html',context)


def delete_assaigned_deal(request):
    if request.method == 'POST':
        id_delete = request.POST.get('id_delete')
        assaign_deal_delete = assign_deal.objects.get(id=id_delete).delete()
        messages.info(request,"Assaigned Deal Deleted")
        return redirect('daily_task')
    else:
        messages.info(request,"No Assaigned Deal Deleted")
        return redirect('daily_task')
    


def delete_assaigned_job(request):
    if request.method == 'POST':
        id_delete = request.POST.get('id_delete')
        assaign_job_delete = assign_job.objects.get(id=id_delete).delete()
        messages.info(request,"Assaigned Job Deleted")
        return redirect('daily_task')
    else:
        messages.info(request,"No Assaigned Job Deleted")
        return redirect('daily_task')




def chats(request):
    items = product_cart.objects.filter(username=request.user.id)
    cart_count = sum(items.values_list('quantity', flat=True))

    user = User.objects.get(id=request.user.id)
    notifications_list = notifications.objects.all()
    user_profile = profile.objects.get(username_id=request.user.id)
    context = {'user':user,'notifications_list':notifications_list,'user_profile':user_profile,'cart_count':cart_count}
    return render(request, 'user_chats.html',context)


def feedback(request):
    if request.method == 'POST':
        feedback = request.POST.get('feedback')

        user = profile.objects.get(username_id=request.user.id)
        feedbacks(feedback=feedback,username=user).save()
        messages.info(request,"Feedback Added")
        return redirect('chats')
    else:
        return redirect('chats')






def delete_deal(request):
    if request.method == 'POST':
        id_delete = request.POST.get('id_delete')
        deal_delete = deals.objects.get(id=id_delete).delete()
        deal_delete_attach = deal_attachments.objects.filter(deal_id=id_delete).delete()
        messages.info(request,"Deal Deleted")
        return redirect('myads')
    else:
        messages.info(request,"No Deal Deleted")
        return redirect('myads')
    

def delete_job(request):
    if request.method == 'POST':
        id_delete = request.POST.get('id_delete')
        job_delete = jobs.objects.get(id=id_delete).delete()
        job_delete_attach = job_attachments.objects.filter(job_id=id_delete).delete()
        messages.info(request,"Job Deleted")
        return redirect('myads')
    else:
        messages.info(request,"No Job Deleted")
        return redirect('myads')

def delete_product(request):
    if request.method == 'POST':
        id_delete = request.POST.get('id_delete')
        product_delete = products.objects.get(id=id_delete).delete()
        product_delete_attach = product_attachments.objects.filter(product_id=id_delete).delete()
        messages.info(request,"Product Deleted")
        return redirect('myads')
    else:
        messages.info(request,"No Product Deleted")
        return redirect('myads')






def detail_view_deals(request,id):
    if request.method == 'POST':
        publish = request.POST['publish']
        deal_name = request.POST['deal_name']
        price = request.POST['price']
        category = request.POST.getlist('category')
        # email = request.POST['email']
        # contact = request.POST['contact']
        location = request.POST['location']
        deal_type = request.POST['deal_type']
        brand_name = request.POST['brand_name']
        picture = request.FILES.get('picture')
        attach = request.FILES.getlist('attachments')
        details = request.POST['details']

        user_deals_update = deals.objects.get(id=int(id))
        user_deals_update.publish = publish
        user_deals_update.deal_name = deal_name
        user_deals_update.price = price
        # user_deals_update.email = email
        # user_deals_update.contact = contact
        user_deals_update.location = location
        user_deals_update.deal_type = deal_type
        user_deals_update.brand_name = brand_name
        user_deals_update.picture = picture
        user_deals_update.details = details

        user_deals_update.save()

        user_deals_update.category.clear()
        for i in category:
            user_deals_update.category.add(categorys.objects.get(id=i))

        for i in attach:
            deal_attachments(deal=user_deals_update,attachment=i).save()

        messages.info(request,"Deal Updated")
        return redirect('myads')
    else:
        items = product_cart.objects.filter(username=request.user.id)
        cart_count = sum(items.values_list('quantity', flat=True))

        user = User.objects.get(id=request.user.id)
        user_deals_list =  deals.objects.get(id=id)
        user_deals_attach_list = deal_attachments.objects.filter(deal_id=id)
        user_profile = profile.objects.get(username_id=request.user.id)

        category_details = categorys.objects.filter(is_deleted=False)
        trade = user_deals_list.category.all()
        context = {'user':user,'user_deals_list':user_deals_list,'user_profile':user_profile,'user_deals_attach_list':user_deals_attach_list,'cart_count':cart_count,'category_details':category_details,'trade':trade}
        return render(request,'user_deals_edit.html',context)




def detail_view_jobs(request,id):
    if request.method == 'POST':
        publish = request.POST['publish']
        job_name = request.POST['job_name']
        price = request.POST['price']
        category = request.POST.getlist('category')
        # email = request.POST['email']
        # contact = request.POST['contact']
        location = request.POST['location']
        job_type = request.POST['job_type']
        brand_name = request.POST['brand_name']
        picture = request.FILES.get('picture')
        attach = request.FILES.getlist('attachments')
        details = request.POST['details']

        user_jobs_update = jobs.objects.get(id=int(id))
        user_jobs_update.publish = publish
        user_jobs_update.job_name = job_name
        user_jobs_update.price = price
        # user_jobs_update.email = email
        # user_jobs_update.contact = contact
        user_jobs_update.location = location
        user_jobs_update.job_type = job_type
        user_jobs_update.brand_name = brand_name
        user_jobs_update.picture = picture
        user_jobs_update.details = details

        user_jobs_update.save()

        user_jobs_update.category.clear()
        for i in category:
            user_jobs_update.category.add(categorys.objects.get(id=i))

        for i in attach:
            job_attachments(job=user_jobs_update,attachment=i).save()

        messages.info(request,"Job Updated")
        return redirect('myads')
    else:
        items = product_cart.objects.filter(username=request.user.id)
        cart_count = sum(items.values_list('quantity', flat=True))

        user = User.objects.get(id=request.user.id)
        user_jobs_list =  jobs.objects.get(id=id)
        user_jobs_attach_list = job_attachments.objects.filter(job_id=id)
        user_profile = profile.objects.get(username_id=request.user.id)

        category_details = categorys.objects.filter(is_deleted=False)
        trade = user_jobs_list.category.all()
        context = {'user':user,'user_jobs_list':user_jobs_list,'user_profile':user_profile,'user_jobs_attach_list':user_jobs_attach_list,'cart_count':cart_count,'category_details':category_details,'trade':trade}
        return render(request,'user_jobs_edit.html',context)
        











########

# category = request.POST.getlist('category')

# for i in category:
#     admin_jobs_add.category.add(categorys.objects.get(id=i))


# <div class="form-group">
# <label>Select Job Category:</label>
# <select id="jobcategory" name="category"
# class="" multiple required="">

# {% for i in category_details %}
# <option id="jobcategory_value" value="{{i.id}}">{{i.name}}</option>
# {% endfor %}
# </select>
# </div>


# category_details = categorys.objects.filter(is_deleted=False)




##################
# category = request.POST.getlist('category')


# admin_deals_list.category.clear()
# for i in category:
#     admin_deals_list.category.add(categorys.objects.get(id=i))



# <div class="form-group">
# <label>Select Job Category:</label>
# <select name="category" class="form-control" multiple="">
# {% for i in category_details %}
#     <option {% for j in trade %} {% if i.id == j.id %} selected {% endif %} {% endfor %} value="{{ i.id }}">{{ i.name }}</option>
# {% endfor %}
# </select>
# </div>



# category_details = categorys.objects.filter(is_deleted=False)
# trade = admin_deals_list.category.all()



def detail_view_products(request,id):
    if request.method == 'POST':
        publish = request.POST['publish']
        product_name = request.POST['product_name']
        price = request.POST['price']
        stock = request.POST['stock']
        category = request.POST.getlist('category')
        # email = request.POST['email']
        # contact = request.POST['contact']
        location = request.POST['location']
        product_type = request.POST['product_type']
        brand_name = request.POST['brand_name']
        picture = request.FILES.get('picture')
        attach = request.FILES.getlist('attachments')
        details = request.POST['details']

        user_products_update = products.objects.get(id=int(id))
        user_products_update.publish = publish
        user_products_update.product_name = product_name
        user_products_update.price = price
        user_products_update.stock = stock
        # user_products_update.email = email
        # user_products_update.contact = contact
        user_products_update.location = location
        user_products_update.product_type = product_type
        user_products_update.brand_name = brand_name
        user_products_update.picture = picture
        user_products_update.details = details

        user_products_update.save()


        user_products_update.category.clear()
        for i in category:
            user_products_update.category.add(categorys.objects.get(id=i))

        for i in attach:
            product_attachments(product=user_products_update,attachment=i).save()

        messages.info(request,"Product Updated")
        return redirect('myads')
    else:
        items = product_cart.objects.filter(username=request.user.id)
        cart_count = sum(items.values_list('quantity', flat=True))

        user = User.objects.get(id=request.user.id)
        user_products_list =  products.objects.get(id=id)
        user_products_attach_list = product_attachments.objects.filter(product_id=id)
        user_profile = profile.objects.get(username_id=request.user.id)

        category_details = categorys.objects.filter(is_deleted=False)
        trade = user_products_list.category.all()
        context = {'user':user,'user_products_list':user_products_list,'user_products_attach_list':user_products_attach_list,'user_profile':user_profile,'cart_count':cart_count,'category_details':category_details,'trade':trade}
        return render(request,'user_products_edit.html',context)





def user_update_product_offer(request,id):
    if request.method == 'POST':
        offer = request.POST['offer']

        user_products_list = products.objects.get(id=int(id))
        user_products_list.offer = offer

        oldprice = user_products_list.oldprice
        offer = float(offer)
        percentage = oldprice * offer / 100
        price = oldprice-percentage
        
        user_products_list.price = price
        user_products_list.save()

        messages.info(request,"Offer added")
        return redirect('myads')
    else:
        messages.info(request,"No offer added")
        return redirect('myads')









def delete_deal_attachments(request):
    if request.method == 'POST':
        attach_delete = request.POST.get('attach_delete')

        deal_attach_delete = deal_attachments.objects.filter(deal_id=attach_delete).delete()
        messages.info(request,"Deal attachments Deleted")
        return redirect('deal')
    else:
        messages.info(request,"No Deal attachments Deleted")
        return redirect('deal')


def delete_job_attachments(request):
    if request.method == 'POST':
        attach_delete = request.POST.get('attach_delete')

        job_attach_delete = job_attachments.objects.filter(job_id=attach_delete).delete()
        messages.info(request,"Job attachments Deleted")
        return redirect('job')
    else:
        messages.info(request,"No Job attachments Deleted")
        return redirect('job')

def delete_product_attachments(request):
    if request.method == 'POST':
        attach_delete = request.POST.get('attach_delete')

        product_attach_delete = product_attachments.objects.filter(product_id=attach_delete).delete()
        messages.info(request,"Product attachments Deleted")
        return redirect('product')
    else:
        messages.info(request,"No Product attachments Deleted")
        return redirect('product')










def wishlist(request):
    items = product_cart.objects.filter(username=request.user.id)
    cart_count = sum(items.values_list('quantity', flat=True))

    user = User.objects.get(id=request.user.id)
    user_profile = profile.objects.get(username_id=request.user.id)
    user_deal_wishlist = deal_wish.objects.filter(username_id=request.user.id)
    user_job_wishlist = job_wish.objects.filter(username_id=request.user.id)
    user_product_wishlist = product_wish.objects.filter(username_id=request.user.id)
    context = {'user':user,'user_profile':user_profile,'user_deal_wishlist':user_deal_wishlist,'user_job_wishlist':user_job_wishlist,'user_product_wishlist':user_product_wishlist,'cart_count':cart_count}
    return render(request,'user_wishlist.html',context)


def cart(request):
    user = User.objects.get(id=request.user.id)

    items = product_cart.objects.filter(username=request.user.id)
    cart_count = sum(items.values_list('quantity', flat=True))
    # count = items.quantity
    # price = count * items.product.price

    price = 0
    total_price = 0
    for product in items:
        count = product.quantity
        price = count * product.product.price
        total_price += price
    #   print("--------------------------------------------------------------------------------------",product.product.price)
    #   print("--------------------------------------------------------------------------------------",price)
    # print("===========================================================================================",total_price)



    user_profile = profile.objects.get(username_id=request.user.id)
    user_product_cart = product_cart.objects.filter(username_id=request.user.id)


    context = {'user':user,'user_profile':user_profile,'user_product_cart':user_product_cart,'cart_count':cart_count,'total_price':total_price}
    return render(request,'user_cart.html',context)



def checkout(request):
    if request.method == 'POST':
        address_id = request.POST['address_id']

        user = User.objects.get(id=request.user.id)
        user_address = address.objects.get(id=address_id)
        user_profile = profile.objects.get(username_id=request.user.id)

        if delivery_address.objects.filter(username_id = user,profile_id = user_profile).exists():
            user_delivery_address = delivery_address.objects.get(username_id=request.user.id)
            user_delivery_address.address = user_address
            user_delivery_address.username = user
            user_delivery_address.profile = user_profile
            user_delivery_address.first_name = user_address.first_name
            user_delivery_address.last_name = user_address.last_name
            user_delivery_address.country = user_address.country
            user_delivery_address.state = user_address.state
            user_delivery_address.district = user_address.district
            user_delivery_address.postalcode = user_address.postalcode
            user_delivery_address.phone = user_address.phone
            user_delivery_address.alternative_phone = user_address.alternative_phone
            user_delivery_address.address_line_1 = user_address.address_line_1
            user_delivery_address.address_line_2 = user_address.address_line_2
            user_delivery_address.save()
        else:
            user_delivery_address = delivery_address.objects.get_or_create(address=user_address,username = user,profile = user_profile,first_name = user_address.first_name,last_name = user_address.last_name,country = user_address.country,state = user_address.state,district = user_address.district,postalcode = user_address.postalcode,phone = user_address.phone,alternative_phone = user_address.alternative_phone,address_line_1 = user_address.address_line_1,address_line_2 = user_address.address_line_2)


        return redirect('payment')

    else:
        user = User.objects.get(id=request.user.id)

        items = product_cart.objects.filter(username=request.user.id)
        cart_count = sum(items.values_list('quantity', flat=True))
        # count = items.quantity
        # price = count * items.product.price

        price = 0
        total_price = 0
        for product in items:
            count = product.quantity
            price = count * product.product.price
            total_price += price
        #   print("--------------------------------------------------------------------------------------",product.product.price)
        #   print("--------------------------------------------------------------------------------------",price)
        # print("===========================================================================================",total_price)



        user_profile = profile.objects.get(username_id=request.user.id)
        user_product_cart = product_cart.objects.filter(username_id=request.user.id)
        user_address = address.objects.filter(username_id=request.user.id)

        context = {'user':user,'user_profile':user_profile,'user_product_cart':user_product_cart,'cart_count':cart_count,'total_price':total_price,'user_address':user_address}
        return render(request,'user_checkout.html',context)




def about_us(request):
    if request.method == 'POST':
        pass

    else:
        user = User.objects.get(id=request.user.id)

        items = product_cart.objects.filter(username=request.user.id)
        cart_count = sum(items.values_list('quantity', flat=True))

        user_profile = profile.objects.get(username_id=request.user.id)
        context = {'user':user,'user_profile':user_profile,'cart_count':cart_count}
        return render(request,'user_about_us.html',context)



def add_address2(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        country = request.POST['country']
        state = request.POST['state']
        district = request.POST['district']
        postalcode = request.POST['postalcode']
        phone = request.POST['phone']
        alternative_phone = request.POST['alternative_phone']
        address_line_1 = request.POST['address_line_1']
        address_line_2 = request.POST['address_line_2']


        user = User.objects.get(id=request.user.id)
        user_profile = profile.objects.get(username_id=request.user.id)

        user_address = address(username=user,profile=user_profile,first_name=first_name,last_name=last_name,country=country,state=state,district=district,postalcode=postalcode,phone=phone,alternative_phone=alternative_phone,address_line_1=address_line_1,address_line_2=address_line_2)
        user_address.save()

        user_address_id = address.objects.get(id=user_address.id)

        if delivery_address.objects.filter(username_id = user,profile_id = user_profile).exists():
            user_delivery_address = delivery_address.objects.get(username_id=request.user.id)
            user_delivery_address.address = user_address_id
            user_delivery_address.username = user
            user_delivery_address.profile = user_profile
            user_delivery_address.first_name = user_address_id.first_name
            user_delivery_address.last_name = user_address_id.last_name
            user_delivery_address.country = user_address_id.country
            user_delivery_address.state = user_address_id.state
            user_delivery_address.district = user_address_id.district
            user_delivery_address.postalcode = user_address_id.postalcode
            user_delivery_address.phone = user_address_id.phone
            user_delivery_address.alternative_phone = user_address_id.alternative_phone
            user_delivery_address.address_line_1 = user_address_id.address_line_1
            user_delivery_address.address_line_2 = user_address_id.address_line_2
            user_delivery_address.save()

            messages.info(request,'Address Added')
            return redirect('payment')

        else:
            user_delivery_address = delivery_address.objects.get_or_create(address=user_address_id,username = user,profile = user_profile,first_name = user_address_id.first_name,last_name = user_address_id.last_name,country = user_address_id.country,state = user_address_id.state,district = user_address_id.district,postalcode = user_address_id.postalcode,phone = user_address_id.phone,alternative_phone = user_address_id.alternative_phone,address_line_1 = user_address_id.address_line_1,address_line_2 = user_address_id.address_line_2)
            messages.info(request,'Address Added')
            return redirect('payment')


    else:
        return redirect('checkout')



def payment(request):

    user = User.objects.get(id=request.user.id)

    items = product_cart.objects.filter(username=request.user.id)
    cart_count = sum(items.values_list('quantity', flat=True))
    # count = items.quantity
    # price = count * items.product.price

    price = 0
    total_price = 0
    for product in items:
        count = product.quantity
        price = count * product.product.price
        total_price += price
    #   print("--------------------------------------------------------------------------------------",product.product.price)
    #   print("--------------------------------------------------------------------------------------",price)
    # print("===========================================================================================",total_price)



    user_profile = profile.objects.get(username_id=request.user.id)
    user_product_cart = product_cart.objects.filter(username_id=request.user.id)
    user_delivery_address = delivery_address.objects.get(username_id=request.user.id)

    context = {'user':user,'user_profile':user_profile,'user_product_cart':user_product_cart,'cart_count':cart_count,'total_price':total_price,'user_delivery_address':user_delivery_address}
    return render(request,'user_payment.html',context)



# def paymentComplete(request):
#   body = json.loads(request.body)
#   print('BODY:',body)
#   return JsonResponse('Payment completed!', safe=False)

def ordercomplete(request):
    user = User.objects.get(id=request.user.id)
    user_profile = profile.objects.get(username_id=request.user.id)

    items = product_cart.objects.filter(username=request.user.id)
    cart_count = sum(items.values_list('quantity', flat=True))

    user_delivery_address = delivery_address.objects.get(username_id=request.user.id)
    print("-----------------------------------------------------------------------------------------------------------",user_delivery_address,user_delivery_address.address,user_delivery_address.address.first_name)

    price = 0
    total_price = 0
    for product in items:
        count = product.quantity
        price = count * product.product.price
        total_price += price


    for i in items:
        order_add = orders(username=user,profile=user_profile,product=i.product,product_count=i.quantity,cart_count=cart_count,amount=total_price,product_name=i.product.product_name,price=i.product.price,email=i.product.email,contact=i.product.contact,brand_name=i.product.brand_name,picture=i.product.picture,address=user_delivery_address,first_name=user_delivery_address.address.first_name,last_name=user_delivery_address.address.last_name,country=user_delivery_address.address.country,state=user_delivery_address.address.state,district=user_delivery_address.address.district,postalcode=user_delivery_address.address.postalcode,phone=user_delivery_address.address.phone,alternative_phone=user_delivery_address.address.alternative_phone,address_line_1=user_delivery_address.address.address_line_1,address_line_2=user_delivery_address.address.address_line_2)
        order_add.save()

    profile.objects.filter(username_id=request.user.id).update(coins=F('coins')+10)



    cart_delete = product_cart.objects.filter(username_id=request.user.id)
    cart_delete.delete()
    
    messages.info(request,'Ordered , Cart is Empty') 
    return redirect('user_home')


def ordercomplete_wallet(request):
    if request.method == 'POST':
        user = User.objects.get(id=request.user.id)
        user_profile = profile.objects.get(username_id=request.user.id)

        items = product_cart.objects.filter(username=request.user.id)
        cart_count = sum(items.values_list('quantity', flat=True))

        user_delivery_address = delivery_address.objects.get(username_id=request.user.id)
        print("-----------------------------------------------------------------------------------------------------------",user_delivery_address,user_delivery_address.address,user_delivery_address.address.first_name)

        price = 0
        total_price = 0
        for product in items:
            count = product.quantity
            price = count * product.product.price
            total_price += price

        if user_profile.wallet >= total_price:
            for i in items:
                order_add = orders(username=user,profile=user_profile,product=i.product,product_count=i.quantity,cart_count=cart_count,amount=total_price,product_name=i.product.product_name,price=i.product.price,email=i.product.email,contact=i.product.contact,brand_name=i.product.brand_name,picture=i.product.picture,address=user_delivery_address,first_name=user_delivery_address.address.first_name,last_name=user_delivery_address.address.last_name,country=user_delivery_address.address.country,state=user_delivery_address.address.state,district=user_delivery_address.address.district,postalcode=user_delivery_address.address.postalcode,phone=user_delivery_address.address.phone,alternative_phone=user_delivery_address.address.alternative_phone,address_line_1=user_delivery_address.address.address_line_1,address_line_2=user_delivery_address.address.address_line_2)
                order_add.save()

            profile.objects.filter(username_id=request.user.id).update(wallet=F('wallet')-total_price,coins=F('coins')+10)
            cart_delete = product_cart.objects.filter(username_id=request.user.id)
            cart_delete.delete()
            
            messages.info(request,'Ordered , Cart is Empty') 
            return redirect('user_home')
        else:
            messages.info(request,'No have enough money in wallet,Use online payment') 
            return redirect('user_home')
    else:
        return redirect('payment')








def delete_wish_deal(request):
    if request.method == 'POST':
        id_delete = request.POST.get('id_delete')
        deal_wish_delete = deal_wish.objects.get(id=id_delete).delete()
        messages.info(request,"Deal Removed from Wishlist")
        return redirect('wishlist')
    else:
        messages.info(request,"No Deal Removed")
        return redirect('wishlist')
    

def delete_wish_job(request):
    if request.method == 'POST':
        id_delete = request.POST.get('id_delete')
        job_wish_delete = job_wish.objects.get(id=id_delete).delete()
        messages.info(request,"Job Removed from Wishlist")
        return redirect('wishlist')
    else:
        messages.info(request,"No Job Removed")
        return redirect('wishlist')
    

def delete_wish_product(request):
    if request.method == 'POST':
        id_delete = request.POST.get('id_delete')
        product_wish_delete = product_wish.objects.get(id=id_delete).delete()
        messages.info(request,"Product Removed from Wishlist")
        return redirect('wishlist')
    else:
        messages.info(request,"No Product Removed")
        return redirect('wishlist')
    




def delete_cart(request):
    if request.method == 'POST':
        id_delete = request.POST.get('id_delete')
        id_product = request.POST.get('id_product')
        product_carts = product_cart.objects.get(id=id_delete)
        product_carts_quantity = product_carts.quantity
        product_carts.delete()
        products.objects.filter(id=id_product).update(stock=F('stock')+product_carts_quantity)

        messages.info(request,"Product Removed from Cart")
        return redirect('cart')
    else:
        messages.info(request,"No Product Removed")
        return redirect('cart')
    







def deal_to_wish(request):
    if request.method == 'POST':
        id_deal = request.POST.get('id_deal')
        dealtowish = deals.objects.get(id=id_deal)
        user = User.objects.get(id=request.user.id)
        deal_wish(deal=dealtowish,username=user).save()
        messages.info(request,"Deal added to Wishlist")
        return redirect('deal')
    else:
        messages.info(request,"Not added to Wishlist")
        return redirect('deal')



def deal_to_task(request):
    if request.method == 'POST':
        id_deal = request.POST.get('id_deal')
        dealtotask = deals.objects.get(id=id_deal)
        user = User.objects.get(id=request.user.id)
        assign_deal(deal=dealtotask,username=user,assigns=user.id).save()
        messages.info(request,"Deal added to DailyTask")
        return redirect('deal')
    else:
        messages.info(request,"Not added to DailyTask")
        return redirect('deal')








def job_to_wish(request):
    if request.method == 'POST':
        id_job = request.POST.get('id_job')
        jobtowish = jobs.objects.get(id=id_job)
        user = User.objects.get(id=request.user.id)
        job_wish(job=jobtowish,username=user).save()
        messages.info(request,"Job added to Wishlist")
        return redirect('job')
    else:
        messages.info(request,"Not added to Wishlist")
        return redirect('job')


def job_to_task(request):
    if request.method == 'POST':
        id_job = request.POST.get('id_job')
        jobtotask = jobs.objects.get(id=id_job)
        user = User.objects.get(id=request.user.id)
        assign_job(job=jobtotask,username=user,assigns=user.id).save()
        messages.info(request,"Job added to DailyTask")
        return redirect('job')
    else:
        messages.info(request,"Not added to DailyTask")
        return redirect('job')







def product_to_wish(request):
    if request.method == 'POST':
        id_product = request.POST.get('id_product')
        producttowish = products.objects.get(id=id_product)
        user = User.objects.get(id=request.user.id)
        product_wish(product=producttowish,username=user).save()
        messages.info(request,"Product added to Wishlist")
        return redirect('product')
    else:
        messages.info(request,"Not added to Wishlist")
        return redirect('product')


def product_to_cart(request):
    if request.method == 'POST':
        id_product = request.POST.get('id_product')
        producttocart = products.objects.get(id=id_product)
        user = User.objects.get(id=request.user.id)
        print("------------------------------------------------------------------------------------------",producttocart.stock)

        if producttocart.stock >= 1:
            if product_cart.objects.filter(product=producttocart,username=user).exists():
                product_cart.objects.filter(product=producttocart,username=user).update(quantity=F('quantity')+1)
                products.objects.filter(id=id_product).update(stock=F('stock')-1)
                messages.info(request,"Product added to Cart")
                return redirect('product')
            else:
                product_cart(product=producttocart,username=user).save()
                products.objects.filter(id=id_product).update(stock=F('stock')-1)
                messages.info(request,"Product added to Cart")
                return redirect('product')

        else:
            messages.info(request,"No Stock")
            return redirect('product')
    else:
        messages.info(request,"Not added to Cart")
        return redirect('product')





def user_logout(request):
    auth.logout(request)
    return redirect('/home')
