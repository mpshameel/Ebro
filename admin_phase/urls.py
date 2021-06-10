from . views import *
from django.urls import path, re_path

urlpatterns = [
	#home page
	path('', admin_home, name='admin_home'),

	#admin ads managment
	path('admin_ads', admin_ads, name='admin_ads'),
	path('delete_admin_ads', delete_admin_ads, name='delete_admin_ads'),
	path('admin_ads_edit<int:id>/', admin_ads_edit, name='admin_ads_edit'),
	
	#login and signup
	path('admin_login', admin_login, name='admin_login'),
	path('admin_signup', admin_signup, name='admin_signup'),



	path('add_premiumuser_payment', add_premiumuser_payment, name='add_premiumuser_payment'),
	path('complete_addpremiumuser_payment', complete_addpremiumuser_payment, name='complete_addpremiumuser_payment'),


	


	#profile update,profile pic update
	path('admin_profile', admin_profile, name='admin_profile'),
	path('update_admin_profile_pic', update_admin_profile_pic, name='update_admin_profile_pic'),

	#admin deals,delete deals,detail view of deal and edit ,delete deal attachments, assign deal,search assign deal
	path('admin_deals', admin_deals, name='admin_deals'),
	path('delete_admin_deals', delete_admin_deals, name='delete_admin_deals'),
	path('detail_view_admin_deals<int:id>/', detail_view_admin_deals, name='detail_view_admin_deals'),
	path('delete_deal_attach', delete_deal_attach, name='delete_deal_attach'),
	path('assign_admin_deals<int:id>/', assign_admin_deals, name='assign_admin_deals'),


	#admin jobs,delete jobs,detail view of jobs and edit ,delete job attachments, assign job
	path('admin_jobs', admin_jobs, name='admin_jobs'),
	path('delete_admin_jobs', delete_admin_jobs, name='delete_admin_jobs'),
	path('detail_view_admin_jobs<int:id>/', detail_view_admin_jobs, name='detail_view_admin_jobs'),
	path('delete_job_attach', delete_job_attach, name='delete_job_attach'),
	path('assign_admin_jobs<int:id>/', assign_admin_jobs, name='assign_admin_jobs'),
	


	#admin Products,delete Products,detail view of Products and edit ,delete product attachment,search 
	path('admin_products', admin_products, name='admin_products'),
	path('delete_admin_products', delete_admin_products, name='delete_admin_products'),
	path('detail_view_admin_products<int:id>/', detail_view_admin_products, name='detail_view_admin_products'),
	path('delete_product_attach', delete_product_attach, name='delete_product_attach'),
	path('update_product_offer<int:id>/', update_product_offer, name='update_product_offer'),
	



	#my ads,delete my ads
	path('admin_myads', admin_myads, name='admin_myads'),


	#user data,search userdata
	path('admin_userdata', admin_userdata, name='admin_userdata'),
	path('add_category', add_category, name='add_category'),
	path('detail_category<int:id>/', detail_category, name='detail_category'),
	path('update_category<int:id>/', update_category, name='update_category'),
	path('delete_subcategory', delete_subcategory, name='delete_subcategory'),
	

	path('add_user', add_user, name='add_user'),
	path('detail_user<int:id>/', detail_user, name='detail_user'),
	# path('degrade_admin<int:id>/', degrade_admin, name='degrade_admin'),
	# path('search_userdata', search_userdata, name='search_userdata'),




	#admin_assigns -- deals and jobs,delete assigned deal and job,
	path('admin_assigns', admin_assigns, name='admin_assigns'),
	path('delete_assigned_deal', delete_assigned_deal, name='delete_assigned_deal'),
	path('delete_assigned_job', delete_assigned_job, name='delete_assigned_job'),


	
	#add notifications,chat with users.
	path('admin_notifications', admin_notifications, name='admin_notifications'),


	#users orders
	# path('admin_orders', admin_orders, name='admin_orders'),
	path('admin_orders_edit<int:id>/', admin_orders_edit, name='admin_orders_edit'),

	#approve payments
	path('admin_payments', admin_payments, name='admin_payments'),
	

	
	#logout
	path('logout', logout, name='logout'),
	
		
]
