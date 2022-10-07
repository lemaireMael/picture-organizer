# picture-organizer
Organize pictures in year folder, month sub-folder, given an entry folder where pictures are not organized.

## Demo

Allows you to go from :
```
.
├── sauvegarde vidéo 10
│   ├── '05_03_02_01
│   │   └── DCIM
│   │       └── 101MSDCF
│   ├── '05_03_02_02
│   │   └── DCIM
│   │       └── 101MSDCF
│   ├── '05_04_16_01
│   │   └── DCIM
│   │       └── 101MSDCF
│   ├── '05_04_21_01
│   │   └── DCIM
│   │       └── 101MSDCF
│   ├── '05_04_23_01
│   │   └── DCIM
│   │       └── 101MSDCF
│   ├── '05_04_23_02
│   │   └── DCIM
│   │       └── 101MSDCF
│   └── '05_05_19_01
│       └── DCIM
│           └── 101MSDCF
├── sauvegarde vidéo 12
│   ├── '05_06_04_01
│   │   └── DCIM
│   │       └── 101MSDCF
│   └── '05_06_09_01
│       └── DCIM
│           └── 101MSDCF

```

to :
```
├── 2004
│   ├── 01_Janvier
│   ├── 02_Fevrier
│   ├── 03_Mars
│   ├── 04_Avril
│   ├── 05_Mai
│   ├── 06_Juin
│   ├── 07_Juillet
│   ├── 08_Aout
│   ├── 09_Septembre
│   ├── 10_Octobre
│   ├── 11_Novembre
│   └── 12_Décembre
├── 2005
│   ├── 01_Janvier
│   ├── 02_Fevrier
│   ├── 03_Mars
│   ├── 04_Avril
│   ├── 05_Mai
│   ├── 06_Juin
│   ├── 07_Juillet
│   ├── 08_Aout
│   ├── 09_Septembre
│   ├── 10_Octobre
│   ├── 11_Novembre
│   └── 12_Décembre
```

## Requirements

You can run the following command to get required packages with the given requirements.txt file :
```pip install -r requirements.txt```
i am currently running this on Python 3.10.6

## How to run
Simply type in terminal
```
python3 main.py start_directory target_directory
```
**Be careful** with folders names, there is no check for special characters so it can raise an error.
The start directory is the directory is where your pictures are not organized and the target directory is where folers will be created and pictures copied.

## Tuning
In ```classes/PicOrdener```, you can find a dict where you can modify month nomenclature (actually in french).
You can also find a ```extension``` array where you can specify which file extension you want to keep, in my case onlt jpg. It is not case sensitive
