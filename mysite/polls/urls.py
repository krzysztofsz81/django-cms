from django.conf.urls import url
from . import views

urlpatterns = [
    # 127.0.0.1/polls
    url(r'^$', views.index, name="index"),

    # 127.0.0.1/polls
    url(r'^contacts$', views.contacts, name="contacts"),

    # 127.0.0.1/contacts/{id}
    url(r'^contacts/(?P<contact_id>[0-9]+)/$', views.contact, name="contact"),

    # 127.0.0.1/polls/{id}
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name="detail"),

    # 127.0.0.1/polls/{id}/results
    url(r'^(?P<question_id>[0-9]+)/results$', views.results, name="results"),

    # 127.0.0.1/polls/{id}/vote
    url(r'^(?P<question_id>[0-9]+)/vote$', views.vote, name="vote"),
]