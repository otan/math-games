import random
import time
import sys

assert len(sys.argv) == 3, "Usage: {} <seed> <num_secs>".format(sys.argv[0])

random.seed(int(sys.argv[1]))

num_correct = 0
correct = []
incorrect = []
num_secs = int(sys.argv[2])

t = time.time()
while time.time() - t < num_secs:
    side_a = random.randint(1, 20)
    side_b = random.randint(1, 20)
    operator = random.choice(['+', '-', '*'])
    sys.stdout.write('{} s left: {} {} {} = '.format(round(num_secs - (time.time() - t), 2), side_a, operator, side_b))
    read_line = sys.stdin.readline()
    while True:
        if time.time() - t > num_secs:
            print 'time exceeded!'
            break
        try:
            answer = int(read_line.strip())
        except:
            print 'Invalid number!'
            sys.stdout.write('{} s left: {} {} {} = '.format(round(num_secs - (time.time() - t), 2), side_a, operator, side_b))
            read_line = sys.stdin.readline()
            continue
        correct_answer = eval('{} {} {}'.format(side_a, operator, side_b))
        answer_str = '{} {} {} = {}'.format(side_a, operator, side_b, answer)
        if answer == correct_answer:
            correct.append(answer_str)
        else:
            incorrect.append(answer_str)
        break

print '--------------'
print 'Got {}/{}'.format(len(correct), len(correct) + len(incorrect))
print 'Correct: \n{}'.format('\n'.join(correct))
print 'Incorrect: \n{}'.format('\n'.join(incorrect))
