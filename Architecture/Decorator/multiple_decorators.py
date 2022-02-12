import imp
import imaplib
from trace_decorator import trace_decorator1, trace_decorator2

# 데코레이터를 여러 개 지정
@trace_decorator1
@trace_decorator2
def hello():
    print('hello')
 
hello()