class Tree:
    def __init__(self, root):
        self.root = root

    def get_element_by_id(self, target_id):
        # Inner recursive DFS function
        def dfs(node):
            if node.get('id') == target_id:
                return node

            for child in node.get('children', []):
                result = dfs(child)
                if result:
                    return result

            return None

        return dfs(self.root)



tree_data = {
    'tag_name': 'div',
    'id': 'container',
    'text_content': '',
    'children': [
        {
            'tag_name': 'h1',
            'id': 'heading',
            'text_content': 'Welcome',
            'children': []
        },
        {
            'tag_name': 'p',
            'id': 'paragraph',
            'text_content': 'Some text',
            'children': []
        }
    ]
}

tree = Tree(tree_data)
print(tree.get_element_by_id('heading'))  # Outputs the 'h1' node
print(tree.get_element_by_id('not-here'))  # Outputs None
