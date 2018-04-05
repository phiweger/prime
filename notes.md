## Primer3 usage

`python setup.py test` as described [here](https://docs.pytest.org/en/latest/goodpractices.html)


```python
# pip install primer3-py
# https://libnano.github.io/primer3-py/quickstart.html#primer-design
import primer3

primer3.calcTm('GTAAAACGACGGCCAGT')
# 49.168
```


dv_conc .. divalent cation in mM -- Magnesium concentration

mv_conc .. monvalent ..., [see](https://www.quora.com/Why-are-monovalent-cation-used-in-PCR) // NH4+ and Tris+ are monovalent cations, and I assume their molarity is added

> At constant cation concentration, the melting temperature of the DNA model hairpin decreases in the order Li+ ∼ Na+ ∼ K+ > NH4+ > TMA+ > Tris+ > TEA+ > TPA+ > TBA+. -- __Stellwagen, Earle, Joseph M. Muse, and Nancy C. Stellwagen. 2011. “Monovalent Cation Size and DNA Conformational Stability.” Biochemistry 50 (15): 3084–94.__

> Currently the SantaLucia salt correction formula should be used if Mg2þ is present. -- __Ahsen, Nicolas von, Carl T. Wittwer, and Ekkehard Schütz. 2011. “Monovalent and Divalent Salt Correction Algorithms for Tm Prediction--Recommendations for Primer3 Usage.” Briefings in Bioinformatics 12 (5): 514–17.__

[buffer LongAmp DNA polymerase (NEB)](https://bit.ly/2GIJjXq):

1X LongAmp® Taq Reaction Buffer Pack 
60 mM Tris-SO4 
20 mM (NH4)2SO4 
2 mM MgSO4 
3% Glycerol 
0.06% IGEPAL® CA-630 
0.05% Tween® 20 
(pH 9.1 @ 25°C)

- [NEB Tm calculator algo](https://tmcalculator.neb.com/#!/help)
- it has a batch mode

> Why is the primer Tm (or annealing temperature) different from other Tm calculators? The NEB Tm calculator is designed to take into account the buffer conditions of the amplification reaction based on the selected NEB polymerase. Many Tm calculators do not, relying instead on a default salt concentration. The annealing temperature for each polymerase is based on empirical observations of efficiency. The optimal annealing temperature for high fidelity hot start DNA polymerases like Q5 may differ significantly from that of Taq-based polymerases.

> [The] primer concentration Cp is assumed to be significantly greater (6x) than the target template concentration. // default value in calculator is 400 nM for LongAmp

> In the NEB Tm Calculator, Tm is computed by the method of SantaLucia [...] The Tm, as calculated above, assumes a 1 M monovalent cation concentration. This value is adjusted to reaction buffer conditions using the salt correction of Owczarzy [...]

> For Phusion® polymerases, Tm is computed by the method of Breslauer [...] The Tm is adjusted to reaction buffer conditions using the salt correction of Schildkraut [...]

> While the method and data of SantaLucia are preferred, it was necessary to use the Breslauer data and modified equations for annealing temperatures in reactions using Phusion® polymerases to allow compatibility with recommendations provided by Finnzymes Oy, now a part of Thermo Fisher Scientific.

on entering Phusion w/ GC buffer (contains DMSO):

> _DMSO_ can improve PCR amplification from GC-rich templates, but it is also known to reduce the annealing temperature of primers in a PCR reaction. Therefore, it is recommended that _for every 1% of additional DMSO added, the calculated annealing temperature should be reduced by 0.6°C_. __Chester and Marshak, 1993. Analytical Biochemistry 209, 284-290__.



```csv
name,sequence,pair
```



```python




def calc_tm(polymerase='longamp', primer_conc=400):
    '''Calculate melting temperature (Tm).'''
    pass


def cal_ta():
    '''Calculate annealing temperature (Ta).'''
    pass


seq = 'AGAGTTTGATCMTGGCTCAG'  # 'CGGTTACCTTGTTACGACTT'
primer_conc = 200  # nM







conf = {'tm_method': 'santalucia', 'salt_corrections_method': 'owczarzy'}

if polymerase == 'phusion':
    conf['tm_method'] = 'breslauer'
    conf['salt_corrections_method'] = 'schildkraut'


primer3.calcTm(
    seq, 
    dna_conc=(primer_conc/6)*7,  # primer is assumed 6x template
    mv_conc=(60+20), 
    dv_conc=2, 
    tm_method='santalucia', 
    salt_corrections_method='owczarzy')

# check for hairpins
primer3.calcHairpin(seq)
# ThermoResult(structure_found=True, tm=35.21, dg=211.61, dh=-36500.00, ds=-118.37)
primer3.calcHomodimer(seq)
# ThermoResult(structure_found=True, tm=17.32, dg=-2936.22, dh=-122200.00, ds=-384.54)
a = 'TTTCTGTTGGTGCTGATATTGCAGAGTTTGATCMTGGCTCAG'
b = 'ACTTGCCTGTCGCTCTATCTTCCGGTTACCTTGTTACGACTT'
primer3.calcHeterodimerTm(a, b)
```


anneal at min_Tm(primer1, primer2) - 5°C, w/ max. 65°C

> Annealing temperature for experiments with this enzyme should typically not exceed 65°C. -- displayed as footnote when entering LongAmp in NEB calculator

> Use of the Q5 High GC Enhancer often lowers the range of temperatures at which specific amplification can be observed, however the rule used to determine Q5 annealing temperatures (Ta = Tm_lower+3°C) typically yields values that will support specific amplification with or without the enhancer. -- displayed as footnote when entering Q5 in NEB calculator

// for DeepVent is seems anneal = Tm_lower

> There is no "exact" annealing temperature of a pcr reaction. I would start the pcr with some degrees below the lower Tm-value (3 - 5 °C). If there are non-spezific bands, rise the temperature stepwise (1 - 2 degree per step). Or, if possible, you can perform a gradien pcr with rising annealing temperature (eg 49, 51, 53, 55, 57). But you should keep in mind, that the MgCl2 conzentration is more critical for performing a PCR. -- https://www.researchgate.net/post/How_do_I_calculate_the_annealing_temperature_of_my_PCR_reaction

optimization of annealing temperature Ta:

> The TaOPT is found to be a function of the melting temperatures of the less stable primer-template pair and of the product. The fact that experimental and calculated T,OPT values agree to within 0.70C eliminates the need for determining TaOPT experimentally. Synthesis of DNA fragments shorter than 1 kb is more efficient if a variable Ta is used, such that the Ta is higher in each consecutive cycle. -- __Rychlik, W., W. J. Spencer, and R. E. Rhoads. 1990. “Optimization of the Annealing Temperature for DNA Amplification in Vitro.” Nucleic Acids Research 18 (21): 6409–12.__

same article:

> Knowing what concentration to use for c in the case of a PCR experiment, however, is problematical: the concentration of template changes dramatically during the course of the PCR reaction (e.g., 260,000-fold in the experiment shown in Fig. 1, 25 cycles). We determined empirically that using _c = 250 pM_ in Eqn. (ii) gave good agreement with experimental results for all primer-template combinations tested. // compare c in equation (ii) to the documentation from NEB

see equations (i), (ii) and (iii)

- in (i), Tm (Breslauer) and salt (Schildkraut) -- use this for Phusion
- the calculation of Ta can from the article can thus only be applied to Phusion

__Pauthenier, Cyrille, and Jean-Loup Faulon. 2014. “PrecisePrimer: An Easy-to-Use Web Server for Designing PCR Primers for DNA Library Cloning and DNA Shuffling.” Nucleic Acids Research 42 (Web Server issue): W205–9.__

- [documentation](https://absynth.issb.genopole.fr/Bioinformatics/tools/PrecisePrimer/doc/DocWebServer-PrecisePrimer.pdf)
- discussion of [additives](https://bitesizebio.com/19420/just-what-do-all-these-additives-do/) such as DMSO and Tween


