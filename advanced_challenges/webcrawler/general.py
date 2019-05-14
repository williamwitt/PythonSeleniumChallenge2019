import os


# Each website is a separate project (folder)
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating project ' + directory)
        os.mkdir(directory)


# Create que and crawled files if not created
def create_data_files(project_name, base_url):
    queue = os.path.join(project_name, 'queue.txt')
    crawled = os.path.join(project_name, 'crawled.txt')
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


# Create a new file
def write_file(path, data):
    with open(path, 'w') as file:
        file.write(data)


# Add data to an existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')


# Delete the contents of file
def delete_file_contents(path):
    open(path, 'w').close()


# Read a file and convert each line to items in set
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results


# Iterate through a set, each item will be a new line in file
def set_to_file(links, file_name):
    with open(file_name, 'w') as f:
        for l in sorted(links):
            f.write(l + '\n')


