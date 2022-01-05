import json, os, uuid


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

def add_post(filename, post):
    data = read_json(filename)
    data.append(post)
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4, sort_keys=True)

def replay_files_name(filename):
    files = os.listdir(path="uploads/images")
    filename = f'{str(uuid.uuid4())}.png'
    return filename


