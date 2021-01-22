'''
队列的应用--击鼓传花大逃杀
题目描述

你和你的 39 个同学外出露营，晚上无聊时，大家围在火堆边做游戏。游戏规则如下：40人围成一个圈，其中一人被指定为第一个人，顺时针报数到第七人，就将他杀死。之后，下一个活着的人继续报数，每次都是杀死第七个人。直到只剩一人时，游戏结束。如果你并不想死，那么应该坐到哪里才能成为最后一人？（假设第一个报数者的位置记为1）
解题思路

如果能想到将这个问题抽象为一个简单队列的问题，那么就已经解决了一大半。

    报数而不被杀的人：相当于从队首出队再从队尾入队；
    被杀的人：只出队；
    留到最后的人：当队列长度为1时，再出队一次，返回。

'''

class Queue(object):
    """队列"""
    def __init__(self, maxsize=0):
        """maxsize<=0代表队列不限定大小"""
        self.queue = []
        self.maxsize = maxsize

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        if self.maxsize <= 0:
            return False
        else:
            return len(self.queue) == self.maxsize

    def enqueue(self, item):
        """入队"""
        if self.is_full():
            raise Exception("Queue is full!")
        else:
            self.queue.append(item)

    def dequeue(self):
        """出队"""
        if self.is_empty():
            raise IndexError("Queue is empty!")
        else:
            return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def get_front(self):
        """返回队头元素"""
        if self.is_empty():
            raise IndexError("Queue is empty!")
        else:
            return self.queue[0]

    def get_rear(self):
        """返回队尾元素"""
        if self.is_empty():
            raise IndexError("Queue is empty!")
        else:
            return self.queue[-1]

    def print_queue(self):
        return self.queue


class CircleQueue(object):
    """循环队列"""
    def __init__(self, capacity):
        """capacity是队列大小，但实际大小为capacity-1，由于尾指针浪费了一个位置"""
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front, self.rear = 0, 0

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        # 1.front=rear+1；2.front=0，rear=capacity-1
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, item):
        if self.is_full():
            raise Exception("Queue is full!")
        else:
            self.queue[self.rear] = item
            self.rear = (self.rear + 1) % self.capacity

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty!")
        else:
            tmp = self.queue[self.front]
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.capacity
            return tmp

    def size(self):
        return (self.rear - self.front + self.capacity) % self.capacity

    def get_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty!")
        else:
            return self.queue[self.front]

    def get_rear(self):
        if self.is_empty():
            raise IndexError("Queue is empty!")
        else:
            return self.queue[(self.rear - 1 + self.capacity) % self.capacity]

    def print_queue(self):
        tmp = self.front
        ls = []
        while tmp != self.rear:
            ls.append(self.queue[tmp])
            tmp = (tmp + 1) % self.capacity
        return ls

# def test_Q():
#     Q = Queue()
#     print("队列是否为空：", Q.is_empty())
#     print("入队'1'")
#     Q.enqueue(1)
#     print("队列大小：", Q.size())
#     print("入队'2'")
#     Q.enqueue(2)
#     print("队头元素：", Q.get_front())
#     print("出队：", Q.dequeue())
#     print("队头元素：", Q.get_front())
#     # print("出队：", Q.dequeue())
#     print("队尾元素：", Q.get_rear())
#     print("队列为：", Q.print_queue())
#
# def test_CQ():
#     CQ = CircleQueue(4)
#     print("循环队列是否为空：", CQ.is_empty())
#     print("入队'1'")
#     CQ.enqueue(1)
#     print("入队'2'")
#     CQ.enqueue(2)
#     print("队头元素：", CQ.get_front())
#     print("入队'3'")
#     CQ.enqueue(3)
#     print("循环队列是否为满：", CQ.is_full())
#     print("出队：", CQ.dequeue())
#     print("队尾元素：", CQ.get_rear())
#     print("循环队列为：", CQ.print_queue())



def dataosha(name_list, kill_num=7):
    """击鼓传花大逃杀"""
    Q = Queue()
    for name in name_list:
        Q.enqueue(name)
    while Q.size() > 1:
        for _ in range(kill_num - 1):  # 这里没有用到_，只是为了循环而已
            Q.enqueue(Q.dequeue())
        print("Kill:", Q.dequeue())
    return Q.dequeue()


name_list = []
for i in range(4000):
    name_list.append(i + 1)
print("Safe number:", dataosha(name_list))



