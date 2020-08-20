from django.utils.deprecation import MiddlewareMixin
class Test1MiddleWare(MiddlewareMixin):

    def process_request(self,request):
        print('请求前执行')
        username=request.COOKIES.get('username')
        if username:
            print('有信息')
        else:
            print('是一个新用户')

    def process_response(self,request,response):
        print('响应前执行')
        return response