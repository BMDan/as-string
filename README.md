# as-string
Silly little utility for dumping arbitrary files as C (or Python or Ruby or...) strings

All the existing tools I could find would dump a string as an integer array (`{72, 101, 108, `...) or with
_everything_ encoded (`"\x48\x65\x6c`...).  I wanted strings encoded as a human does (`"Hello, world!\n"`).
This does that.
