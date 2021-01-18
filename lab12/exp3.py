
class DNA() :
    def __init__(self,dna_string):
        for i in dna_string :
            if i != "A" or "T" or "G" or "C" :
                print("invalid string")
                break
        self.dna_string = dna_string

    def count_nucleotides(self) :
        A_count = 0
        T_count = 0
        G_count = 0
        C_count = 0
        A_ddict = {}
        T_ddict = {}
        G_ddict = {}
        C_ddict = {}
        for i in self.dna_string :
            if i == "A" :
                A_count += 1
            if i == "A" :
                T_count += 1
            if i == "A" :
                G_count += 1
            if i == "A" :
                C_count += 1
        A_ddict["A"] = A_count
        T_ddict["T"] = T_count
        G_ddict["G"] = G_count
        C_ddict["C"] = C_count
        return A_ddict , T_ddict , G_ddict , C_ddict

    def calculate_complement(self):
        complement_dna = self.dna_string.replace("A","T")
        complement_dna = complement_dna.replace("G","C")
        complement_dna = complement_dna.replace("C", "G")
        complement_dna = complement_dna.replace("T", "A")
        return complement_dna

    def count_point_mutations(self,dna) :
        count = 0
        for i in range(len(dna)):
            if dna[i] != self.dna_string[i]:
                count += 1
        return count

    def find_motif(self,dna) :
        l1 = []
        index = 0
        while index < len(dna):
            i = dna.find(self.dna_string, index)
            if i == -1:
                return l1
            l1.append(i)
            index = i + 1
        return l1







