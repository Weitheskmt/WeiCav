# WeiCav: Westlake Uni Cavity Simulations

![setup](src/setup.png)

## What is WeiCav?

WeiCav is an approach to simulate **coupled photon-nuclear dynamics for realistic(>100,0000) molecules** in optical cavities under **vibrational strong coupling (VSC)**. Considering the influence of molecular rotation and level disorder on the coupling between molecules and photons, we can use WeiCav to explore possible cavity modifications of molecular properties. It aims to accurately describe **VSC or vibrational ultrastrong (V-USC) coupling**, i.e., when a few cavity modes are resonantly coupled to a few vibrational normal modes of molecules and a collective Rabi splitting is formed in the molecular infrared (IR) spectrum.

This approach is still under development and more features will be reported and updated in the near future.

#### What can WeiCav do NOW?

- Calculating **density of states (DOS) of polaritons** under VSC for both disordered or ordered molecular energy levels, where molecular rotation frequency and phase can be included.

- Propagating **time evolution of correlation functions (CORR) of photon-matter hybrid wavefunctions** under VSC for both disordered or ordered molecular energy levels, where molecular rotation frequency and phase can be included.

## System Requirement

#### Hardware Requirements

A modern personal laptop with
RAM: 64+ GB
CPU: 8+ cores

#### Software Requirements

##### OS Requirments
WeiCav has been tested on the following operating systems:
- Linux: Ubuntu 20.04 or Centos 7.0
- Mac OS Sonoma with M1 chip

##### Other software environment
Installing Anaconda or Miniconda (https://docs.conda.io/en/latest/miniconda.html) with Python 3 (up to 3.11) before installing this package.

## How to use WeiCav?

Please check folder [**"tutorials/"**](tutorials/) for step-by-step introductions on running

1. [DOS for collective VSC](tutorials/DOS/);

2. [CORR for collective VSC](tutorials/CORR/);

Please also feel free to send me an email (see [here](https://weitheskmt.github.io/)) if you are confused about any functionality of WeiCav or want to use this code for a feature not mentioned in the tutorials.

Please also check the following Github repositories which store the input and post-processing files for reproducing all figures in the publications of WeiCav.

- [Fig.2](examples/fig2/)

- [Fig.3](examples/fig3/)

- [Fig.4](examples/fig4/)

- [Fig.5](examples/fig5/)

## Folder structure

- **weicav/**: source code in python 3.

- **tutorials/**: a series of tutorials (from installation to a simulation example of WeiCav) for exploring different features of WeiCav.

## Citations

If you find WeiCav useful for your research, please cite:

- Liu, Wei, Jingqi Chen, and Wenjie Dou. "Polaritons under Extensive Disordered Molecular Rotation in Optical Cavities." arXiv preprint arXiv:2312.16891 (2023). [Arxiv](https://arxiv.org/abs/2312.16891).
