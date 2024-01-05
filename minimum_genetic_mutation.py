# A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.
# Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is defined as one single character changed in the gene string.
# For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
# There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.
# Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed to mutate from startGene to endGene. If there is no such a mutation, return -1.
# Note that the starting point is assumed to be valid, so it might not be included in the bank.
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1
        res =  self.chooseMutation(startGene, endGene, bank, 0)
        if res >= 10:
            return -1
        else:
            return res

    def chooseMutation(self, startGene, endGene, bank, epoch):
        min_val = 10
        if epoch >= min_val:
            return min_val
        for gene in bank:
            if self.calculateDistance(startGene, gene) == 1:
                if gene == endGene:
                    min_val = min(min_val, epoch + 1)
                else:
                    bank_copy = bank.copy()
                    bank_copy.remove(gene)
                    min_val = min(min_val,
                                  self.chooseMutation(gene, endGene, bank_copy, epoch+1))
        return min_val

    def calculateDistance(self, gene1, gene2):
        return len([j for j in range(len(gene1)) if gene1[j] != gene2[j]])
  
