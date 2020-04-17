# from django.views.generic import TemplateView
# from django.conf.urls import url
# from django.urls import path, re_path
# from .views import Home, Assets


# # # new version

# # # urlpatterns = [
# # #     # path('', Home.as_view()),
# # #     re_path(r'^[\w\?\=\-\/]*$', Home.as_view()),
# # #     re_path(r'(?P<filename>(assets/)?[\w\.\-\/]+)$', Assets.as_view())
# # # ]

# # # old version

# urlpatterns = [
#     path('', Home.as_view()),
#     re_path(r'^(?P<filename>[\w\.]+)$', Assets.as_view()),
#     # url(r'^$', TemplateView.as_view(template_name='index.html')),
#     # re_path(r'^.*$', index)
# ]
