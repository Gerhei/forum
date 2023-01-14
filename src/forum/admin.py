from django.contrib import admin
from src.forum.models import Account, Comment, Section, Topic


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'slug', 'reputation')
    fields = ('user', 'slug', 'reputation', 'description')
    readonly_fields = ('slug',)
    search_fields = ('user__username',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('topic_name', '__str__', 'account', 'created_at')
    list_display_links = ('__str__',)
    fields = ('topic', 'account', 'text', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('topic__name', 'account__user__username')
    list_filter = ('created_at',)

    @admin.display(description='Topic', ordering='topic__name')
    def topic_name(self, obj):
        return obj.topic.name


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'order', 'parent_name')
    fields = ('name', 'slug', 'order', 'parent')
    readonly_fields = ('slug', 'order')
    search_fields = ('name',)
    list_filter = ('order',)

    @admin.display(description='Parent', ordering='section__name')
    def parent_name(self, obj):
        if obj.parent:
            return obj.parent.name
        return self.get_empty_value_display()


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'section_name', 'account', 'slug', 'created_at')
    search_fields = ('name', 'account__user__username', 'section__name')

    @admin.display(description='Section', ordering='section__name')
    def section_name(self, obj):
        return obj.section.name
