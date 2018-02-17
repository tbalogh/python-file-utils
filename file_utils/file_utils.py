import os, json, codecs


def replace_extension(path, new_extension):
    if not path:
        return ''
    return os.path.splitext(path)[0] + "." + new_extension.lstrip('.')


def files_ends_with_filter(ends_with):
    return lambda f: f.endswith(ends_with)


def collect_files(root_path, filter_method):
    for dir_path, dir_names, file_names in os.walk(root_path):
        for file_name in list(filter(filter_method, file_names)):
            yield os.path.join(dir_path, file_name)


def files_ends_with(root_path, ends_with):
    return collect_files(root_path, files_ends_with_filter(ends_with))


def read(path):
    with codecs.open(path, 'r', encoding='utf8') as f:
        text = f.read()
    return text


def read_lines(path):
    with codecs.open(path, 'r', encoding='utf8') as f:
        lines = f.readlines()
    lines = [x.strip() for x in lines]
    return lines


def read_json_by_key(path, key):
    return read_json(path)[key]


def read_json(path):
    with codecs.open(path, 'r', encoding='utf8') as f:
        json_content = json.load(f)

    return json_content


def save_json(dictionary, path):
    json_content = json.dumps(dictionary, indent=4, sort_keys=True, ensure_ascii=False)
    save(json_content, path)


def save(content, path):
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    with codecs.open(path, "w+", encoding='utf8') as f:
        f.write(content)


def append(content, path):
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    with codecs.open(path, "a+", encoding='utf8') as f:
        f.write(content)
