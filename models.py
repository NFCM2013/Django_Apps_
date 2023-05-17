import datetime

from django.db import models
from django.utils import timezone

from django.contrib import admin

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.question_text
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    #以下追加5月17日
#    was_published_recently.admin_order_field = 'pub_date'
#    was_published_recently.boolean = True
#    was_published_recently.short_description = 'Published recently?'

#class QuestionAdmin(admin.ModelAdmin):
#    list_display = ['question_text', 'was_published_recently']
#    list_filter = ['pub_date']

#admin.site.register(Question, QuestionAdmin)



#        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
