# SSG

## Description

Generate sample sheet by the given GEO accession number.

Put all idat files in `idats` folder. In case user wants to use part of idat files from a GEO Accession, user may manually put the idat files in "idats" folder.

## Usage
### GetGETSampleSheet.py

Upon running `GetGEOSampleSheet.py` script, user will be prompted to enter the `GEO Accession number` and `identifier of characteristics` . The script will then download the sample sheet and idat files from the GEO Accession number. `GEO Accession number` is the desired GEO Accession number that user wants to download the sample sheet and idat files from. `identifier of characteristics` can be found in the characteristics section of each sample. Choose the identifier that user wants to use as the sample group. The script will then generate a sample sheet with the idat files in the "idats" folder.


For example, identifier of characteristics could be "disease state".
![alt text](images/image.png)

### unzip.py
unzip all ".gz" files in the "idats" folder.

### rename.py
rename all idat files in the "idats" folder. 

## Demo
    
```bash 
python GetGEOSampleSheet.py
```
enter the GEO Accession number: 122126 <br>
enter the identifier of characteristics: disease state

## Notes

`unzip.py` script unzip all ".gz" files in the "idats" folder.
 
