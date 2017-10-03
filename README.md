# jinjatree

![circle-ci-badge](https://circleci.com/gh/ramonsaraiva/jinjatree.svg?style=shield&circle-token=)
![codecov](https://codecov.io/gh/ramonsaraiva/jinjatree/branch/master/graph/badge.svg)(https://codecov.io/gh/ramonsaraiva/jinjatree)

## Installing

`pip install . --upgrade`

## Usage

### Default stdout render
Renders a simple tree in your terminal/stdout
```
jinjatree my_project
```

### Create a PNG image
Renders the tree in PNG image
```
jinjatree my_project --output png --file tree.png
```

### Create a DOT file
Generates a dot file with the tree
```
jinjatree my_project --output dot --file tree.dot
```
