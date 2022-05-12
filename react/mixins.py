class ReactMixin:
    """
    Export Props for React App
    html include react_props.html
    """
    app_root = ''

    def get_app_root(self):
        return self.app_root

    def get_props_data(self):
        return {}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['props'] = self.get_props_data()
        context['app_root'] = self.get_app_root()
        return context
