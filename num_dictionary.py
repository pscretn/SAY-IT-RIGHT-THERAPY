import json
nums = json.load(open('json_file/numbers.json'))

def num_dict(number):
    return nums.get(number)