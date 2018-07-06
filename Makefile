# Settings
MAKEFILES=Makefile $(wildcard *.mk)
JEKYLL=jekyll
SRC_MD=$(wildcard *.md)
DST_DIR=_site

# Controls
.PHONY : commands clean serve site
all : commands

## commands : show all commands.
commands :
	@grep -h -E '^##' ${MAKEFILES} | sed -e 's/## //g'

## serve    : run a local server.
serve :
	${JEKYLL} serve -I

## site     : build files but do not run a server.
site :
	${JEKYLL} build

## design   : make visualization of design.
design : files/design/design.svg

files/design/design.svg : files/design/design.gv
	dot -Tsvg < $< > $@

## clean    : clean up junk files.
clean :
	@rm -rf ${DST_DIR}
	@find . -name .DS_Store -exec rm {} \;
	@find . -name '*~' -exec rm {} \;
