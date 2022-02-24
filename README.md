# Binary Classification of Biomimicry Papers Using SciBERT

The NASA PeTaL (Periodic Table of Life) Project is an open source artificial intelligence design tool that leverages data and information from nature and technology to advance biomimicry R&D.

This README was last updated on 24 February 2022.

# Links
 * [Overview](#overview)
 * [Files](#files)
 * [Getting Started](#getting-started)
 * [Running SciBERT](#running-scibert)
 * [More Informaion](#more-information)
 * [Future Work](#future-work)
 * [Contact](#contact)
  
## Overview
The aim of this project is to utilize SciBERT to identify biomimicry papers in the scientific literature using binary classification (Y/N). 

## Files
```binary_labeler_scibert_new.py``` main file to train SciBERT on biomimicry papers.

```golden_1-27-22.csv``` training data

```convert_goldenjson_to_csv``` convert golden.json file to csv file 

```train.py``` code for training SciBERT

```test.py``` code for testing SciBERT

## More Information
 * [SciBERT: A Pretrained Language Model for Scientific Text](https://arxiv.org/abs/1903.10676)
 * [Attention Is All You Need](https://arxiv.org/abs/1706.03762)

## Future Work
 * Expand training set of both positive and negative papers.
 * Compare results to Support Vector Machine work from Allen Institute for AI (AI2).

# Contact
For questions contact Alexandra Ralevski (alexandra.ralevski@gmail.com)


