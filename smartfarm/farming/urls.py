from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('threats/', views.threat_list, name='threat_list'),
    path('threats/<int:pk>/', views.threat_detail, name='threat_detail'),
    path('crop-tips/', views.crop_tips, name='crop_tips'),
    path('ask-expert/', views.ask_expert, name='ask_expert'),
    path('wildlife/', views.wildlife, name='wildlife'),
    path('pests/', views.pests, name='pests'),
    path('weeds/', views.weeds, name='weeds'),
    path('weather/', views.weather, name='weather'),
    path('market-prices/', views.market_prices, name='market_prices'),
    path('irrigation/', views.irrigation_calculator, name='irrigation'),
    path('govt-schemes/', views.govt_schemes, name='govt_schemes'),
    path('community/', views.community, name='community'),
    path('community/post/', views.community_post, name='community_post'),
    path('community/like/<int:pk>/', views.community_like, name='community_like'),

    path('community/<int:post_id>/comment/', views.community_comment, name='community_comment'),
    path('community/comment/<int:comment_id>/like/', views.community_comment_like, name='community_comment_like'),

    # 1-to-1 Chat
    path('chat/', views.chat_list, name='chat_list'),
    path('chat/new/', views.chat_new, name='chat_new'),
    path('chat/<int:room_id>/', views.chat_room, name='chat_room'),
    path('chat/<int:room_id>/send/', views.chat_send, name='chat_send'),
    path('chat/<int:room_id>/messages/', views.chat_messages_api, name='chat_messages_api'),
    path('chat/<int:room_id>/resolve/', views.chat_resolve, name='chat_resolve'),

    # Farmer Registration
    path('register/', views.farmer_register, name='farmer_register'),

    # Admin / Expert Panel
    path('expert-panel/', views.expert_panel, name='expert_panel'),
    path('expert-panel/sms/', views.send_sms_alert, name='send_sms_alert'),
    path('expert-panel/answer/<int:pk>/', views.answer_query, name='answer_query'),

    # Live Mandi Prices API (proxied)
    path('api/mandi-prices/', views.mandi_prices_api, name='mandi_prices_api'),
]
