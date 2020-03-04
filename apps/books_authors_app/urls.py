from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^addbook$', views.books),
	url(r'^books/(?P<id>[0-9]+)$', views.bookdet),
    url(r'^bookaut$', views.bookaut),

    url(r'^addauthor$', views.addauthor),
    url(r'^addauthorform$', views.addauthorform),
    url(r'^author/(?P<id>[0-9]+)$', views.author),
    url('^add_book_to_author/(?P<author_id>\d+)$', views.add_book_to_author),
]