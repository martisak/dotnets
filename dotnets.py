# Inspired by
# https://tgmstat.wordpress.com/2013/06/12/draw-neural-network-diagrams-graphviz/

layers = [3, 5, 5, 5, 2]

layers_str = ["Input"] + ["Hidden"] * (len(layers) - 2) + ["Output"]
layers_col = ["none"] + ["none"] * (len(layers) - 2) + ["none"]
layers_fill = ["black"] + ["gray"] * (len(layers) - 2) + ["black"]

print "digraph G {"
print "fontname = \"Hilda 10\""
print "rankdir=LR"
print "splines=line"
print "nodesep=.08;"
print "ranksep=1;"
print "edge [color=black, arrowsize=.5];"
print "node [fixedsize=true,label=\"\",style=filled," + \
    "color=none,fillcolor=gray,shape=circle]"

for i in range(0, len(layers)):
    print("subgraph cluster_{} {{".format(i))
    print("color={};".format(layers_col[i]))
    print("node [style=filled, color=white, penwidth=15,"
          "fillcolor={} shape=circle];".format(
              layers_fill[i]))

    for a in range(layers[i]):
        print "l{}{} ".format(i + 1, a),

    print ";"
    print("label = {};".format(layers_str[i]))
    print("}")


# Nodes
for i in range(1, len(layers)):
    for a in range(layers[i - 1]):
        for b in range(layers[i]):
            print "l{}{} -> l{}{}".format(i, a, i + 1, b)

print "}"
