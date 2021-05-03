from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from admin_phase.models import *

# Create your views here.


def user_home(request):
	if request.user.is_authenticated:
		user_profile = profile.objects.get(username_id=request.user.id)
		context = {'user_profile':user_profile}
		return render(request, 'user_home.html',context)
	else:
		return render(request, 'user_home.html')


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

				pr = profile(username=user,phone=phone,refferalcode=refferalcode,usertype="free").save()

				messages.info(request,"Registered Successfully")
				return redirect('user_home')

		else:
			messages.info(request,'Password not matching')
			return redirect('user_home')

	else:
		return redirect('user_home')








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

				pr = profile(username=user,phone=phone,refferalcode=refferalcode,usertype="premium").save()

				messages.info(request,"Registered Successfully")
				return redirect('user_home')

		else:
			messages.info(request,'Password not matching')
			return redirect('user_home')

	else:
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
		user_profile = profile.objects.get(username_id=request.user.id)
		context = {'user_profile':user_profile}
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




def deal(request):
	if request.method == 'POST':
		publish = request.POST['publish']
		deal_name = request.POST['deal_name']
		price = request.POST['price']
		category = request.POST['category']
		# email = request.POST['email']
		# contact = request.POST['contact']
		location = request.POST['location']
		deal_type = request.POST['deal_type']
		brand_name = request.POST['brand_name']
		picture = request.FILES.get('picture')
		attach = request.FILES.getlist('attachments')
		details = request.POST['details']


		user = User.objects.get(id=request.user.id)
		
		user_deals_add = deals(username=user,publish=publish,deal_name=deal_name,price=price,category=category,location=location,deal_type=deal_type,brand_name=brand_name,picture=picture,details=details)
		user_deals_add.save()

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
			user_profile = profile.objects.get(username_id=request.user.id)
			# user = User.objects.get(id=request.user.id)
			user_deals_list = deals.objects.all()
			context = {'user_deals_list':user_deals_list,'user_profile':user_profile}
			return render(request, 'user_deals.html',context)
		else:
			user_deals_list = deals.objects.all()
			context = {'user_deals_list':user_deals_list}
			return render(request, 'user_deals.html',context)






def job(request):
	if request.method == 'POST':
		publish = request.POST['publish']
		job_name = request.POST['job_name']
		price = request.POST['price']
		category = request.POST['category']
		# email = request.POST['email']
		# contact = request.POST['contact']
		location = request.POST['location']
		job_type = request.POST['job_type']
		brand_name = request.POST['brand_name']
		picture = request.FILES.get('picture')
		attach = request.FILES.getlist('attachments')
		details = request.POST['details']

		user = User.objects.get(id=request.user.id)
		
		user_jobs_add = jobs(username=user,publish=publish,job_name=job_name,price=price,category=category,location=location,job_type=job_type,brand_name=brand_name,picture=picture,details=details)
		user_jobs_add.save()

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
			user_profile = profile.objects.get(username_id=request.user.id)
			# user = User.objects.get(id=request.user.id)
			user_jobs_list = jobs.objects.all()
			context = {'user_jobs_list':user_jobs_list,'user_profile':user_profile}
			return render(request, 'user_jobs.html',context)
		else:
			user_jobs_list = jobs.objects.all()
			context = {'user_jobs_list':user_jobs_list}
			return render(request, 'user_jobs.html',context)





def product(request):
	if request.method == 'POST':
		publish = request.POST['publish']
		product_name = request.POST['product_name']
		price = request.POST['price']
		category = request.POST['category']
		# email = request.POST['email']
		# contact = request.POST['contact']
		location = request.POST['location']
		product_type = request.POST['product_type']
		brand_name = request.POST['brand_name']
		picture = request.FILES.get('picture')
		attach = request.FILES.getlist('attachments')
		details = request.POST['details']

		user = User.objects.get(id=request.user.id)
		
		user_products_add = products(username=user,publish=publish,product_name=product_name,price=price,category=category,location=location,product_type=product_type,brand_name=brand_name,picture=picture,details=details)
		user_products_add.save()

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
			user_profile = profile.objects.get(username_id=request.user.id)
			# user = User.objects.get(id=request.user.id)
			user_products_list = products.objects.all()
			context = {'user_products_list':user_products_list,'user_profile':user_profile}
			return render(request, 'user_products.html',context)
		else:
			user_products_list = products.objects.all()
			context = {'user_products_list':user_products_list}
			return render(request, 'user_products.html',context)



def myads(request):
	user = User.objects.get(id=request.user.id)
	user_deals_list = deals.objects.filter(username_id=request.user.id)
	user_jobs_list = jobs.objects.filter(username_id=request.user.id)
	user_products_list = products.objects.filter(username_id=request.user.id)
	user_profile = profile.objects.get(username_id=request.user.id)
	context = {'user':user,'user_deals_list':user_deals_list,'user_jobs_list':user_jobs_list,'user_products_list':user_products_list,'user_profile':user_profile}
	return render(request, 'user_myads.html',context)


def daily_task(request):
	user = User.objects.get(id=request.user.id)
	daily_deals_list = assign_deal.objects.filter(assigns=request.user.id)
	daily_jobs_list = assign_job.objects.filter(assigns=request.user.id)
	# user_products_list = products.objects.filter(username_id=request.user.id)
	user_profile = profile.objects.get(username_id=request.user.id)
	context = {'user':user,'daily_deals_list':daily_deals_list,'daily_jobs_list':daily_jobs_list,'user_profile':user_profile}
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
	user = User.objects.get(id=request.user.id)
	notifications_list = notifications.objects.all()
	user_profile = profile.objects.get(username_id=request.user.id)
	context = {'user':user,'notifications_list':notifications_list,'user_profile':user_profile}
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
		category = request.POST['category']
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
		user_deals_update.category = category
		# user_deals_update.email = email
		# user_deals_update.contact = contact
		user_deals_update.location = location
		user_deals_update.deal_type = deal_type
		user_deals_update.brand_name = brand_name
		user_deals_update.picture = picture
		user_deals_update.details = details

		user_deals_update.save()

		for i in attach:
			deal_attachments(deal=user_deals_update,attachment=i).save()

		messages.info(request,"Deal Updated")
		return redirect('myads')
	else:
		user = User.objects.get(id=request.user.id)
		user_deals_list =  deals.objects.get(id=id)
		user_profile = profile.objects.get(username_id=request.user.id)
		context = {'user':user,'user_deals_list':user_deals_list,'user_profile':user_profile}
		return render(request,'user_deals_edit.html',context)
		



def detail_view_jobs(request,id):
	if request.method == 'POST':
		publish = request.POST['publish']
		job_name = request.POST['job_name']
		price = request.POST['price']
		category = request.POST['category']
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
		user_jobs_update.category = category
		# user_jobs_update.email = email
		# user_jobs_update.contact = contact
		user_jobs_update.location = location
		user_jobs_update.job_type = job_type
		user_jobs_update.brand_name = brand_name
		user_jobs_update.picture = picture
		user_jobs_update.details = details

		user_jobs_update.save()

		for i in attach:
			job_attachments(job=user_jobs_update,attachment=i).save()

		messages.info(request,"Job Updated")
		return redirect('myads')
	else:
		user = User.objects.get(id=request.user.id)
		user_jobs_list =  jobs.objects.get(id=id)
		user_profile = profile.objects.get(username_id=request.user.id)
		context = {'user':user,'user_jobs_list':user_jobs_list,'user_profile':user_profile}
		return render(request,'user_jobs_edit.html',context)
		

def detail_view_products(request,id):
	if request.method == 'POST':
		publish = request.POST['publish']
		product_name = request.POST['product_name']
		price = request.POST['price']
		category = request.POST['category']
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
		user_products_update.category = category
		# user_products_update.email = email
		# user_products_update.contact = contact
		user_products_update.location = location
		user_products_update.product_type = product_type
		user_products_update.brand_name = brand_name
		user_products_update.picture = picture
		user_products_update.details = details

		user_products_update.save()

		for i in attach:
			product_attachments(product=user_products_update,attachment=i).save()

		messages.info(request,"Product Updated")
		return redirect('myads')
	else:
		user = User.objects.get(id=request.user.id)
		user_products_list =  products.objects.get(id=id)
		user_products_attach_list = product_attachments.objects.filter(product_id=id)
		user_profile = profile.objects.get(username_id=request.user.id)
		context = {'user':user,'user_products_list':user_products_list,'user_products_attach_list':user_products_attach_list,'user_profile':user_profile}
		return render(request,'user_products_edit.html',context)


def user_logout(request):
	auth.logout(request)
	return redirect('/')
