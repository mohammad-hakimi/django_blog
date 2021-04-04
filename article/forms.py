from django.forms import ModelForm
from article.models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'category', 'content', 'image']

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = None
        self.fields['category'].widget.choices = self.fields['category'].choices
