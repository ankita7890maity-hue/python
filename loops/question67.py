
import data


result = []
for item in data:
    if isinstance(item, list):
        for sub_item in item:
            if isinstance(sub_item, list):
                result.extend(sub_item)
            else:
                if sub_item % 2 == 0:
                    result.append(sub_item * 2)
                else:
                    continue
    else:
        if item > 5:
            result.append(item)
print(result)