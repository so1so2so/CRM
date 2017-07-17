# _*_coding:utf-8_*_
# from django.contrib import admin
import xadmin as admin
# Register your models here.
from xadmin import views


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

admin.site.register(views.BaseAdminView, BaseSetting)


class AdminSettings(object):
    # 设置base_site.html的Title
    site_title = 'TMS管理系统'
    # 设置base_site.html的Footer
    site_footer = 'SGTMS2017'
    # menu_style = 'default'
    menu_style = "accordion"
    # 菜单设置

    def get_site_menu(self):
        return (
    {'title': '学员管理', 'perm': self.get_model_perm(models.UserProfile, 'change'), 'menus':(
    {'title': '学员咨询管理', 'icon': 'info-sign', 'url': self.get_model_url(models.Customer, 'changelist') },
    {'title': '学员咨询情况', 'icon': 'file', 'url': self.get_model_url(models.ConsultRecord, 'changelist') },
                    )},
    {'title': '课程管理', 'perm': self.get_model_perm(models.ClassList, 'change'),
     'menus':(
     {'title': '上课记录', 'url': self.get_model_url(models.CourseRecord, 'changelist') },
    {'title': '课程分数', 'url': self.get_model_url(models.StudyRecord, 'changelist') },
                    )},
                )

admin.site.register(views.CommAdminView, AdminSettings)
import models
admin.site.register(models.ClassList)
admin.site.register(models.Course)
admin.site.register(models.UserProfile)
admin.site.register(models.ConsultRecord)
admin.site.register(models.Customer)
admin.site.register(models.StudyRecord)
admin.site.register(models.School)
admin.site.register(models.CourseRecord)
