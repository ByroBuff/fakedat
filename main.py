import json
from resources.utils import construct_value
import argparse


def reconstruct_dict_recursively(data, separator, iter_variables, static_variables, is_nested=False):
    new_dict = {}
    if isinstance(data, dict):
        if "_repeat" in data and "template" in data:
            repeat_count = data["_repeat"]
            template = data["template"]
            result_list = []
            for _ in range(repeat_count):
                if not is_nested:  # Only evaluate iter_variables if not in a nested iteration
                    evaluated_iter_variables = {
                        var: construct_value(value, separator, {**static_variables, **iter_variables})
                        for var, value in iter_variables.items()
                    }
                else:  # Use iter_variables as is if in a nested iteration
                    evaluated_iter_variables = iter_variables
                combined_variables = {**static_variables, **evaluated_iter_variables}
                if isinstance(template, str):
                    result_list.append(
                        construct_value(template, separator, combined_variables)
                    )
                else:
                    result_list.append(
                        reconstruct_dict_recursively(
                            template, separator, evaluated_iter_variables, combined_variables, is_nested=True
                        )
                    )
            return result_list
        else:
            for key, value in data.items():
                if isinstance(value, dict) or isinstance(value, list):
                    new_dict[construct_value(key, separator, static_variables)] = reconstruct_dict_recursively(
                        value, separator, iter_variables, static_variables, is_nested=False
                    )
                else:
                    new_dict[construct_value(key, separator, static_variables)] = construct_value(value, separator, static_variables)
    elif isinstance(data, list):
        return [reconstruct_dict_recursively(item, separator, iter_variables, static_variables, is_nested=False) for item in data]
    else:
        return construct_value(data, separator, static_variables)
    return new_dict



if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Detailed JSON data generator with dynamic and static variables"
    )
    parser.add_argument(
        "-i", "--input", help="Input file name", type=str, default="input.json"
    )
    parser.add_argument(
        "-o", "--output", help="Output file name", type=str, default="output.json"
    )
    parser.add_argument("-s", "--separator", help="Separator", type=str, default="|")

    args = parser.parse_args()

    with open(args.input, "r") as f:
        json_data = json.load(f)

    iter_variables = json_data.get("_iter_variables", {})
    static_variables = json_data.get("_static_variables", {})
    evaluated_static_variables = {
        var: construct_value(value, args.separator, static_variables)
        for var, value in static_variables.items()
    }

    new_json_data = reconstruct_dict_recursively(
        json_data, args.separator, iter_variables, evaluated_static_variables
    )

    with open(args.output, "w") as f:
        json.dump(new_json_data, f, indent=4)
