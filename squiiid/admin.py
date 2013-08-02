from squiiid.models import SquiiidImage, Tag, Invite
from django.contrib import admin

#class OrderAdmin(admin.ModelAdmin):
#    list_display = ('id','name','customer','num_colors','payment_date','date','status','active')
#    
#    def get_order_email(self,obj):
#        return obj.customer.email

admin.site.register(SquiiidImage)
admin.site.register(Tag)
admin.site.register(Invite)

#admin.site.register(Order,OrderAdmin)