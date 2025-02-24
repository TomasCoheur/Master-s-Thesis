import json

def compare_json(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        json1 = json.load(f1)
        json2 = json.load(f2)

    diff = {}

    # Find keys present in file1 but not in file2
    for key in json1:
        if key not in json2:
            diff[key] = {'in_file1': json1[key], 'in_file2': None}
        elif json1[key] != json2[key]:
            diff[key] = {'in_file1': json1[key], 'in_file2': json2[key]}

    # Find keys present in file2 but not in file1
    for key in json2:
        if key not in json1:
            diff[key] = {'in_file1': None, 'in_file2': json2[key]}

    return diff

def print_diff(diff):
    print("Differences between the JSON files:")
    for key, value in diff.items():
        print(f"Key: {key}")
        if value['in_file1'] is not None:
            print(f"    Value in file 1: {value['in_file1']}")
        if value['in_file2'] is not None:
            print(f"    Value in file 2: {value['in_file2']}")

if __name__ == "__main__":
    file1 = input("Enter the path to the first JSON file: ")
    file2 = input("Enter the path to the second JSON file: ")

    diff = compare_json(file1, file2)
    print_diff(diff)
