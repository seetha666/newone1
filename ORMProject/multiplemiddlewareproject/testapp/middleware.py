class FirstMiddleWare(object):
    def __init__(self,get_response):
        self.get_response=get_response
        
    def __call__(self,request):
        print("this line printed middleware-1 before processing")
        response=self.get_response(request)
        print("this line printed middleware-1 after processing")
        return response
    
    
class SecondMiddleWare(object):
    def __init__(self,get_response):
        self.get_response=get_response
        
    def __call__(self,request):
        print("this line printed middleware-2 before processing")
        response=self.get_response(request)
        print("this line printed middleware-2 after processing")
        return response