import click


def load_config():
    '''
    polymerases, buffers = load_config()
    '''
    from glob import glob
    import yaml
    import prime

    files = glob(prime.__file__.replace('__init__.py', 'config/*'))
    # http://python-packaging.readthedocs.io/en/latest/non-code-files.html

    d = {}
    for f in files:
        name = f.split('/')[-1].replace('.yaml', '')
        d[name] = f

    try:
        with open(d['polymerases'], 'r') as p:  # p .. polymerases
            polymerases = yaml.load(p)
        with open(d['buffers'], 'r') as b:  # b .. buffers
            buffers = yaml.load(b)
    except yaml.YAMLError as exc:
        print(exc)
    
    return polymerases, buffers


def disambiguate(seq):
    '''Yield disambiguate sequences for ambiguate ones (degenerate primers).
    
    Usage:

    seq = 'GAGTTTGATCMTGGCTKAG'
    disambiguate_primer(seq)

    # original first:
    # GAGTTTGATC M TGGCT K AG
    # GAGTTTGATC A TGGCT G AG
    # GAGTTTGATC C TGGCT G AG
    # GAGTTTGATC A TGGCT T AG
    # GAGTTTGATC C TGGCT T AG
    '''
    from collections import OrderedDict
    from Bio.Alphabet import IUPAC
        
    alphabet = IUPAC.IUPACData.ambiguous_dna_values
    # IUPAC.IUPACData.ambiguous_dna_complement

    ambiguous = {}
    for pos, char in enumerate(seq):
        if (char not in 'ACTG') and (char in alphabet):
            ambiguous[pos] = char
    
    if not ambiguous:
        return [seq]

    # since Python 3.6, dictionaries are insertion ordered
    # however, to be on the save side, we can order by key for earlier versions
    ambiguous = OrderedDict(sorted(ambiguous.items()))

    k = ambiguous.keys()
    v = list(ambiguous.values())
    expanded = expand_ambiguous(v, alphabet)
    
    result = []
    for haplotype in expanded:  # MK has 4 haplotypes: AG, CG, AT, CT
        result.append(mutate(seq, k, haplotype))

    return result


def mutate(seq, pos, haplotype):
    '''Replace characters in a sequence using an index and a haplotype.

    Usage:

    mutate('ACTG', [1, 3], 'AA')
    # 'AATA'
    '''
    cp = seq  # Python strings are immutable, so we won't clobber seq w/ this
    for i, j in zip(pos, haplotype):
        cp = cp[:i] + j + cp[i+1:]
    return cp 


def expand_ambiguous(ambiguous, alphabet):
    '''Expand ambiguous letters (IUPAC alphabet) and return all combinations.

    Usage:

    from Bio.Alphabet import IUPAC
    expand_ambiguous(['M', 'K'], IUPAC.IUPACData.ambiguous_dna_values)
    # ['AG', 'CG', 'AT', 'CT']
    '''
    l = [base for base in alphabet[ambiguous.pop(0)]]
    for letter in ambiguous:
        tmp = []
        for base in alphabet[letter]:
            [tmp.append(i + base) for i in l]
        l = tmp

    return l


def is_degenerate(seq):
    return not all([char in 'ACTG' for char in seq])


@click.command()
@click.option(
    '--pairs', '-2',
    help='File path to primers (csv)',
    required=True, type=click.Path(exists=True))
@click.option(
    '--primers', '-p',
    help='File path to primer pairs (csv)',
    required=True, type=click.Path(exists=True))
@click.option(
    '--outfile', '-o',
    help='Results file',
    required=True, type=click.Path(exists=False))
def batch(pairs, primers, outfile):
    '''Short info.

    Some info.

    Usage:

    \b
    prime batch \\
        -2 prime/tests/pairs.csv \\
        -p prime/tests/primers.csv \\
        -o ~/tmp/batch.csv

    \b
    27F;GAGTTTGATCATGGCTCAG;1492R;CGGTTACCTTGTTACGACTT
    27F;GAGTTTGATCCTGGCTCAG;1492R;CGGTTACCTTGTTACGACTT
    '''
    import csv
    from itertools import repeat, product
    from Bio.Alphabet import IUPAC
    import numpy as np

    
    db = {}
    with open(primers, newline='') as file:
        reader = csv.reader(file, delimiter=',')
        next(reader)  # skip header
        
        for name, seq, *rest in reader:
            db[name] = seq
    # print(db)   

    with open(pairs, newline='') as file:
        reader = csv.reader(file, delimiter=',')
        next(reader)  # skip header
        
        with open(outfile, 'w+') as out:
            
            for fwd, rev in reader:  # fwd .. forward, rev .. reverse

                seq_fwd = disambiguate(db[fwd])
                seq_rev = disambiguate(db[rev])

                dis_fwd = zip(repeat(fwd), seq_fwd)
                dis_rev = zip(repeat(rev), seq_rev)
                # stackoverflow.com/questions/36709978
                # stackoverflow.com/questions/4815792

                for left, right in product(dis_fwd, dis_rev):
                # left, right as in forward, reverse -- synonyms
                # here, the former refers to ambiguate, the latter disambiguate
                # product .. stackoverflow.com/questions/12935194
                    out.write(
                        ';'.join(left) + ';' + ';'.join(right) + '\n')






# evaluation: Tm difference is greater than the recommended limit of 5 °C.
# shown in NEB calculator
# if accession, then download it, align primers and extract it
# use snakemake workflow for this




'''
anneal at min_Tm(primer1, primer2) - 5°C, w/ max. 65°C

> Annealing temperature for experiments with this enzyme should typically not exceed 65°C. -- displayed as footnote when entering LongAmp in NEB calculator

> Use of the Q5 High GC Enhancer often lowers the range of temperatures at which specific amplification can be observed, however the rule used to determine Q5 annealing temperatures (Ta = Tm_lower+3°C) typically yields values that will support specific amplification with or without the enhancer. -- displayed as footnote when entering Q5 in NEB calculator

'''





