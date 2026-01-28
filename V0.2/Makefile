# Aught to merge with /scripts/pdf/Makefile

L=scripts/PDFs

# all: $(NAME).$(EXT)

# $(NAME).$(EXT): $(INS)

# $(NAME).md: $(INS) $L/header.tex $L/defs.tex
# 	pandoc --strip-comments -o $(NAME).md $(INS)

# For PDF versions of source files
SOURCES := $(wildcard techdoc/*.md)
PDFS := $(SOURCES:techdoc/%.md=build/%.pdf)

$(info SOURCES = $(SOURCES))
$(info PDFS = $(PDFS))

all: $(PDFS)

PDFLAGS=--standalone --pdf-engine=lualatex \
		--variable monofont='JetBrainsMono Nerd Font' \
		--lua-filter=$L/latex-aside.lua \
		--metadata-file=$L/conf.yaml -H $L/header.tex -B $L/defs.tex \

GETTITLE=-ane '@a=/^\\\#\\\#\s+(.*?\n)$$/m; print $$a[0]'

# @mkdir -p build
build/%.pdf: techdoc/%.md
	TITLE=`perl $(GETTITLE) $<` \
	BASENAME=$(basename $(notdir $<)) \
	pandoc $(PDFLAGS) -o $@ $<

build/%.tex: techdoc/%.md
	BASENAME=$(basename $(notdir $<)) pandoc $(PDFLAGS) -o $@ $<
