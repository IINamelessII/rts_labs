"""RTS labs"""

from time import time


def log(filename):
    def log_decorator(func):
        def log_wrapper(*args, **kwargs):
            start = time()
            result = func(*args, **kwargs)
            stop = time()

            with open(filename, 'w') as fh:
                fh.write(f'Execution time: {((stop - start) * 1000):.3f} s\n')

                if isinstance(result, list):  # only iterable option for the project
                    res = '\n'.join('Result[{}]: {:.3f}'.format(i, v) for i, v in enumerate(result))
                else:
                    res = f'Result: {result:.5f}'
                
                fh.write(res)

            return result
        return log_wrapper
    return log_decorator
