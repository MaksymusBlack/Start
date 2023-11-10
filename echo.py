import sys


def parse_args():
    
    list_of_argv = []
    result = ""
    
    for i in sys.argv:
        if i != sys.argv[0]:
            list_of_argv.append(i)
         
    result = ' '.join(list_of_argv)
    print(result)
    return result

parse_args()


