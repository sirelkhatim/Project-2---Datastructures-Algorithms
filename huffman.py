import sys

class HuffmanNode:
    """
    class to abstract a huffman node with value and weight
    """
    def __init__(self, value=None, weight=None):
        self.value = value
        self.weight = weight
        self.left = None
        self.right = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_left_child(self, left):
        self.left = left

    def set_right_child(self, right):
        self.right = right

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None

    def __lt__(self, other):
        return self.weight < other.weight

    def __le__(self, other):
        return self.weight <= other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __ge__(self, other):
        return self.weight >= other.weight


def get_frequencies(data):
    chrs = list(data)
    count_dict = {}
    for chr_ in chrs:
        if chr_ not in count_dict:
            count_dict[chr_] = 1
        else:
            count_dict[chr_] += 1
    counter = sorted(zip(count_dict.values(), count_dict.keys()))
    for i in range(len(counter)):
        counter[i] = HuffmanNode(counter[i][1], counter[i][0])

    return counter

def huffman_tree(data):
    heap = get_frequencies(data)
    heapq.heapify(heap)
    while len(heap)!= 1:
        Z = HuffmanNode()
        Z.left = x = heapq.heappop(heap)
        Z.right = y = heapq.heappop(heap)
        Z.weight = x.weight + y.weight
        heapq.heappush(heap,Z)
    return heap



def create_Huffcode_table(root):
    code = {}
    def create_code(node, current = ""):
        if not node:
            return
        if not node.has_left_child() and not node.has_right_child():
            code[node.value] = current
        create_code(node.get_left_child(), current + "0")
        create_code(node.get_right_child(), current + "1")

    create_code(root[0])
    print(code)
    return code

def huff_encode(data):
    if (len(get_frequencies(data))) == 1:
        return "0"*len(data)

    huff_code = ""
    root = huffman_tree(data)
    table = create_Huffcode_table(root)
    print(table)
    for item in data:
        huff_code += table[item]
    return huff_code

def huffman_encoding(data):

    return huff_encode(data), huffman_tree(data)


def huffman_decoding(data,tree):
    if (len(get_frequencies(data))) == 1:
        return len(data)*str(tree.value)
    decode = ''
    n = len(data)
    count = 0
    while count < n:
        current = tree[0]
        while not current.get_left_child() and not current.get_right_child():
            if data[count] == "0":
                current = current.get_left_child()
            elif data[count] == "1":
                current = current.get_right_child()

            count += 1

        decode += current.value
    return decode




if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))