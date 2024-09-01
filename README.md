# SSG

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)

## Installation

poetry install

### Prerequisites

- python>=3.11
- poetry>=1.8.3

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/BioTechCo/SSG.git
   ```
2. Navigate to the project directory:
   ```bash
   cd SSG
   ```
3. Install dependencies:
   ```bash
    poetry install
   ```

## Usage

1. `geo_champ.ipynb`:
This notebook fetches data from GEO database via FTP server and `GEOparse`. The critical phenotypes are identified and a sample sheet suitable for ChAMP analysis is generated. 

[!WARNING]  
The one phenotype differentiating tumor and normal samples is identified by selecting the phenotype with exactly two unique values. Users might need to manually select the phenotype of interest if more than one phenotype has two unique values.  

2. `champ_analysis.ipynb`:
This notebook fetch Data tables by specific GEO accession. Users are encouraged to visit the GEO database and look up whether the data is normalized, which is often presented in `Data table header descriptions` of every sample.

3. `geo_phenotype.ipynb`:
This notebook fetch phenotypes form GEO database and export them as a csv file. Excluded phenotypes are those names containing `supplementary_file`, `data_processing`, `extract_protocol_ch1`, `hyb_protocol`, `contact`.

## Features

- Generate sample sheet for ChAMP analysis by specific GEO accession.
- Fetch data tables by specific GEO accession.
- Fetch phenotypes by specific GEO accession.
