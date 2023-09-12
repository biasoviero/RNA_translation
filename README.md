# Deterministic Finite Automaton that simulates RNA translation

Project made by [Beatriz Soviero](https://github.com/biasoviero) and [Lais Canabarro](https://github.com/laiscanabarro)

## Description of the RNA translation process

### What is RNA?

RNA its a molecule that synthesizes proteins. Its structure is formed by a single strand that contains four types of nitrogenous bases:

  * Adenine (A)
  * Cytosine (C)
  * Guanine (G)
  * Uracil (U)

### Protein synthesis

To synthesize proteins, this process needs two phases:
  * Transcription - synthesis of messenger RNA (mRNA) by reading DNA´s nitrogenous bases
  * Translation - the chain of bases contained in the mRNA are divided in groups of 3 bases (called codons) that are translated into amino acids. This stage begins after reading the start codon (AUG) and ends after reading a stop codon (UAA, UAG or UGA). The protein is a result of the group of amino acids encoded by the read codons.

The relations among codons and amino acids are described in the genetic code, shown in the table below:

![Genetic Code](https://cdn1.byjus.com/wp-content/uploads/2022/05/Genetic-Code-Table.png)

### Deterministic Finite Automaton

### Alphabet

The group of symbols accepted by our automaton are the four types of nitrogenous bases (A, U, C, G) and all the acaminoacids present in the genetic code (Phe, Leu, Ser, Tyr, Cys, Trp, Pro, His, Gln, Arg, Ile, Thr, Asn, Lys,
Val, Ala, Asp, Glu, Gly)

### States

The automaton´s start stage is the q0 (when the start codon is read) and the final states q28 and q30 (when a stop codon is read)

![Automaton](https://github.com/biasoviero/Trabalho-RNA/blob/main/RNA.jpg)

## Automaton implemented with Python
