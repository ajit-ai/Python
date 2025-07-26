from collections import defaultdict
import heapq

class Node:
    def __init__(self, frequency=0, sign=None, left=None, right=None):
        self.frequency = frequency
        self.sign = sign
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.frequency < other.frequency

    def __repr__(self):
        return f"<ch: {self.sign}, freq: {self.frequency}>"

class HuffmanReader:
    def __init__(self, file):
        self.file = file
        self.buffer = []

    def get_bit(self):
        """Read a single bit from the file."""
        if not self.buffer:
            byte = self.file.read(1)
            if not byte:
                return None
            self.buffer.extend(list(f"{int.from_bytes(byte, 'big'):08b}"))
        return self.buffer.pop(0)

    def get_byte(self):
        """Read 8 bits as a byte."""
        bits = []
        for _ in range(8):
            bit = self.get_bit()
            if bit is None:
                return None
            bits.append(bit)
        return "".join(bits)

    def get_number_of_additional_bits(self):
        """Read the first 3 bits to get the number of additional bits in the last byte."""
        bits = []
        for _ in range(3):
            bit = self.get_bit()
            if bit is None:
                raise ValueError("Invalid file format: missing additional bits info")
            bits.append(bit)
        return int("".join(bits), 2)

    def load_tree(self):
        """Load the Huffman tree from the file."""
        def load_node():
            bit = self.get_bit()
            if bit is None:
                raise ValueError("Invalid file format: incomplete tree")
            if bit == "1":  # Leaf node
                byte = self.get_byte()
                if byte is None:
                    raise ValueError("Invalid file format: missing character")
                return Node(sign=int(byte, 2))
            node = Node()
            node.left = load_node()
            node.right = load_node()
            return node
        return load_node()

class HuffmanWriter:
    def __init__(self, file):
        self.file = file
        self.buffer = ""
        self.saved_bits = 0

    def write_bits(self, bits):
        """Write bits to the file."""
        self.buffer += bits
        self.saved_bits += len(bits)
        while len(self.buffer) >= 8:
            byte = int(self.buffer[:8], 2)
            self.file.write(bytes([byte]))
            self.buffer = self.buffer[8:]

    def write_int(self, num):
        """Write an 8-bit integer."""
        self.write_bits(f"{num:08b}")

    def save_tree(self, tree):
        """Save the Huffman tree to the file."""
        def save_node(node):
            if node.sign is not None:
                self.write_bits("1")
                self.write_int(node.sign)
            else:
                self.write_bits("0")
                save_node(node.left)
                save_node(node.right)
        save_node(tree)

    def reserve_additional_bits(self):
        """Reserve 3 bits for additional bits info."""
        self.write_bits("000")

    def set_additional_bits(self, additional_bits):
        """Set the first 3 bits to indicate additional bits in the last byte."""
        self.file.seek(0)
        first_byte = self.file.read(1)
        if not first_byte:
            raise ValueError("File is empty")
        first_byte = f"{int.from_bytes(first_byte, 'big'):08b}"
        first_byte = f"{additional_bits:03b}{first_byte[3:]}"
        self.file.seek(0)
        self.file.write(bytes([int(first_byte, 2)]))

    def close(self):
        """Flush remaining bits, padding with zeros if necessary."""
        if self.buffer:
            additional_bits = 8 - len(self.buffer)
            self.write_bits("0" * additional_bits)
            self.set_additional_bits(additional_bits)
        self.file.flush()

class HuffmanCoding:
    @staticmethod
    def encode_file(file_in_name, file_out_name):
        """Encode a file using Huffman coding."""
        try:
            with open(file_in_name, "rb") as file_in, open(file_out_name, "wb") as file_out:
                signs_frequency = HuffmanCoding._get_char_frequency(file_in)
                if not signs_frequency:
                    print("Input file is empty. No encoding performed.")
                    return
                file_in.seek(0)
                tree = HuffmanCoding._create_tree(signs_frequency)
                codes = HuffmanCoding._generate_codes(tree)
                writer = HuffmanWriter(file_out)
                writer.reserve_additional_bits()
                writer.save_tree(tree)
                HuffmanCoding._encode_and_write_signs_to_file(file_in, writer, codes)
                writer.close()
            print(f"File encoded: {file_in_name} -> {file_out_name}")
        except FileNotFoundError:
            print(f"Error: Input file '{file_in_name}' not found.")
        except Exception as e:
            print(f"Error during encoding: {str(e)}")

    @staticmethod
    def decode_file(file_in_name, file_out_name):
        """Decode a Huffman-coded file."""
        try:
            with open(file_in_name, "rb") as file_in, open(file_out_name, "wb") as file_out:
                reader = HuffmanReader(file_in)
                additional_bits = reader.get_number_of_additional_bits()
                tree = reader.load_tree()
                HuffmanCoding._decode_and_write_signs_to_file(file_out, reader, tree, additional_bits)
            print(f"File decoded: {file_in_name} -> {file_out_name}")
        except FileNotFoundError:
            print(f"Error: Input file '{file_in_name}' not found.")
        except Exception as e:
            print(f"Error during decoding: {str(e)}")

    @staticmethod
    def _get_char_frequency(file):
        """Calculate frequency of each character in the file."""
        signs_frequency = defaultdict(int)
        while True:
            sign = file.read(1)
            if not sign:
                break
            signs_frequency[int.from_bytes(sign, "big")] += 1
        return signs_frequency

    @staticmethod
    def _create_tree(signs_frequency):
        """Create a Huffman tree from character frequencies."""
        if not signs_frequency:
            return None
        nodes = [Node(frequency=freq, sign=char) for char, freq in signs_frequency.items()]
        heapq.heapify(nodes)
        if len(nodes) == 1:
            return Node(frequency=nodes[0].frequency, left=nodes[0])
        while len(nodes) > 1:
            left = heapq.heappop(nodes)
            right = heapq.heappop(nodes)
            parent = Node(frequency=left.frequency + right.frequency, left=left, right=right)
            heapq.heappush(nodes, parent)
        return nodes[0]

    @staticmethod
    def _generate_codes(tree):
        """Generate Huffman codes for each character."""
        if not tree:
            return {}
        codes = {}
        def generate(node, code):
            if node.sign is not None:
                codes[node.sign] = code or "0"
            if node.left:
                generate(node.left, code + "0")
            if node.right:
                generate(node.right, code + "1")
        generate(tree, "")
        return codes

    @staticmethod
    def _encode_and_write_signs_to_file(file, writer, codes):
        """Encode and write file contents using Huffman codes."""
        while True:
            sign = file.read(1)
            if not sign:
                break
            writer.write_bits(codes[int.from_bytes(sign, "big")])

    @staticmethod
    def _decode_and_write_signs_to_file(file, reader, tree, additional_bits):
        """Decode and write signs to the output file."""
        if not tree:
            return
        current = tree
        bits_processed = 0
        total_bits = 0
        file.seek(0, 2)
        total_bytes = file.tell()
        file.seek(0)
        while True:
            bit = reader.get_bit()
            if bit is None:
                break
            total_bits += 1
            if total_bits > 8 * total_bytes - additional_bits:
                continue
            if bit == "0" and current.left:
                current = current.left
            elif bit == "1" and current.right:
                current = current.right
            if current.sign is not None:
                file.write(bytes([current.sign]))
                current = tree

if __name__ == '__main__':
    # Example usage: Ensure input.txt exists or create a sample one
    try:
        with open("input.txt", "w") as f:
            f.write("Hello, Huffman coding!")
        HuffmanCoding.encode_file("input.txt", "output.bin")
        HuffmanCoding.decode_file("output.bin", "output_decoded.txt")
        # Read and print decoded file to verify
        with open("output_decoded.txt", "r") as f:
            print("Decoded content:", f.read())
    except Exception as e:
        print(f"Error in main: {str(e)}")



#call main method
if __name__ == '__main__':
    pass
