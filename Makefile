SOURCES=$(wildcard *.dot)
PNG_OBJECTS=$(SOURCES:.dot=.png)

all: $(PNG_OBJECTS)

%.png: %.dot
	dot -v -Tpng $< -o $@

clean:
	-rm $(PNG_OBJECTS)