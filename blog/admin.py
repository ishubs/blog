from django.contrib import admin
from blog.models import Post, Category, emailid, images, Comments

class PostAdmin(admin.ModelAdmin):
	pass

class CommentsAdmin(admin.ModelAdmin):
	pass

class CategoryAdmin(admin.ModelAdmin):
	pass

class emailAdmin(admin.ModelAdmin):
	pass

class imageAdmin(admin.ModelAdmin):
	pass

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(emailid , emailAdmin)
admin.site.register(images, imageAdmin)
admin.site.register(Comments, CommentsAdmin)
