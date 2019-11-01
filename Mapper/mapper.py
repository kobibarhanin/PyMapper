from Mapper import *


def trace_calls(frame, event, arg):

    if event != 'call':
        return

    co = frame.f_code
    func_name = co.co_name
    func_line_no = frame.f_lineno
    func_filename = co.co_filename
    caller = frame.f_back
    caller_func_name = caller.f_code.co_name
    caller_line_no = caller.f_lineno
    caller_filename = caller.f_code.co_filename

    # if workspace not in func_filename \
    #         or context not in func_filename \
    #         or rule_out1 in func_filename \
    #         or rule_out2 in func_filename \
    #         or rule_out3 in func_filename \
    #         or func_name[0] == '<' or func_name[0] == '_':
    #     return

    # flow = f'{caller_filename}[{caller_func_name}] >> {func_filename}[{func_name}]'
    flow = f'{caller_func_name},{func_name}'

    with open('stack_log.txt', 'a') as stack_log:
        stack_log.write(flow+';')

    print(flow)

    return