import importlib
import re
import json


def construct_value(value, separator, variables=None):
    if variables is None:
        variables = {}
    pattern = rf"\{separator}([a-zA-Z_.]+)\(([^)]*)\)"
    var_pattern = r"\{([^}]+)\}"

    def replace_variable(match):
        var_name = match.group(1)
        var_value = variables.get(var_name, match.group(0))
        try:
            return int(var_value) if var_value.isdigit() else var_value
        except AttributeError:
            return var_value

    value = re.sub(var_pattern, lambda match: str(replace_variable(match)), value)

    def split_args(arg_str):
        args = []
        temp_arg = ''
        stack = []
        in_string = False
        escape = False
        for char in arg_str:
            if escape:
                temp_arg += char
                escape = False
            elif char == '\\':
                temp_arg += char
                escape = True
            elif in_string:
                if char == in_string:
                    in_string = False
                temp_arg += char
            elif char in ['"', "'"]:
                in_string = char
                temp_arg += char
            elif char in ['[', '{']:
                stack.append(char)
                temp_arg += char
            elif char in [']', '}']:
                if char == ']' and stack and stack[-1] == '[':
                    stack.pop()
                elif char == '}' and stack and stack[-1] == '{':
                    stack.pop()
                temp_arg += char
            elif char == ',' and not stack and not in_string:
                args.append(temp_arg.strip())
                temp_arg = ''
            else:
                temp_arg += char

        if temp_arg:
            args.append(temp_arg.strip())

        # Convert string representations of lists and dictionaries to actual lists and dictionaries
        for i, arg in enumerate(args):
            try:
                args[i] = json.loads(arg)
            except json.JSONDecodeError:
                pass

        return args

    def replace_match(match):
        func = match.group(1)
        args_str = match.group(2)
        try:
            func = importlib.import_module(f"resources.functions.{func}")
            args = split_args(args_str)

            processed_args = []
            for arg in args:
                if arg.startswith(("'", '"')) and arg.endswith(("'", '"')):
                    arg = arg[1:-1].replace('\\"', '"').replace("\\'", "'")
                else:
                    try:
                        arg = int(arg) if arg.isdigit() else arg
                    except ValueError:
                        pass
                processed_args.append(arg)
                print(processed_args)
            result = func.main(*processed_args)
            return str(result)
        except (AttributeError, ModuleNotFoundError) as e:
            return match.group(0)

    result = re.sub(pattern, lambda match: str(replace_match(match)), value)

    if result.isdigit():
        return int(result)
    else:
        return result
