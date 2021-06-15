from . views import *
from django.urls import path, re_path
from django.urls import path,include



urlpatterns = [

	path('update_item', updateItem, name='update_item'),
	# path('update_item<int:id>', updateItem, name='update_item'),


	#ad click count unknown and user
	path('update_adcount', update_adcount, name='update_adcount'),
	path('update_useradcount', update_useradcount, name='update_useradcount'),



	#social accounts login and register
	path('register_social', register_social, name='register_social'),

	# path('accounts/',include('allauth.urls')),



	#home page
	path('', user_home, name='user_home'),

	#login and signup,premium signup
	path('user_login', user_login, name='user_login'),
	path('user_signup', user_signup, name='user_signup'),
	path('premium_user_signup', premium_user_signup, name='premium_user_signup'),
	
	path('premium_signup_payment', premium_signup_payment, name='premium_signup_payment'),
	path('complete_premium_signup_payment', complete_premium_signup_payment, name='complete_premium_signup_payment'),
	

	#user profile,profile pic update,add address
	path('profiles', profiles, name='profiles'),
	path('update_user_profile_pic', update_user_profile_pic, name='update_user_profile_pic'),

	path('topup_payment', topup_payment, name='topup_payment'),
	path('topupcomplete', topupcomplete, name='topupcomplete'),
	path('sendmoney', sendmoney, name='sendmoney'),
	path('voucher_claim', voucher_claim, name='voucher_claim'),
	


	path('add_address', add_address, name='add_address'),
	path('add_address2', add_address2, name='add_address2'),
	
	
	path('offers', offers, name='offers'),
	path('detail_offers<int:id>/', detail_offers, name='detail_offers'),

	#user deals
	path('deal', deal, name='deal'),

	#user jobs
	path('job', job, name='job'),

	#user products
	path('product', product, name='product'),

	#user myads
	path('myads', myads, name='myads'),
	path('myorders', myorders, name='myorders'),
	

	#daily tasks,delete assaigned deal and job
	path('daily_task', daily_task, name='daily_task'),
	path('delete_assaigned_deal', delete_assaigned_deal, name='delete_assaigned_deal'),
	path('delete_assaigned_job', delete_assaigned_job, name='delete_assaigned_job'),

	#user chats,feedbacks
	path('chats', chats, name='chats'),
	path('feedback', feedback, name='feedback'),

	#deletes--deal,job,product, detail views of deal,job and product
	path('delete_deal', delete_deal, name='delete_deal'),
	path('detail_deal<int:id>/', detail_deal, name='detail_deal'),
	path('delete_job', delete_job, name='delete_job'),
	path('detail_job<int:id>/', detail_job, name='detail_job'),
	path('delete_product', delete_product, name='delete_product'),
	path('detail_product<int:id>/', detail_product, name='detail_product'),

	#detailviews--deals,jobs,products
	path('detail_view_deals<int:id>/', detail_view_deals, name='detail_view_deals'),
	path('detail_view_jobs<int:id>/', detail_view_jobs, name='detail_view_jobs'),
	path('detail_view_products<int:id>/', detail_view_products, name='detail_view_products'),
	
	path('user_update_product_offer<int:id>/', user_update_product_offer, name='user_update_product_offer'),


	
	#delete deal ,job,and product attachments
	path('delete_deal_attachments', delete_deal_attachments, name='delete_deal_attachments'),
	path('delete_job_attachments', delete_job_attachments, name='delete_job_attachments'),
	path('delete_product_attachments', delete_product_attachments, name='delete_product_attachments'),


	#wishlist of deal,job,products  
	path('wishlist', wishlist, name='wishlist'),
	#wish to task deal and job
	#wish to cart product
	#delete wish
	path('delete_wish_deal', delete_wish_deal, name='delete_wish_deal'),
	path('delete_wish_job', delete_wish_job, name='delete_wish_job'),
	path('delete_wish_product', delete_wish_product, name='delete_wish_product'),


	#cart products
	path('cart', cart, name='cart'),
	#delete cart products
	path('delete_cart', delete_cart, name='delete_cart'),


	#checkout,add address,payment
	path('checkout', checkout, name='checkout'),
	path('payment', payment, name='payment'),

	path('ordercomplete', ordercomplete, name='ordercomplete'),
	path('ordercomplete_wallet', ordercomplete_wallet, name='ordercomplete_wallet'),
	

	#about us
	path('about_us', about_us, name='about_us'),



	#add deals,jobs,products to wishlist and cart
	path('deal_to_wish', deal_to_wish, name='deal_to_wish'),
	path('deal_to_task', deal_to_task, name='deal_to_task'),

	path('job_to_wish', job_to_wish, name='job_to_wish'),
	path('job_to_task', job_to_task, name='job_to_task'),
	
	path('product_to_wish', product_to_wish, name='product_to_wish'),
	path('product_to_cart', product_to_cart, name='product_to_cart'),


	

	#logout
	path('user_logout', user_logout, name='user_logout'),

		
]
