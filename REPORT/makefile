### Report makefile ###

R = master

moc: $R.tex
	pdflatex $R.tex

all: $R.tex
	pdflatex --shell-escape $R.tex
	bibtex $R
	pdflatex --shell-escape $R.tex
	pdflatex --shell-escape -synctex=1 $R.tex


nobib: $R.tex
	pdflatex --shell-escape $R.tex
	pdflatex --shell-escape $R.tex
	pdflatex --shell-escape -synctex=1 $R.tex

view:	$R.tex
	make moc
	evince $R.pdf &

open:	$R.tex
	open $R.pdf

okular: $R.tex
	make all
	okular $R.pdf 1>&- 2>&- &

bot: $R.tex
	make clean
	pdflatex -interaction=nonstopmode -shell-escape	$R.tex
	bibtex $R
	pdflatex -interaction=nonstopmode -shell-escape $R.tex
	pdflatex -interaction=nonstopmode -shell-escape	-synctex=1 $R.tex
	make clean

clean:
	rm -f *.aux $R.log $R.toc $R.blg $R.lot $R.lof $R.ps $R.dvi $R.lox *~ *.backup *.out *.log *.bbl *.tmp *.tps   */*~ */*.log  */*/*~ *.bak *conflicted\ copy*.pdf *synctex*conflicted\ copy*.gz
## $R is clean! ##
