from __future__ import division
import random

template="""[injection-pointinj{0}]
i-distr = fixed
fixed-inc = {9}
m-distr = componentMass
min-mass1 = {1}
max-mass1 = {2}
min-mass2 = {3}
max-mass2 = {4}
min-mtotal = 1.
max-mtotal = 1000.
enable-spin =
aligned =
min-spin1 = 0
max-spin1 = {5}
min-spin2 = 0
max-spin2 = {6}
taper-injection = startend
seed = {8}
waveform = {7}

[banksim-pointinj{0}]
template-approximant={7}
signal-approximant={7}
signal-start-frequency = 14
template-start-frequency = 14
filter-low-frequency = 15
filter-sample-rate = 2048
filter-signal-length = 4

[workflow-pointinjs]
pointinj{0}=2000

"""

max_injs = 100
count=0
while count < max_injs:
    mass1 = random.uniform(10,500)
    mass2 = random.uniform(10,500)
    inc = random.uniform(75,105)
    if mass2 > mass1:
        continue
    if mass1 / mass2 > 10 or (mass1 + mass2) < 100 or (mass1 + mass2) > 500:
        continue
    if mass1 > 2:
        maxspin1 = 0.998
    if mass2 > 2:
        maxspin2 = 0.998
    waveform = "IMRPhenomHM"
    name = "_{:.2f}_{:.2f}".format(mass1, mass2)
    print template.format(name, mass1, mass1 + 0.0001, mass2, mass2 + 0.0001, maxspin1, maxspin2, waveform, random.randint(0,1000000),inc)
    count += 1
