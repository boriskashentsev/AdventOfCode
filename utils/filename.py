def calculateFileName(args):
    ''' Expects args[0] have format 'aaaa/bbbb.cc.py' or '.\aaaa\bbbb.cc.py' '''
    filename =''
    names = []
    if '/' in args[0]:
        names = args[0].split('/')
    else:
        names = args[0].split('\\')
    parts = names[-1].split('.')
    test = ''
    if len(args) > 1:
        test = '.' + args[1]
    filename += names[-2] + '/' + parts[1] + test + '.input'
    return filename