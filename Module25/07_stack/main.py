class Stack:
    def __init__(self):
        self.__stacks = []

    def __str__(self):
        if len(self.__stacks) == 0:
            return "{}".format(None)
        return "{}".format(self.__stacks)

    def pop(self):
        self.__stacks = self.__stacks[:len(self.__stacks) - 1]
        return self.__stacks

    def add(self, file):
        self.__stacks.append(file)


test = Stack()
test.pop()
print(test)
test.add(5)
test.add(7)
test.add(5)
print(test)
test.pop()
print(test)


class TaskManager:
    def __init__(self):
        self.__stack = dict()

    def new_task(self, task, task_priority):
        if task_priority not in self.__stack:
            self.__stack[task_priority] = " {}".format(task)
        else:
            self.__stack[task_priority] += "; {}".format(task)

    def __str__(self):
        print("Результат:")
        return "{}".format(self.__get_stack())

    def __get_stack(self):
        result = ""
        for key in sorted(self.__stack.keys()):
            for priority, task in self.__stack.items():
                if key == priority:
                    text = "{} {}\n".format(key, task)
                    result += text
        return result


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)

print(manager)

# зачет!
