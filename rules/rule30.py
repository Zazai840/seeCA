import cellpylib as cpl
import matplotlib as plt 

rule30_test = cpl.init_simple(200)
rule30_test = automaton = cpl.evolve(rule30_test, timesteps=100, memoize=True,
                                apply_rule=lambda n, c, t: cpl.nks_rule(n, 30))
cpl.plot(rule30_test)