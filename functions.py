import json


def read_json(filename):
    with open(filename, encoding='utf-8') as f:
        return json.load(f)

def get_tags(data):
    result = set()

    for i in data:
        content = i['content']
        words = content.split()
        for word in words:
            if word.startswith('#'):
                result.add(word.lstrip('#'))
    return result

def get_posts_tag(data, tag):
    result = []
    for i in data:
        if f'#{tag}' in i['content']:
            result.append(i)
    return result