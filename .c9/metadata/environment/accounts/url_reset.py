{"filter":false,"title":"url_reset.py","tooltip":"/accounts/url_reset.py","ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":10,"column":1},"end":{"row":10,"column":1},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"hash":"aa4bcc60d4ec80f0bf94a42a1fdfc121941679d0","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":10,"column":1},"action":"insert","lines":["from django.conf.urls import url","from django.core.urlresolvers import reverse_lazy","from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete","","urlpatterns = [","    url('^$', password_reset, {'post_reset_redirect': reverse_lazy('password_reset_done')}, name='password_reset'),","    url(r'^done/$', password_reset_done, name='password_reset_done'),","    url(r'^(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,","        {'post_reset_redirect': reverse_lazy('password_reset_complete')}, name='password_reset_confirm'),","    url('^complete/$', password_reset_complete, name='password_reset_complete')","]"],"id":1}]]},"timestamp":1562678174455}