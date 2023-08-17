# 📈 Combat Otter: Tesseract 5 traning 👀

Hi! This is an auxiliary repository for a [kriakiku/combat-otter](https://github.com/kriakiku/combat-otter) project. The purpose of the repository is to simplify the training of the [tesseract-ocr](https://github.com/tesseract-ocr) model for new fonts by creating ready-made commands.

😜 But of course you can use this solution for your own purposes not related to our application in any way.

## How to install Tesseract 5 on Ubuntu

The author of the repository used WSL 2 ([installation guide](https://learn.microsoft.com/en-us/windows/wsl/install)) with installed Ubuntu 22.04.3 LTS ([download](https://apps.microsoft.com/store/detail/ubuntu-22042-lts/9PN20MSR04DW)) and Tesseract 5.

You can install the latest version of the library using the following commands:

```sh
# sudo add-apt-repository -y ppa:alex-p/tesseract-ocr-devel
# sudo apt -y update
# sudo apt install -y tesseract-ocr
```

## How to recognize the font being used?

Take a screenshot of the area of the screen containing the font you are exclusively interested in. 
Use one of the services: [whatfontis](https://www.whatfontis.com/?s2o), [fontsquirrel](https://www.fontsquirrel.com/matcherator).


## How do I find out the real name of the downloaded font?

Use the `fc-scan` or `fc-list` CLI utility. You should use the `fullname` value.

#### fc-scan usage example:

```sh
# fc-scan "./fonts/Stratum2 Bold.ttf"
Pattern has 23 elts (size 32)
        family: "Stratum2"(s) "Stratum2 Bd"(s)
        familylang: "en"(s) "en"(s)
        style: "Bold"(s)
        stylelang: "en"(s)
        fullname: "Stratum2 Bd Bold"(s)
        fullnamelang: "en"(s)
        slant: 0(i)(s)
        weight: 200(f)(s)
        width: 100(f)(s)
        foundry: "ptf"(s)
        file: "./fonts/Stratum2 Bold.ttf"(s)
        index: 0(i)(s)
        [...]
        postscriptname: "Stratum2-Bold"(s)
        color: False(s)
        symbol: False(s)
        variable: False(s)
```

#### fc-list usage example

You will only be able to see the fonts installed in the system.

```sh
# fc-list
[...]
~/.fonts/tessfont/Stratum2 Bold.ttf: Stratum2,Stratum2 Bd:style=Bold
[...]
~/.fonts/tessfont/Stratum2 Medium.ttf: Stratum2,Stratum2 Md:style=Medium,Regular
```

## What fonts were found and trained?

*We are talking about the pre-game lobby in CoD*

- **Stratum2 Bold**: EN, DE, ES (Latin), ES, FR, IT, PT (Brazilian);
- **Bio Sans Bold**, **Bio Sans Regular**: PL, RU;
- **????**: AR, ZN (Traditional), ZN (Simplified);
- **????**: TH, KO, JA – each language has a unique font;

## How to train a model?

Download and place the font you need in the `fonts` folder. Next, update the environment settings in the `config.ini` file:

- Enter the font name in the environment variable (`FONT_NAME`);

### Step I. Generate training data

You will need to generate images to retrain the model. This process will take several hours (about 195 000 files will be generated). But you can stop its execution at any time and continue by restarting the command:

```sh
# ./0.generate-training-data.sh
```

You may want to save files to cloud storage or share them. To do this, use the command that archives the files:

```sh
# ./0.post-archive-generated-training-data.sh
```

If you need the generated files for already trained fonts, you can download and uncompress them to the `train` folder:

- [Bio Sans Bold-GT.tar.bz2](https://www.icloud.com/iclouddrive/0b1LTjnh8-L4UEJASjX7JXN1A#Bio_Sans_Bold-GT) (375 MB)
- [Bio Sans-GT.tar.bz2](https://www.icloud.com/iclouddrive/0ccOqSUZEKb72wFBC2eAwRjXA#Bio_Sans-GT) (393 MB)
- [Stratum2 Bold-GT.tar.bz2](https://www.icloud.com/iclouddrive/08a0POidxiZVe-5BDt9lsUgbg#Stratum2_Bold-GT) (325 MB)

### Step II. 

-------

## Links

- https://tesseract-ocr.github.io/tessdoc/
- https://techviewleo.com/how-to-install-tesseract-ocr-on-ubuntu/
- https://youtu.be/TpD76k2HYms
- https://www.youtube.com/watch?v=veJt3U44yqc
- https://habr.com/ru/companies/rosatom/articles/669020/


