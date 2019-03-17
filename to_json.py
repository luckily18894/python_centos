
import json
from dateutil import parser
from datetime import timedelta

# 原数据，格式有误
test_str_source = "{'姓名': '秦柯', '年龄': 39, '出生日期': '1979-05-05', '状态': true}"
# 修改后格式正确（手动）
test_str = '{"姓名": "秦柯", "年龄": 39, "出生日期": "1979-05-05", "状态": true}'

test_dict = json.loads(test_str)
print(test_dict)

test_dict['出生日期'] = (parser.parse(test_dict['出生日期']) + timedelta(days=365 * 10)).strftime('%Y-%m-%d')
print(test_dict)

with open('json_test.json', 'w', encoding='utf-8') as f:
    json.dump(test_dict, f, ensure_ascii=False)

with open('json_test.json', 'r', encoding='utf-8') as f:
    test_dict_read = json.load(f)

print(test_dict_read)

