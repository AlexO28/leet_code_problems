# Biologists are studying basic patterns in DNA sequences. Write a solution to identify sample_id with the following patterns:
# Sequences that start with ATG (a common start codon)
# Sequences that end with either TAA, TAG, or TGA (stop codons)
# Sequences containing the motif ATAT (a simple repeated pattern)
# Sequences that have at least 3 consecutive G (like GGG or GGGG)
# Return the result table ordered by sample_id in ascending order.
import pandas as pd


def analyze_dna_patterns(samples: pd.DataFrame) -> pd.DataFrame:
    samples["has_start"] = samples["dna_sequence"].apply(lambda x: int(x[:3] == "ATG"))
    samples["has_stop"] = samples["dna_sequence"].apply(
        lambda x: int(x[-3:] in ["TAA", "TAG", "TGA"])
    )
    samples["has_atat"] = samples["dna_sequence"].apply(lambda x: int("ATAT" in x))
    samples["has_ggg"] = samples["dna_sequence"].apply(lambda x: int("GGG" in x))
    return samples
