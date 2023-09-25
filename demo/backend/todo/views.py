from django.views.generic import TemplateView
from react.mixins import ReactMixin


class IndexView(ReactMixin, TemplateView):
    template_name = 'react/react.html'
    app_root = 'todo/components/todo.jsx'
    def get_props_data(self):
        return {
            'data': ['Eat Launch', 'Watch a movie', 'Sleep']
        }
