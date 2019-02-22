from django.contrib import admin
from web.models import User, Invoice, Statistics

# update the models header && title
admin.site.site_header = '发票识别系统后台管理'
admin.site.site_title = '发票识别'
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('user_id', 'user_password', 'user_phone',)
    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50
    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('-user_id',)
    # 操作项功能显示位置设置，两个都为True则顶部和底部都显示
    actions_on_top =True
    actions_on_bottom = True
    # 操作项功能显示选中项的数目
    actions_selection_counter = True
    # 字段为空值显示的内容
    empty_value_display = ' -空白- '
    # list_editable 设置默认可编辑字段（user_id默认不可编辑，因为它是一个链接，点击会进入修改页面）
    list_editable = ['user_password', 'user_phone',]
    # fk_fields 设置显示外键字段
    fk_fields = ('user_id',)
    # 过滤器功能及能过滤的字段
    list_filter = ('user_phone',)
    # 搜索功能及能实现搜索的字段
    search_fields = ('user_id', 'user_phone',)

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('user_id', 'inv_numh', 'inv_numd', 'inv_money',)
    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50
    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('-user_id',)
    # 操作项功能显示位置设置，两个都为True则顶部和底部都显示
    actions_on_top =True
    actions_on_bottom = True
    # 操作项功能显示选中项的数目
    actions_selection_counter = True
    # 字段为空值显示的内容
    empty_value_display = ' -空白- '
    # list_editable 设置默认可编辑字段（user_id默认不可编辑，因为它是一个链接，点击会进入修改页面）
    list_editable = ['inv_numh', 'inv_numd', 'inv_money',]
    # fk_fields 设置显示外键字段
    fk_fields = ('user_id',)
    # 过滤器功能及能过滤的字段
    list_filter = ('inv_money', 'inv_date',)
    # 搜索功能及能实现搜索的字段
    search_fields = ('user_id', 'inv_numh', 'inv_numd', 'inv_money', )

@admin.register(Statistics)
class StatisticsAdmin(admin.ModelAdmin):
    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('sta_user_id', 'sta_num', 'sta_total_money', 'sta_average_money',)
    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50
    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('-sta_user_id',)
    # 操作项功能显示位置设置，两个都为True则顶部和底部都显示
    actions_on_top =True
    actions_on_bottom = True
    # 操作项功能显示选中项的数目
    actions_selection_counter = True
    # 字段为空值显示的内容
    empty_value_display = ' -空白- '
    # list_editable 设置默认可编辑字段（sta_user_id默认不可编辑，因为它是一个链接，点击会进入修改页面）
    list_editable = ['sta_num', 'sta_total_money', 'sta_average_money',]
    # fk_fields 设置显示外键字段
    fk_fields = ('sta_user_id',)
    # 过滤器功能及能过滤的字段
    list_filter = ('sta_num', 'sta_total_money', 'sta_average_money',)
    # 搜索功能及能实现搜索的字段
    search_fields = ('sta_num', 'sta_total_money', 'sta_average_money',)