# assumed L, INPUTS, and NAME, are set coming in.
EXT = pdf
$(info L = $(L))
$(info INS = $(INS))
$(info NAME = $(NAME))
$(info EXT = $(EXT))

all: $(NAME).$(EXT)

$(NAME).$(EXT): $(INS)

$(NAME).md: $(INS) $L/header.tex $L/defs.tex
	pandoc --strip-comments -o $(NAME).md $(INS)

%.pdf: %.md $L/header.tex $L/defs.tex
	pandoc \
		--standalone --pdf-engine=lualatex \
		--variable monofont='JetBrainsMono Nerd Font' \
		--lua-filter=$L/latex-aside.lua \
		--metadata-file=$L/conf.yaml -H $L/header.tex -B $L/defs.tex \
		-o $@ \
		$<

%.tex: %.md $L/header.tex $L/defs.tex
	pandoc \
		--standalone \
		--variable monofont='JetBrainsMono Nerd Font' \
		--lua-filter=$L/latex-aside.lua \
		--metadata-file=$L/conf.yaml -H $L/header.tex -B $L/defs.tex \
		-o $@ \
		$<
