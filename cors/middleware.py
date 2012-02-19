from django.http import HttpResponse


class AllowOriginMiddleware(object):
    def process_request(self, request):
        if request.method == 'OPTIONS':
            response = HttpResponse()
            return response

    def process_response(self, request, response):
        origin = request.META.get('HTTP_ORIGIN')
        if origin:
            response['Access-Control-Allow-Origin'] = origin
            response['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
            response['Access-Control-Max-Age-'] = 1000
            response['Access-Control-Allow-Headers'] = 'Content-Type'
        return response
