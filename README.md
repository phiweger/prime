## README

Note: This is a work in progress, and really meant for internal use first. We will add functionality as we run into new problems.

### Installation

```bash
# install conda, then create a virtual environment w/
conda create -n lab python=3.6

# enter it
source activate lab

# for illustration, we'll create a directory
mkdir ~/tmp && cd ~/tmp
git clone https://github.com/phiweger/prime && cd prime
pip install -e .

# test
python setup.py test

# alternative installation (don't run if you ran the above)
pip install git+https://github.com/phiweger/prime.git@master
```

### Usage

First, we'll process our example data into a format that can be used for the [NEB calculator batch mode](https://tmcalculator.neb.com/#!/batch). `prime batch` takes 2 files (both in csv format), a primer inventory of the form 

| name | sequence | other columns in inventory |
| :-- | :-- | --- |
| 27F | AGAGTTTGATCMTGGCTCAG | ... |
| 1492R | CGGTTACCTTGTTACGACTT | ... |

and a file that specifies which primers are to be used in each pairing, like

| forward | reverse |
| :-- | :-- |
| 27F | 1492R |

That way, you can recycle your primer inventory file and only have to specify the pairs for each new experiment. With these files in place, you can prepare them for NEB:

```bash
# help
prime --help

# subcommand help
prime batch --help

# run
prime batch \
    -2 prime/tests/pairs.csv \
    -p prime/tests/primers.csv \
    -o ~/tmp/batch.csv
```

We can now upload `batch.csv` and NEB returns a file like:

| ID 1 | Primer 1 sequence | Tm 1 | ID 2 | Primer 2 sequence | Tm 2 | Anneal temp | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 27F | GAGTTTGATCATGGCTCAG | 60 | 1492R | CGGTTACCTTGTTACGACTT | 62 | 61 | OK
| 27F | GAGTTTGATCCTGGCTCAG | 63 | 1492R | CGGTTACCTTGTTACGACTT | 62 | 63 | OK

Note that our example primer, 27F, is actually degenerate: AGAGTTTGATC`M`TGGCTCAG -- `prime` will take care of this and disambiguate this primer according to the [IUPAC alphabet](https://www.bioinformatics.org/sms/iupac.html). If more than one degenerate base is present, `prime` will create all implicit primers (haplotypes). For example, if a primer contains `M` and `N`, the disambiguate result will be 2 * 4 = 8 primers. For now we recommend using the mean Tm for such a set, assuming the haplotypes are equimolar.
