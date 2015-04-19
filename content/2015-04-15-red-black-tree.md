Title: Red black tree
Date: 2015-04-15
category: data structure

## Intro

Before introducing a red black tree, we need to know what is a binary search tree.

### Binary search tree

Binary search tree's features

+ insert cost order lgn
+ find cost order lgn
+ delete cost order lgn

If we want all operations are order lgn time, we need to make sure the tree is balanced. A red black tree is balanced all the time. We can say a red black tree is a self balanced binary search tree.

### Red black tree

What is a red black tree.

1. a node is either red or black
2. the root and leaves(nils) are black
3. every red node has black parent
4. all simple paths from a node x to a descendent leaf of x have same


![rb_tree_sample](/images/rbtree/red-black-tree-sample.jpg)
