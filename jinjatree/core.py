import os
import re

from anytree import Node, RenderTree


PATTERN = r'(extends|include|from) [\"\'](.*?)[\"\']'


class JinjaTree:

    RELATIONSHIP_PATTERN = r'(extends|include|from) [\"\'](.*?)[\"\']'

    def __init__(self, location):
        self.nodes = []
        self.jinjas = []
        self.location = location

        self.initialize()

    def load_jinjas(self):
        for path, name, filenames in os.walk(self.location):
            normalized_path = path.replace(self.location, '')[1:]
            self.jinjas += [
                (f'{path}/{f}', f'{normalized_path}/{f}')
                for f in filenames if f.endswith('.jinja')
            ]

    def process_content(self, content):
        matches = re.findall(self.RELATIONSHIP_PATTERN, content)
        for relationship, name in matches:
            print((relationship, name))

    def build_nodes(self):
        for path, jinja in self.jinjas:
            with open(path, 'r') as f:
                content = f.read()
                self.process_content(content)

    def initialize(self):
        self.load_jinjas()
        self.build_nodes()
