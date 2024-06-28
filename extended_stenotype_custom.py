from plover.system.english_stenotype import *

KEYS = (
  '#', '_', '$', '@', '^-', '+-', '&-',
  'S-', 'T-', 'K-', 'P-', 'W-', 'H-', 'R-',
  'A-', 'O-',
  '*',
  '-E', '-U',
  '-F', '-R', '-P', '-B', '-L', '-G', '-T', '-S', '-D', '-Z',
)

SUFFIX_KEYS = ()

NUMBER_KEY = None
NUMBERS = {}
FERAL_NUMBER_KEY = False

ORTHOGRAPHY_RULES.insert(
  # panic +ed = panicked (*panicced)
  0, (r'^(.+)ic \^ (ed|ing|y|ier|iest|er)$', r'\1ick\2'),
)