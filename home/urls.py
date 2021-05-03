from . views import *
from django.urls import path, re_path


urlpatterns = [
	#home page
	path('', user_home, name='user_home'),

	#login and signup,premium signup
	path('user_login', user_login, name='user_login'),
	path('user_signup', user_signup, name='user_signup'),
	path('premium_user_signup', premium_user_signup, name='premium_user_signup'),

	#user profile,profile pic update,
	path('profiles', profiles, name='profiles'),
	path('update_user_profile_pic', update_user_profile_pic, name='update_user_profile_pic'),

	#user deals
	path('deal', deal, name='deal'),

	#user jobs
	path('job', job, name='job'),

	#user products
	path('product', product, name='product'),

	#user myads
	path('myads', myads, name='myads'),

	#daily tasks,delete assaigned deal and job
	path('daily_task', daily_task, name='daily_task'),
	path('delete_assaigned_deal', delete_assaigned_deal, name='delete_assaigned_deal'),
	path('delete_assaigned_job', delete_assaigned_job, name='delete_assaigned_job'),

	#user chats,feedbacks
	path('chats', chats, name='chats'),
	path('feedback', feedback, name='feedback'),

	#deletes--deal,job,product
	path('delete_deal', delete_deal, name='delete_deal'),
	path('delete_job', delete_job, name='delete_job'),
	path('delete_product', delete_product, name='delete_product'),

	#detailviews--deals,jobs,products
	path('detail_view_deals<int:id>/', detail_view_deals, name='detail_view_deals'),
	path('detail_view_jobs<int:id>/', detail_view_jobs, name='detail_view_jobs'),
	path('detail_view_products<int:id>/', detail_view_products, name='detail_view_products'),


	

	#logout
	path('user_logout', user_logout, name='user_logout'),

		
]
