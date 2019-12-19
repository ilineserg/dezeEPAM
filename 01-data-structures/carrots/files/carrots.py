from collections import namedtuple


def translate_from_dna_to_rna(dna):
    """your code here"""
    rna = None
    rnk_map = {"A": "U", "C": "G", "G": "C", "T": "A"}
    if rna is None:
        rna = "".join([rnk_map[el] for el in dna])
    return rna


def count_nucleotides(dna):
    """your code here"""
    num_of_nucleotides = ['A - ' + str(dna.count('A')),
                          'C - ' + str(dna.count('C')),
                          'G - ' + str(dna.count('G')),
                          'T - ' + str(dna.count('T'))]
    return num_of_nucleotides


def translate_rna_to_protein(rna, protein_map):
    """your code here"""
    rna_list = [rna[x:x+3] for x in range(0, len(rna), 3)]
    protein = "".join([protein_map[el] for el in rna_list if len(el) == 3])
    return protein


if __name__ == '__main__':
    dna = []
    dna_code = ''
    Gen = namedtuple('Gen', 'name dna_code')
    name = ''
    with open('dna.fasta', 'r') as dna_file:
        for line in dna_file:
            line = line.strip()
            if line.startswith('>'):
                if len(dna_code) > 0:
                    dna.append(Gen(name, dna_code))
                    dna_code = ''
                name = line
            if not line.startswith('>'):
                dna_code += line
        if len(dna_code) > 0:
            dna.append(Gen(name, dna_code))

    with open('rna_codon_table.txt', 'r') as codon_file:
        rna_codon_dict = {}
        for line in codon_file:
            line = line.strip().split()
            for index, item in enumerate(line):
                if index % 2 == 0:
                    rna_codon_dict.update({item: line[index + 1]})

    with open('statistics_of_nucleotid.txt', 'w') as statistics:
        for gen in dna:
            statistics.write('Count of: ' + gen.name + '\n')
            statistics.write(', '.join(count_nucleotides(gen.dna_code)) + '\n')

    with open('rna.txt', 'w') as rna_file:
        for gen in dna:
            rna_file.write('RNA code of: ' + gen.name + '\n')
            rna = translate_from_dna_to_rna(gen.dna_code)
            rna_file.write(rna + '\n')

    with open('protein.txt', 'w') as protein_file:
        for gen in dna:
            protein_file.write('RNA to protein for: ' + gen.name + '\n')
            rna = translate_from_dna_to_rna(gen.dna_code)
            protein_file.write(translate_rna_to_protein(rna, rna_codon_dict) + '\n')



