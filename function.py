def get_unique_file_name(file_name):
    import os
    '''避免重名'''
    if not os.path.isfile(file_name):
        return file_name
    else:
        base_name, ext = os.path.splitext(file_name)
        counter = 1
        while True:
            numbered_file_name = f"{base_name}_{counter}{ext}"
            if not os.path.isfile(numbered_file_name):
                return numbered_file_name
            counter += 1

def get_unique_dir_name(dir_name):
    import os
    root = './output'
    '''避免重名'''
    if not os.path.isdir(os.path.join(root, dir_name)):
        return dir_name
    else:
        counter = 1
        while True:
            numbered_dir_name = f"{dir_name}_{counter}"
            if not os.path.isdir(os.path.join(root, numbered_dir_name)):
                return numbered_dir_name
            counter += 1
