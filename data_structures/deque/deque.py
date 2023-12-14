class Deque():
    def __init__(self):
        self.data = []

    def push_front(self, elem):
        temp = [elem]
        temp.extend(iter(self.data))
        self.data = temp

    def push_back(self, elem):
        self.data.append(elem)

    def pop_front(self):
        temp = [self.data[i] for i in range(0, len(self.data)) if i != 0]
        self.data = temp
    
    def pop_back(self):
        temp = [
            self.data[i]
            for i in range(0, len(self.data))
            if i != len(self.data) - 1
        ]
        self.data = temp

    def get_first(self):
        return self.data[0] if (len(self.data)>0) else "Deque is empty"

    def get_last(self):
        if(len(self.data)>0):
            return self.data[len(self.data)-1]
        else:
            return "Deque is empty"

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return len(self.data) == 0

    def contains(self, elem):
        return any(i==elem for i in self.data)

    def printElems(self):
        result = "".join(f"{str(i)} | " for i in self.data)
        print(result)