#!/usr/bin/env python3
import json


def generate_diff(sorce, sorce2):

    data1 = json.load(open(f'./tests/fixtures/{sorce}'))
    data2 = json.load(open(f'./tests/fixtures/{sorce2}'))

    result = {(key, value) for key, value in data1.items()}
    result2 = {(key, value) for key, value in data2.items()}
    result3 = sorted(list(result | result2))
    check = []

    for key, _ in result3:
        if key in data1.keys() and key in data2.keys():
            if data1[key] == data2[key]:
                check.append(f' {key}: {data1[key]}')
            else:
                check.append(f'-{key}: {data1[key]}')
                check.append(f'+{key}: {data2[key]}')
        else:
            if key in data1.keys():
                check.append(f'-{key}: {data1[key]}')
            else:
                check.append(f'+{key}: {data2[key]}')

    new_check = sorted(set(check), key=lambda index: check.index(index))
    final = '\n'.join(new_check)

    return final
