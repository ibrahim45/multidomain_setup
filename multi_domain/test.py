# test.py
def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    print("Ibrahim sha -- multi domain")
    return [b"Hello World"] # python3
    #return ["Hello World"] # python2
