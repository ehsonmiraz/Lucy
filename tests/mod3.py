import singleton

def modify_q(a):
    singleton.func_queue.put(a*a)