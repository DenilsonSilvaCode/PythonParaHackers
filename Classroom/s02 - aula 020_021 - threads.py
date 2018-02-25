import _thread, time

# sequencia de fibonacci ex.: 1, 1, 2, 3, 5, 8, 13 ...

def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)

def test_fib(n):
    print('Fib %d: %d' % (n, fib(n)))

def run_fibs():
    test_fib(35)
    test_fib(10)
    test_fib(30)

def run_fibs_with_threads():
    _theread.start_new_thread(test_fib, (35,))
    _theread.start_new_thread(test_fib, (35,))
    _theread.start_new_thread(test_fib, (35,))
    time.sleep(12)

#run_fibs()
run_fibs_with_threads()