from django.contrib import admin
from src.forum.models import Comment, Section, Topic


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('topic_name', '__str__', 'user', 'created_at')
    list_display_links = ('__str__',)
    fields = ('topic', 'user', 'text', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('topic__name', 'user__username')
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
    list_display = ('name', 'section_name', 'user', 'slug', 'created_at')
    search_fields = ('name', 'user__username', 'section__name')
    fields = ('name', 'section', 'user', 'slug', 'created_at')
    readonly_fields = ('slug', 'created_at')

    @admin.display(description='Section', ordering='section__name')
    def section_name(self, obj):
        return obj.section.name
