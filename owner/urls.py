from django.urls import path
from owner import views


urlpatterns=[
    path("mobiles/add",views.mobile_create,name="addmobiles"),
    path("home",views.home,name="home"),
    path("brands/add",views.brand_create,name="addbrands"),
    path("brands/list",views.list_brand,name="brandlist"),
    path("brand/display/<int:id>",views.view_brand,name="display"),
    path("brand/update/<int:id>", views.update_brand, name="update"),
    path("brand/remove/<int:id>", views.remove_brand, name="remove"),
    path("mobiles",views.mobile_list,name="listmobiles"),
    path("mobiles/change/<int:id>",views.mobile_update,name="updatemobile"),
    path("mobiles/<int:id>",views.mobile_detail,name="mobiledetail"),
    path("mobiles/remove/<int:id>",views.remove_mobile,name="removemobile")

]

