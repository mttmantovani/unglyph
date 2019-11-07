# unglyph

## Description
Makes an EPS file processable with [psfrag](https://www.ctan.org/pkg/psfrag), converting glyphs to plain text.

## When to use it
[psfrag](https://www.ctan.org/pkg/psfrag) allows replacement of strings in EPS files loaded in a .tex document, allowing full LaTeX control of the text in these figures. 
EPS files produced by recent versions of [matplotlib](https://github.com/matplotlib/matplotlib) contain 'glyphs' which are not processed regularly by `psfrag`. This tool will convert glyphs to plain text and will make them processable.

## Usage
Run with `python3 unglyph.py <input_eps_file>` or `python3 unglyph.py
<input_file> <output_file>`.


