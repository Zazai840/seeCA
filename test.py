import numpy as np
from automata import *
from rules.rule30 import rule30_test

rule30 = Automaton.create(30)
np.testing.assert_array_equal(rule30, rule30_test)
