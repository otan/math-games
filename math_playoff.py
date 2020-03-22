import random
import time
import sys

assert len(sys.argv) == 3, "Usage: {} <seed> <num_questions>".format(sys.argv[0])

random.seed(int(sys.argv[1]))

num_correct = 0
t = time.time()
correct = []
incorrect = []
total = int(sys.argv[2])

for i in xrange(total):
    side_a = random.randint(1, 20)
    side_b = random.randint(1, 20)
    operator = random.choice(['+', '-', '*'])
    sys.stdout.write('{} {} {} = '.format(side_a, operator, side_b))
    read_line = sys.stdin.readline()
    while True:
        try:
            answer = int(read_line.strip())
        except:
            print 'Invalid number!'
            sys.stdout.write('{} {} {} = '.format(side_a, operator, side_b))
            read_line = sys.stdin.readline()
            continue
        correct_answer = eval('{} {} {}'.format(side_a, operator, side_b))
        answer_str = '{} {} {} = {}'.format(side_a, operator, side_b, answer)
        if answer == correct_answer:
            correct.append(answer_str)
        else:
            incorrect.append(answer_str)
        break

stop = time.time() - t
print '--------------'
print 'Got {}/{} in {}s'.format(len(correct), total, stop)
print 'Correct: \n{}'.format('\n'.join(correct))
print 'Incorrect: \n{}'.format('\n'.join(incorrect))
