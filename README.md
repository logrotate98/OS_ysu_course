OS_ysu_course
# Github repo for Operating Systems university course

=============================================================

Task 1: Producer-consumer problem

The producer-consumer problem arises when a process is producing some data, the producer, and another process is using that data, the consumer. The producer and the consumer, however, could be operating at different rates, ie the consumer could be using data quicker than the producer can produce it. To support this we need to offer a queue structure for the producer to place data onto and the consumer to take from and also a count of how many items exist on the queue, so producers cannot place too much data on the queue and consumers do not try and take data that is not there.

=============================================================

Task 2: Dining philosophers problem

There are five philosophers sitting around a circular dining table.
The dining table has five forks and a bowl of food in the middle.
At any instant, a philosopher is either eating or thinking.
When a philosopher wants to eat, he uses two forks - one from their left and one from their right.
When a philosopher wants to think, he keeps down both forks at their original place.
Eating is not limited by the remaining amounts of food;

Solution directory: dining_philosophers_task

