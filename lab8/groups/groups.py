def groups_of_3(lst, n):
        return [lst[i:i+n] for i in range(0, len(lst), n)]
