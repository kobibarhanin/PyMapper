import os
import yaml

def prefix(subject, ctx):
    return subject.startswith(ctx)


def has(subject, ctx):
    return ctx in subject


def exclude(subject, rule, ctx):
    return rule(subject, ctx)


def enforce(subject, rule, ctx):
    return rule(subject, ctx)


class Mapper:

    def __init__(self, conf_file) -> None:
        self.stack_file = os.path.dirname(os.path.abspath(__file__)) + '/stack_log.txt'
        self.create_stack_log()
        self.confs = self.parse_confs(conf_file)
        self.callees = []

    @staticmethod
    def parse_confs(conf_file):
        try:
            with open(conf_file, 'r') as stream:
                configs = yaml.safe_load(stream)
            return configs
        except Exception:
            print(f'No configuration')
            return None

    def create_stack_log(self):
        try:
            os.remove(self.stack_file)
        except:
            pass
        open(self.stack_file, 'a').close()

    def trace_calls(self, frame, event, arg):

        if event != 'call':
            return

        callee = frame.f_code
        callee_func = callee.co_name
        callee_file = callee.co_filename
        caller = frame.f_back
        caller_func = caller.f_code.co_name
        caller_file = caller.f_code.co_filename

        try:
            force_out = True
            enforce_files = self.confs["enforce_files"]
            for context, rules in enforce_files.items():
                for rule in rules.split(","):
                    if enforce(caller_file, globals()[context], rule) or enforce(callee_file, globals()[context], rule):
                        force_out = False

            if force_out:
                return
        except:
            pass

        try:
            exclude_files = self.confs["exclude_files"]
            for context, rules in exclude_files.items():
                for rule in rules.split(","):
                    if exclude(caller_file, globals()[context], rule) or exclude(callee_file, globals()[context], rule):
                        return
        except:
            pass

        try:
            exclude_funcs = self.confs["exclude_funcs"]
            for context, rules in exclude_funcs.items():
                for rule in rules.split(","):
                    if exclude(caller_func, globals()[context], rule) or exclude(callee_func, globals()[context], rule):
                        return
        except:
            pass

        flow = caller_func + ',' + callee_func + ';'

        if self.callees:
            last_target = self.callees[-1]

            if last_target != caller_func:
                flow = last_target + ',' + caller_func + ";" + flow

        self.callees.append(callee_func)

        with open(self.stack_file, 'a') as stack_log:
            stack_log.write(flow)

        print(caller_file + ':' + caller_func + '===>' + callee_file + ':' + callee_func)

        return


if __name__ == '__main__':
    mapper = Mapper('../Targets/simpleApp/mapping_rules')