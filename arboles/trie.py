class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False  # Flag to mark the end of a word
        self.data = None  # Optional: could store additional data associated with the word

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word, data=None):
        """Insert a word into the trie, with optional associated data."""
        current = self.root
        for char in word:
            # Create a new node if the path doesn't exist
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        
        # Mark the end of a word
        current.is_end_of_word = True
        # Store data if provided
        if data is not None:
            current.data = data
    
    def search(self, word):
        """
        Search for a word in the trie.
        Returns True if the word exists, False otherwise.
        """
        current = self.root
        for char in word:
            # If the character path doesn't exist, the word doesn't exist
            if char not in current.children:
                return False
            current = current.children[char]
        
        # The word exists only if we've reached a node marked as end of word
        return current.is_end_of_word
    
    def starts_with(self, prefix):
        """
        Check if any word in the trie starts with the given prefix.
        Returns True if there is at least one word with the prefix, False otherwise.
        """
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        
        # If we've traversed the entire prefix, it exists in the trie
        return True
    
    def get_words_with_prefix(self, prefix):
        """
        Find all words that start with the given prefix.
        Returns a list of words.
        """
        results = []
        current = self.root
        
        # Navigate to the node corresponding to the prefix
        for char in prefix:
            if char not in current.children:
                return results  # No words with this prefix
            current = current.children[char]
        
        # Use a helper function to collect all words from this node
        self._collect_words(current, prefix, results)
        return results
    
    def _collect_words(self, node, prefix, results):
        """Helper function to recursively collect all words from a given node."""
        if node.is_end_of_word:
            results.append(prefix)
        
        for char, child_node in node.children.items():
            self._collect_words(child_node, prefix + char, results)


#-------------------------------------
# Example usage of the Trie class
#-------------------------------------
def autocomplete(trie, prefix, max_suggestions=5):
    """Return up to max_suggestions words that start with the given prefix."""
    suggestions = trie.get_words_with_prefix(prefix)
    return suggestions[:max_suggestions]

# Create and populate a trie
word_trie = Trie()
words = ["apple", "application", "apartment", "appetizer", "append", "banana", "bat", "bath", "bet"]
for word in words:
    word_trie.insert(word)

#-------------------------------------
# Get autocomplete suggestions
prefix = "ap"
suggestions = autocomplete(word_trie, prefix)
print(f"Autocomplete suggestions for '{prefix}': {suggestions}")
# Output: Autocomplete suggestions for 'ap': ['apple', 'application', 'apartment', 'appetizer', 'append']

def spell_check(trie, word):
    """Check if a word exists in the dictionary (trie)."""
    return trie.search(word)

# Create a dictionary trie
dictionary = Trie()
valid_words = ["hello", "world", "programming", "python", "algorithm", "data", "structure"]
for word in valid_words:
    dictionary.insert(word)

# Check if words exist
test_words = ["hello", "python", "algoritm", "structures"]
for word in test_words:
    if spell_check(dictionary, word):
        print(f"'{word}' is correctly spelled.")
    else:
        print(f"'{word}' is not in the dictionary.")
# Output:
# 'hello' is correctly spelled.
# 'python' is correctly spelled.
# 'algoritm' is not in the dictionary.
# 'structures' is not in the dictionary.

#-------------------------------------

# Store definitions with words
dictionary = Trie()
words_with_definitions = [
    ("trie", "A tree-like data structure for efficient string retrieval"),
    ("algorithm", "A step-by-step procedure for solving a problem"),
    ("python", "A high-level programming language")
]

for word, definition in words_with_definitions:
    dictionary.insert(word, definition)

# Retrieve a definition
def get_definition(trie, word):
    current = trie.root
    for char in word:
        if char not in current.children:
            return None
        current = current.children[char]
    
    if current.is_end_of_word:
        return current.data
    return None

# Look up a word
lookup_word = "trie"
definition = get_definition(dictionary, lookup_word)
if definition:
    print(f"{lookup_word}: {definition}")
else:
    print(f"No definition found for '{lookup_word}'")
