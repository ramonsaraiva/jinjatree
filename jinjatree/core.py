import os
import re

from anytree import (
    Node,
    RenderTree)
from anytree.dotexport import RenderTreeGraph


class TreeRenderer:

    def render(self):
        for pre, fill, node in RenderTree(self.root):
            print('{pre}{node_name}'.format(pre=pre, node_name=node.name))

    def render_image(self, name):
        RenderTreeGraph(self.root).to_picture(name)

    def generate_dotfile(self, name):
        RenderTreeGraph(self.root).to_dotfile(name)


class JinjaTree(TreeRenderer):

    RELATIONSHIP_PATTERN = r'(extends|include|from) [\"\'](.*?)[\"\']'

    def __init__(self, location):
        self.nodes = []
        self.jinjas = []
        self.location = os.path.abspath(location)
        self.current_node = None
        self.root = None

        self.initialize()

    @property
    def orphan_nodes(self):
        return (node for node in self.nodes if node.is_root and node.children)

    def load_jinjas(self):
        for path, name, filenames in os.walk(self.location):
            norm_path = os.path.abspath(path).replace(self.location, '')[1:]
            self.jinjas += [
                ('{path}/{f}'.format(path=path, f=f), '{norm_path}/{f}'.format(
                    norm_path=path, f=f) if norm_path else '{f}'.format(f=f))
                for f in filenames if f.endswith('.jinja')
            ]

    def process_content(self, content):
        matches = re.findall(self.RELATIONSHIP_PATTERN, content)
        for relationship, name in matches:
            node, created = self.find_or_create(name)
            if relationship == 'extends':
                self.current_node.parent = node
                continue
            # include (partials) or from .. import (macros)
            if not created:
                node = Node(name)
            node.parent = self.current_node

    def build_nodes(self):
        for path, jinja in self.jinjas:
            self.current_node, _ = self.find_or_create(jinja)
            with open(path, 'r') as f:
                content = f.read()
                self.process_content(content)

    def adopt_orphan_nodes(self):
        self.root = Node('jinjas')
        for node in self.orphan_nodes:
            node.parent = self.root

    def find_or_create(self, jinja):
        found = (node for node in self.nodes if node.name == jinja)

        try:
            return next(found), False
        except StopIteration:
            node = Node(jinja)
            self.nodes.append(node)
            return node, True

    def initialize(self):
        self.load_jinjas()
        self.build_nodes()
        self.adopt_orphan_nodes()
