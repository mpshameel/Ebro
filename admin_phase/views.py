from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import *


from datetime import timedelta


# Create your views here.


def admin_home(request):
	if request.user.is_authenticated:
		admin_profile = profile.objects.get(username_id=request.user.id)
		context = {'admin_profile':admin_profile}
		if request.user.is_superuser:
			return render(request, 'admin_home.html',context)
		else:
			messages.info(request,'You are not approved as admin')
			return redirect('admin_login')
	else:
		messages.info(request,'User not Logged in')
		return redirect('admin_login')


def admin_login(request):
	if request.method == 'POST':
		name = request.POST['name']
		password = request.POST['password']

		user = auth.authenticate(username=name,password=password)
		if user is not None:
			auth.login(request,user)
			messages.info(request,'User Logged in')
			return redirect('/')
			

		else:
			messages.info(request,'Invalid credentials')
			return redirect('admin_login')

	else:
		return render(request, 'admin_login.html')



def admin_signup(request):
	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		phone = request.POST['phone']
		password1 = request.POST['password1']
		password2 = request.POST['password2']



		if password1 == password2:
			if User.objects.filter(email=email).exists():
				messages.info(request,"Email already exist")
				return redirect('admin_login')
			else:
				user=User.objects.create_superuser(first_name=first_name,last_name=last_name,username=email,email=email,password=password1)
				user.save()

				pr = profile(username=user,phone=phone,usertype="admin").save()

				messages.info(request,"Admin Registered Successfully")
				return redirect('admin_login')

		else:
			messages.info(request,'Password not matching')
			return redirect('/')

	else:
		return redirect('admin_login')




def admin_profile(request):
	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		# email = request.POST['email']
		phone = request.POST['phone']
		alternative_phone = request.POST['alternative_phone']
		dob = request.POST['dob']
		adhar_id = request.POST['adhar_id']
		qualification = request.POST['qualification']
		hobbies = request.POST['hobbies']
		summary = request.POST['summary']

		user = User.objects.get(id=request.user.id)
		user.first_name = first_name
		user.last_name= last_name
		# user.email= email
		# user.username = email
		user.save()
		
		admin_update_profile = profile.objects.get(username_id=request.user.id)
		admin_update_profile.phone = phone
		admin_update_profile.alternative_phone = alternative_phone
		admin_update_profile.dob = dob
		admin_update_profile.adhar_id = adhar_id
		admin_update_profile.qualification = qualification
		admin_update_profile.hobbies = hobbies
		admin_update_profile.summary = summary
		admin_update_profile.save()

		messages.info(request,'Profile Updated')
		return redirect('admin_profile')

	else:
		admin_profile = profile.objects.get(username_id=request.user.id)
		context = {'admin_profile':admin_profile}
		return render(request, 'admin_profile.html',context)

def update_admin_profile_pic(request):
	if request.method == 'POST':
		image = request.FILES.get('img')
		
		profile_pic = profile.objects.get(username_id=request.user.id)
		profile_pic.image = image
		profile_pic.save()

		messages.info(request,'Profile-Pic Updated')
		return redirect('admin_profile')
	else:
		messages.info(request,'Profile-Pic Not Updated')
		return redirect('admin_profile')



def admin_deals(request):
	if request.method == 'POST':
		publish = request.POST['publish']
		deal_name = request.POST['deal_name']
		price = request.POST['price']
		category = request.POST['category']
		email = request.POST['email']
		contact = request.POST['contact']
		location = request.POST['location']
		deal_type = request.POST['deal_type']
		brand_name = request.POST['brand_name']
		picture = request.FILES.get('picture')
		attach = request.FILES.getlist('attachments')
		details = request.POST['details']


		user = User.objects.get(id=request.user.id)
		
		admin_deals_add = deals(username=user,publish=publish,deal_name=deal_name,price=price,category=category,email=email,contact=contact,location=location,deal_type=deal_type,brand_name=brand_name,picture=picture,details=details)
		admin_deals_add.save()

		ids = admin_deals_add.id

		deal_id = deals.objects.get(id=ids)
		print("-------------------------------------------------------------",attach)
		for i in attach:
			print("-------------------------------------------------------------",i,deal_id)
			deal_attachments(deal=deal_id,attachment=i).save()
			
		messages.info(request,'Deal Added')
		return redirect('admin_deals')

	elif 'deal_name' in request.GET:
		deal_name = request.GET['deal_name']
		publish = request.GET['publish']
		deal_type = request.GET['deal_type']
		brand_name = request.GET['brand_name']
		location = request.GET['location']
		admin_deals_list = deals.objects.filter(deal_name__contains=deal_name,publish__contains=publish,deal_type__contains=deal_type,brand_name__contains=brand_name,location__contains=location)

	else:
		admin_deals_list = deals.objects.all()
	admin_profile = profile.objects.get(username_id=request.user.id)
	user = User.objects.get(id=request.user.id)
	context = {'user':user,'admin_deals_list':admin_deals_list,'admin_profile':admin_profile}
	return render(request, 'admin_deals.html',context)


def delete_admin_deals(request):
	if request.method == 'POST':
		id_delete = request.POST.get('id_delete')
		deal_delete = deals.objects.get(id=id_delete).delete()
		deal_delete_attach = deal_attachments.objects.filter(deal_id=id_delete).delete()
		messages.info(request,"Deal Deleted")
		return redirect('admin_deals')
	else:
		messages.info(request,"No Deal Deleted")
		return redirect('admin_deals')
	

def detail_view_admin_deals(request,id):
	if request.method == 'POST':
		publish = request.POST['publish']
		deal_name = request.POST['deal_name']
		price = request.POST['price']
		category = request.POST['category']
		email = request.POST['email']
		contact = request.POST['contact']
		location = request.POST['location']
		deal_type = request.POST['deal_type']
		brand_name = request.POST['brand_name']
		picture = request.FILES.get('picture')
		attach = request.FILES.getlist('attachments')
		details = request.POST['details']

		admin_deals_list = deals.objects.get(id=int(id))
		admin_deals_list.publish = publish
		admin_deals_list.deal_name = deal_name
		admin_deals_list.price = price
		admin_deals_list.category = category
		admin_deals_list.email = email
		admin_deals_list.contact = contact
		admin_deals_list.location = location
		admin_deals_list.deal_type = deal_type
		admin_deals_list.brand_name = brand_name
		admin_deals_list.picture = picture
		admin_deals_list.details = details

		admin_deals_list.save()

		for i in attach:
			deal_attachments(deal=admin_deals_list,attachment=i).save()

		messages.info(request,"Deal Updated")
		return redirect('admin_deals')
	else:
		admin_profile = profile.objects.get(username_id=request.user.id)
		admin_deals_list =  deals.objects.get(id=id)
		admin_deals_attach_list = deal_attachments.objects.filter(deal_id=id)
		context = {'admin_deals_list':admin_deals_list,'admin_deals_attach_list':admin_deals_attach_list,'admin_profile':admin_profile}
		return render(request,'admin_deals_edit.html',context)



def delete_deal_attach(request):
	if request.method == 'POST':
		attach_delete = request.POST.get('attach_delete')

		deal_attach_delete = deal_attachments.objects.filter(deal_id=attach_delete).delete()
		messages.info(request,"Deal attachments Deleted")
		return redirect('admin_deals')
	else:
		messages.info(request,"No Deal attachments Deleted")
		return redirect('admin_deals')
	





def assign_admin_deals(request,id):
	if request.method == 'POST':
		assigns = request.POST.getlist('assigns')

		user = User.objects.get(id=request.user.id)

		for i in assigns:
			assign_deal(deal=deals.objects.get(id=int(id)),username=user,assigns=i).save()

		messages.info(request,"Deal Assigned")
		return redirect('admin_deals')

	elif 'user_search' in request.GET:
		user_search = request.GET['user_search']
		profile_list =  profile.objects.filter(username__is_superuser=False,username__username__contains=user_search)
	else:
		profile_list =  profile.objects.filter(username__is_superuser=False)
	admin_profile = profile.objects.get(username_id=request.user.id)
	admin_deals_list =  deals.objects.get(id=id)
	users = User.objects.filter(is_superuser=False)
	context = {'admin_deals_list':admin_deals_list,'users':users,'profile_list':profile_list,'admin_profile':admin_profile}
	return render(request,'assign_admin_deals.html',context)





def admin_jobs(request):
	if request.method == 'POST':
		publish = request.POST['publish']
		job_name = request.POST['job_name']
		price = request.POST['price']
		category = request.POST['category']
		email = request.POST['email']
		contact = request.POST['contact']
		location = request.POST['location']
		job_type = request.POST['job_type']
		brand_name = request.POST['brand_name']
		picture = request.FILES.get('picture')
		attach = request.FILES.getlist('attachments')
		details = request.POST['details']


		user = User.objects.get(id=request.user.id)
		
		admin_jobs_add = jobs(username=user,publish=publish,job_name=job_name,price=price,category=category,email=email,contact=contact,location=location,job_type=job_type,brand_name=brand_name,picture=picture,details=details)
		admin_jobs_add.save()

		ids = admin_jobs_add.id

		job_id = jobs.objects.get(id=ids)
		print("-------------------------------------------------------------",attach)
		for i in attach:
			print("-------------------------------------------------------------",i,job_id)
			job_attachments(job=job_id,attachment=i).save()
		
		return redirect('admin_jobs')

	elif 'job_name' in request.GET:
		job_name = request.GET['job_name']
		publish = request.GET['publish']
		job_type = request.GET['job_type']
		brand_name = request.GET['brand_name']
		location = request.GET['location']
		admin_jobs_list = jobs.objects.filter(job_name__contains=job_name,publish__contains=publish,job_type__contains=job_type,brand_name__contains=brand_name,location__contains=location)

	else:
		admin_jobs_list = jobs.objects.all()
	admin_profile = profile.objects.get(username_id=request.user.id)
	user = User.objects.get(id=request.user.id)	
	context = {'user':user,'admin_jobs_list':admin_jobs_list,'admin_profile':admin_profile}
	return render(request, 'admin_jobs.html',context)



def delete_admin_jobs(request):
	if request.method == 'POST':
		id_delete = request.POST.get('id_delete')
		job_delete = jobs.objects.get(id=id_delete).delete()
		job_delete_attach = job_attachments.objects.filter(job_id=id_delete).delete()
		messages.info(request,"Job Deleted")
		return redirect('admin_jobs')
	else:
		messages.info(request,"No Job Deleted")
		return redirect('admin_jobs')
	



def detail_view_admin_jobs(request,id):
	if request.method == 'POST':
		publish = request.POST['publish']
		job_name = request.POST['job_name']
		price = request.POST['price']
		category = request.POST['category']
		email = request.POST['email']
		contact = request.POST['contact']
		location = request.POST['location']
		job_type = request.POST['job_type']
		brand_name = request.POST['brand_name']
		picture = request.FILES.get('picture')
		attach = request.FILES.getlist('attachments')
		details = request.POST['details']

		admin_jobs_list = jobs.objects.get(id=int(id))
		admin_jobs_list.publish = publish
		admin_jobs_list.job_name = job_name
		admin_jobs_list.price = price
		admin_jobs_list.category = category
		admin_jobs_list.email = email
		admin_jobs_list.contact = contact
		admin_jobs_list.location = location
		admin_jobs_list.job_type = job_type
		admin_jobs_list.brand_name = brand_name
		admin_jobs_list.picture = picture
		admin_jobs_list.details = details

		admin_jobs_list.save()

		for i in attach:
			job_attachments(job=admin_jobs_list,attachment=i).save()

		messages.info(request,"Job Updated")
		return redirect('admin_jobs')
	else:
		admin_profile = profile.objects.get(username_id=request.user.id)
		admin_jobs_list =  jobs.objects.get(id=id)
		admin_jobs_attach_list = job_attachments.objects.filter(job_id=id)
		context = {'admin_jobs_list':admin_jobs_list,'admin_jobs_attach_list':admin_jobs_attach_list,'admin_profile':admin_profile}
		return render(request,'admin_jobs_edit.html',context)



def delete_job_attach(request):
	if request.method == 'POST':
		attach_delete = request.POST.get('attach_delete')

		job__attach_delete = job_attachments.objects.filter(job_id=attach_delete).delete()
		messages.info(request,"Job attachments Deleted")
		return redirect('admin_jobs')
	else:
		messages.info(request,"No Job attachments Deleted")
		return redirect('admin_jobs')
	


def assign_admin_jobs(request,id):
	if request.method == 'POST':
		assigns = request.POST.getlist('assigns')

		user = User.objects.get(id=request.user.id)

		for i in assigns:
			assign_job(job=jobs.objects.get(id=int(id)),username=user,assigns=i).save()

		messages.info(request,"Job Assigned")
		return redirect('admin_jobs')

	elif 'user_search' in request.GET:
		user_search = request.GET['user_search']
		profile_list =  profile.objects.filter(username__is_superuser=False,username__username__contains=user_search)
	else:
		profile_list =  profile.objects.filter(username__is_superuser=False)
	admin_profile = profile.objects.get(username_id=request.user.id)
	admin_jobs_list =  jobs.objects.get(id=id)
	users = User.objects.all()
	context = {'admin_jobs_list':admin_jobs_list,'users':users,'profile_list':profile_list,'admin_profile':admin_profile}
	return render(request,'assign_admin_jobs.html',context)










def admin_products(request):
	if request.method == 'POST':
		publish = request.POST['publish']
		product_name = request.POST['product_name']
		price = request.POST['price']
		category = request.POST['category']
		email = request.POST['email']
		contact = request.POST['contact']
		location = request.POST['location']
		product_type = request.POST['product_type']
		brand_name = request.POST['brand_name']
		picture = request.FILES.get('picture')
		attach = request.FILES.getlist('attachments')
		details = request.POST['details']


		user = User.objects.get(id=request.user.id)
		
		admin_products_add = products(username=user,publish=publish,product_name=product_name,price=price,category=category,email=email,contact=contact,location=location,product_type=product_type,brand_name=brand_name,picture=picture,details=details)
		admin_products_add.save()

		ids = admin_products_add.id

		product_id = products.objects.get(id=ids)
		print("-------------------------------------------------------------",attach)
		for i in attach:
			print("-------------------------------------------------------------",i)
			product_attachments(product=product_id,attachment=i).save()
		
		return redirect('admin_products')

	elif 'product_name' in request.GET:
		product_name = request.GET['product_name']
		publish = request.GET['publish']
		product_type = request.GET['product_type']
		brand_name = request.GET['brand_name']
		location = request.GET['location']
		admin_products_list = products.objects.filter(product_name__contains=product_name,publish__contains=publish,product_type__contains=product_type,brand_name__contains=brand_name,location__contains=location)

	else:
		admin_products_list = products.objects.all()
	admin_profile = profile.objects.get(username_id=request.user.id)
	user = User.objects.get(id=request.user.id)
	context = {'user':user,'admin_products_list':admin_products_list,'admin_profile':admin_profile}
	return render(request, 'admin_products.html',context)



def delete_admin_products(request):
	if request.method == 'POST':
		id_delete = request.POST.get('id_delete')
		product_delete = products.objects.get(id=id_delete).delete()
		product_delete_attach = product_attachments.objects.filter(product_id=id_delete).delete()
		messages.info(request,"Product Deleted")
		return redirect('admin_products')
	else:
		messages.info(request,"No Products Deleted")
		return redirect('admin_products')



def detail_view_admin_products(request,id):
	if request.method == 'POST':
		publish = request.POST['publish']
		product_name = request.POST['product_name']
		price = request.POST['price']
		category = request.POST['category']
		email = request.POST['email']
		contact = request.POST['contact']
		location = request.POST['location']
		product_type = request.POST['product_type']
		brand_name = request.POST['brand_name']
		picture = request.FILES.get('picture')
		attach = request.FILES.getlist('attachments')
		details = request.POST['details']

		admin_products_list = products.objects.get(id=int(id))
		admin_products_list.publish = publish
		admin_products_list.product_name = product_name
		admin_products_list.price = price
		admin_products_list.category = category
		admin_products_list.email = email
		admin_products_list.contact = contact
		admin_products_list.location = location
		admin_products_list.product_type = product_type
		admin_products_list.brand_name = brand_name
		admin_products_list.picture = picture
		admin_products_list.details = details

		admin_products_list.save()

		for i in attach:
			product_attachments(product=admin_products_list,attachment=i).save()

		messages.info(request,"Product Updated")
		return redirect('admin_products')
	else:
		admin_profile = profile.objects.get(username_id=request.user.id)
		admin_products_list =  products.objects.get(id=id)
		admin_products_attach_list = product_attachments.objects.filter(product_id=id)
		context = {'admin_products_list':admin_products_list,'admin_products_attach_list':admin_products_attach_list,'admin_profile':admin_profile}
		return render(request,'admin_products_edit.html',context)



def delete_product_attach(request):
	if request.method == 'POST':
		attach_delete = request.POST.get('attach_delete')

		product_attach_delete = product_attachments.objects.filter(product_id=attach_delete).delete()
		messages.info(request,"Product attachments Deleted")
		return redirect('admin_products')
	else:
		messages.info(request,"No Product attachments Deleted")
		return redirect('admin_products')
	





def admin_myads(request):
	user = User.objects.get(id=request.user.id)
	admin_deals_list = deals.objects.filter(username_id=request.user.id)
	admin_jobs_list = jobs.objects.filter(username_id=request.user.id)
	admin_products_list = products.objects.filter(username_id=request.user.id)
	admin_profile = profile.objects.get(username_id=request.user.id)
	context = {'user':user,'admin_deals_list':admin_deals_list,'admin_jobs_list':admin_jobs_list,'admin_products_list':admin_products_list,'admin_profile':admin_profile}
	return render(request, 'admin_myads.html',context)





def admin_userdata(request):
	if 'search' in request.GET:
		searched = request.GET['search']
		user_type = request.GET['user_type']
		location = request.GET['location']
		profile_list = profile.objects.filter(username__first_name__contains=searched,usertype__contains=user_type,location__contains=location)

	else:
		profile_list = profile.objects.all()
	users = User.objects.all()

	total_admins =  User.objects.filter(is_superuser=True).count()
	total_users =  User.objects.filter(is_superuser=False).count()
	total_registrations = total_admins + total_users

	online_admins = User.objects.all().count()

	# user_activity_objects = OnlineUserActivity.get_user_activities()
	# number_of_active_users = user_activity_objects.count()

	
	public_admin_deals = deals.objects.filter(publish="public",username__is_superuser=True).count()
	private_admin_deals = deals.objects.filter(publish="private",username__is_superuser=True).count()
	public_user_deals = deals.objects.filter(publish="public",username__is_superuser=False).count()
	private_user_deals = deals.objects.filter(publish="private",username__is_superuser=False).count()
	total_deals = deals.objects.all().count()

	public_admin_jobs = jobs.objects.filter(publish="public",username__is_superuser=True).count()
	private_admin_jobs = jobs.objects.filter(publish="private",username__is_superuser=True).count()
	public_user_jobs = jobs.objects.filter(publish="public",username__is_superuser=False).count()
	private_user_jobs = jobs.objects.filter(publish="private",username__is_superuser=False).count()
	total_jobs = jobs.objects.all().count()

	public_admin_products = products.objects.filter(publish="public",username__is_superuser=True).count()
	private_admin_products = products.objects.filter(publish="private",username__is_superuser=True).count()
	public_user_products = products.objects.filter(publish="public",username__is_superuser=False).count()
	private_user_products = products.objects.filter(publish="private",username__is_superuser=False).count()
	total_products = products.objects.all().count()

	admin_assigned_deal = assign_deal.objects.filter(username__is_superuser=True).count()
	user_assigned_deal = assign_deal.objects.filter(username__is_superuser=False).count()
	total_assigned_deal = assign_deal.objects.all().count()

	admin_assigned_job = assign_job.objects.filter(username__is_superuser=True).count()
	user_assigned_job = assign_job.objects.filter(username__is_superuser=False).count()
	total_assigned_job = assign_job.objects.all().count()

	admin_profile = profile.objects.get(username_id=request.user.id)



	
	
	print("00000000000000000000000000000000000000000000000000000000000000000000000000000000000000",online_admins)
	context = {
	'users':users,
	'profile_list':profile_list,
	'total_admins':total_admins,
	'total_users':total_users,
	'total_registrations':total_registrations,

	'public_admin_deals':public_admin_deals,
	'private_admin_deals':private_admin_deals,
	'public_user_deals':public_user_deals,
	'private_user_deals':private_user_deals,
	'total_deals':total_deals,

	'public_admin_jobs':public_admin_jobs,
	'private_admin_jobs':private_admin_jobs,
	'public_user_jobs':public_user_jobs,
	'private_user_jobs':private_user_jobs,
	'total_jobs':total_jobs,

	'public_admin_products':public_admin_products,
	'private_admin_products':private_admin_products,
	'public_user_products':public_user_products,
	'private_user_products':private_user_products,
	'total_products':total_products,

	'admin_assigned_deal':admin_assigned_deal,
	'user_assigned_deal':user_assigned_deal,
	'total_assigned_deal':total_assigned_deal,

	'admin_assigned_job':admin_assigned_job,
	'user_assigned_job':user_assigned_job,
	'total_assigned_job':total_assigned_job,

	'admin_profile':admin_profile
	}


	return render(request, 'admin_userdata.html',context)


# def search_userdata(request):
# 	if request.method == "POST":
# 		searched = request.POST['searched']
# 		result = profile.objects.filter(username__first_name__contains=searched)


# 		context = {'searched':searched,'result':result}
# 		return render(request, 'search_userdata.html',context)
# 	else:
# 		return render(request, 'search_userdata.html')


def admin_assigns(request):
	users = User.objects.all()
	admin_assigned_deals_list = assign_deal.objects.all()
	admin_assigned_jobs_list = assign_job.objects.all()
	admin_profile = profile.objects.get(username_id=request.user.id)
	context = {'users':users,'admin_assigned_deals_list':admin_assigned_deals_list,'admin_assigned_jobs_list':admin_assigned_jobs_list,'admin_profile':admin_profile}
	return render(request, 'admin_assigns.html',context)

def delete_assigned_deal(request):
	if request.method == 'POST':
		id_delete = request.POST.get('id_delete')
		assigned_deal_delete = assign_deal.objects.get(id=id_delete).delete()
		messages.info(request,"Assigned Deal Deleted")
		return redirect('admin_assigns')
	else:
		messages.info(request,"No Assaigned Deal Deleted")
		return redirect('admin_assigns')



def delete_assigned_job(request):
	if request.method == 'POST':
		id_delete = request.POST.get('id_delete')
		assigned_job_delete = assign_job.objects.get(id=id_delete).delete()
		messages.info(request,"Assigned Job Deleted")
		return redirect('admin_assigns')
	else:
		messages.info(request,"No Assaigned Job Deleted")
		return redirect('admin_assigns')


def admin_notifications(request):
	if request.method == 'POST':
		notification = request.POST.get('notification')

		user = User.objects.get(id=request.user.id)
		notifications(notification=notification,username=user).save()
		messages.info(request,"Notification Added")
		return redirect('admin_notifications')
	else:
		total_users =  profile.objects.filter(username__is_superuser=False)
		notifications_list = notifications.objects.all()
		feedbacks_list = feedbacks.objects.all()
		admin_profile = profile.objects.get(username_id=request.user.id)
		context = {'total_users':total_users,'notifications_list':notifications_list,'feedbacks_list':feedbacks_list,'admin_profile':admin_profile}
		return render(request, 'admin_notification.html',context)



def logout(request):
	auth.logout(request)
	return redirect('/')
