def stringInsert(where, what, position):
    where = where[:position] + what + where[position+len(what):]
    return where