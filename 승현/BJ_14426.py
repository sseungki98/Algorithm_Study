class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    # 문자열 삽입
    def insert(self, string):
        curr_node = self.head
        # 삽입할 string 각각의 문자에 대해 자식 Node를 만들며 내려간다.
        for char in string:
            # 자식 Node들 중 같은 문자가 없으면 Node 새로 생성
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            # 같은 문자가 있으면 노드를 따로 생성하지 않고, 해당 노드로 이동
            curr_node = curr_node.children[char]
        # 문자열이 끝난 지점의 노드의 data값에 해당 문자열을 입력
        curr_node.data = string

    # 문자열이 존재하는지 search
    def search(self, string):
        # 가장 아래에 있는 노드에서 부터 탐색 시작
        curr_node = self.head
        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False
        # 탐색이 끝난 후 해당 노드의 data값이 존재한다면
        # 문자가 포함되어있다는 뜻이다.
        if curr_node.data != None:
            return True


n, m = map(int, input().split())
count = 0
trie = Trie()
for i in range(n):
    trie.insert(input())


for i in range(m):
    test = input()
    print(test)
    if trie.search(test):
        count += 1

print(count)
