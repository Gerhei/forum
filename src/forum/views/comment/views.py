from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import FormView

from src.forum.services.topic import TopicService
from src.forum.forms.comment import CommentForm


class CommentCreateView(LoginRequiredMixin, FormView):
    http_method_names = ['post']
    form_class = CommentForm

    def form_valid(self, form):
        comment = TopicService().create_comment(topic_id=self.kwargs['topic_pk'],
                                                text=form.cleaned_data['text'],
                                                user=self.request.user)
        return HttpResponseRedirect(comment.topic.get_absolute_url())
