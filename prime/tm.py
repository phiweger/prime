import click


@click.command()
def tm():
    print('bar')


'''
    pairs = '/Users/phi/Dropbox/repos_git/prime/prime/tests/pairs.csv'
    fp = '/Users/phi/Dropbox/repos_git/prime/prime/tests/primers.csv'
    
    db = {}
    with open(fp, newline='') as file:
        reader = csv.reader(file, delimiter=',')
        next(reader)  # skip header
        
        for name, seq, *rest in reader:
            db[name] = seq
            
            if is_degenerate(seq):
                query = disambiguate(seq)
            else:
                query = [seq]

            result = []
            for q in query:
                result.append(
                    round(
                        primer3.calcTm(
                            q, 
                            dna_conc=(concentration/6)*7,  # primer is assumed 6x template
                            dntp_conc=0.3,
                            mv_conc=(60+20), 
                            dv_conc=2, 
                            tm_method='santalucia', 
                            salt_corrections_method='owczarzy'),
                        1))
            print(round(np.mean(result), 1), name, q, result)
'''