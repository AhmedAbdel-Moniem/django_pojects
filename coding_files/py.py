class myexp(Exception): pass

try:
    raise myexp('hello')
except myexp as me:
    print(me)