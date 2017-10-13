from unittest import TestCase

from jinjatree.core import JinjaTree, TreeRenderer


class JinjaTreeTest(TestCase):

    def setUp(self):
        self.jinjatree = JinjaTree('')

    def test_attr(self):
        self.assertEqual(
            self.jinjatree.RELATIONSHIP_PATTERN,
            r'(extends|include|from) [\"\'](.*?)[\"\']')
        self.assertIsInstance(self.jinjatree, TreeRenderer)
