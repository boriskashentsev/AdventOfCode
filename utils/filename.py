def calculateFileName(args):
    ''' Expects args[0] have format 'xxxx/yyyy.zz.py' '''
    filename =''
    names = args[0].split('/')
    parts = names[1].split('.')
    test = ''
    if len(args) > 1:
        test = '.' + args[1]
    filename += names[0] + '/' + parts[1] + test + '.input'
    return filename