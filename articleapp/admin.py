from django.contrib import admin

from .models import Article, TeamMember

admin.site.register(TeamMember)


class MemberInline(admin.TabularInline):
    model = TeamMember # 어느 모델을 가져올 것인지


class ArticleAdmin(admin.ModelAdmin):
    # 각 필드를 구분하는 대표제목을 설정한다. (리스트 내 튜플)
    fieldsets = [
        ('프로젝트 제목', {'fields': ['title']}),
        ('프로젝트 간단 소개', {'fields': ['Introduce']}),
        ('진행정보', {'fields': ['local','lapse', 'deadline']}),
        ('현재팀원', {'fields': ['now_pd', 'now_dev', 'now_designer']}),

    ]
    inlines = [MemberInline] # 해당 클래스를 인라인으로 추가한다.
    list_display = ('Publisher', 'title', 'Introduce')


admin.site.register(Article, ArticleAdmin)