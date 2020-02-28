import sys
import heapq

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
    if root is None:
        return None
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
    for item in data:
        huff_code += table[item]
    return huff_code

def huffman_encoding(data):
    if len(data)== 0:
        return None,{}
    return huff_encode(data), huffman_tree(data)


def huffman_decoding(data,tree):
    if data is None:
        return ''
    if (len(get_frequencies(data))) == 1:
        return len(data)*str(tree[0].value)

    decode = ''
    n = len(data)
    count = 0
    while count < n:
        current = tree[0]
        while current.get_left_child() and current.get_right_child():
            if data[count] == "0":
                current = current.get_left_child()
            elif data[count] == "1":
                current = current.get_right_child()

            count += 1

        decode += str(current.value)
    return decode




if __name__ == "__main__":

    # Test 1
    print('Test 1...')
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


    '''
    table should be : {'T': '0000', 't': '0001', 'h': '001', 'd': '010', 'r': '011', 'w': '1000', 'o': '1001', 'b': '1010', 's': '1011', ' ': '110', 'e': '1110', 'i': '1111'}
    solution for encoding is 0000001111011010101111011010110111110111100001001111011010001001011010
    '''
    # Test 2

    print('Test 2...')

    a_great_sentence = "Another message"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    '''
    table should be: {'e': '00', 'o': '0100', 'g': '0101', ' ': '0110', 'm': '0111', 's': '100', 'n': '1010', 'a': '1011', 'A': '1100', 'r': '1101', 't': '1110', 'h': '1111'}
    solution for encoding is 1100101001001110111100110101100111001001001011010100
    '''

    # Test 3
    print('Test 3...')

    a_great_sentence = ""

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    #print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    '''
    solution should just be blank as there is nothing to encode
    '''

    # Test 3
    print('Test 4...')

    a_great_sentence = "AAAAAAA"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    #print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    '''
    expected result:
    Test 4...
    The size of the data is: 56

    The content of the data is: AAAAAAA

    The content of the encoded data is: 0000000

    The size of the decoded data is: 56

    The content of the encoded data is: AAAAAAA

    '''