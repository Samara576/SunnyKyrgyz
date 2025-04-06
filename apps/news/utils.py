from rest_framework.response import Response

from apps.travel.utils import translator


def retrieve_trans(self, request, *args, **kwargs):
    instance = self.get_object()
    lang = self.get_language()

    instance.title = translator.translate(instance.title, dest=lang).text
    instance.content = translator.translate(instance.content, dest=lang).text

    serializer = self.get_serializer(instance)
    return Response(serializer.data)