from django.conf.urls import url

from notification.views import notice_settings

urlpatterns = (
    url(r"^settings/$", notice_settings, name="notification_notice_settings"),
)
