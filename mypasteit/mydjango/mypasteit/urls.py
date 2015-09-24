from django.conf.urls import url, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

# ---This is the 1st stage of using DRF---
# ---This is the 2nd stage of using DRF---
# urlpatterns = [
#     url(r'^$', views.snippet_list),
#     url(r'^(?P<pk>[0-9]+)$', views.snippet_detail)
# ]
#
# -----------------------------------------------
#
# ---This is the 3rd stage of using DRF---
# ---This is the 4th stage of using DRF---
# ---This is the 5th stage of using DRF---
# urlpatterns = [
#     url(r'^$', views.SnippetList.as_view()),
#     url(r'^(?P<pk>[0-9]+)$', views.SnippetDetail.as_view())
# ]
#
# urlpatterns = format_suffix_patterns(urlpatterns)
#
# -------------------------------------------------
#
# ---This is the 6th stage of using DRF---

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
# router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]