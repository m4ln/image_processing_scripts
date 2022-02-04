
def get_file_name(file_path):

    import ntpath
    if isinstance(file_path, list):
        tail = []
        for i in range(0,len(file_path)):
            t_head, t_tail = ntpath.split(file_path[i])
            tail.append(t_tail)
    else:
        head, tail = ntpath.split(file_path)

    return tail
