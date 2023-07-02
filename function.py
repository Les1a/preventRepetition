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
