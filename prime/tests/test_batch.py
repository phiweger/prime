def test_mutate():
    from prime.batch import mutate

    assert mutate('ACTG', [1, 3], 'AA') == 'AATA'


def test_expand_ambiguous():
    from Bio.Alphabet import IUPAC
    from prime.batch import expand_ambiguous

    haplotypes = expand_ambiguous(
        ['M', 'K'], IUPAC.IUPACData.ambiguous_dna_values)
    assert haplotypes == ['AG', 'CG', 'AT', 'CT']


def test_disambiguate():
    from prime.batch import disambiguate
    
    seq = 'GAMTGN'
    expected = set([
        'GAATGG',
        'GACTGG',
        'GAATGA',
        'GACTGA',
        'GAATGT',
        'GACTGT',
        'GAATGC',
        'GACTGC',])
    assert set(disambiguate(seq)) == expected


def test_is_degenerate():
    from prime.batch import is_degenerate

    assert is_degenerate('ACTACN')
    assert not is_degenerate('ACTACGCA')