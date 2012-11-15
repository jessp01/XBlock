from django.shortcuts import render_to_response

from xmodule.xmodule import XModule

class DebuggerRuntime(object):
    children = []

def index(request):
    xmodules = XModule.load_classes()
    return render_to_response('index.html', {
        'xmodules': xmodules
    })

def module(request, module_name):
    module = XModule.load_class(module_name)
    content = course_settings = student_state = user_preferences = {}
    runtime = DebuggerRuntime()

    module = module(runtime, content, course_settings, user_preferences, student_state)

    return render_to_response('module.html', {
        'module': module,
        'student_view': module.render('student_view'),
    })
