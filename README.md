# pySandbox
## My little scripts to learn Python by doing
These scripts are written in Python 3 and tested in my development environment in Linux.

## Reference
### rename_faDigits_to_ascDigits
- Gets a directory path, iterates through the contents (not-recursively), and renames any file containing Farsi (Persian) numerals to make the numerals ASCII (English).
- Some smartphones that their interface language has been set to Farsi, save camera images with Farsi numerals (۱۲۳۴۵۶۷۸۹۰).
- May work for Arabic numerals, too.
- Usage: `python3 rename_faDigits_to_ascDigits.py TARGET_DIR_PATH`
    - EXAMPLE:
        ```
        $ python3 rename_faDigits_to_ascDigits.py ~/test
        
        Working directory changed to:  ~/test 

        ۲۰۱۸۱۲۲۱_۲۱۴۷۰۳.jpg --> 20181221_214703.jpg
        ۲۰۱۸۱۲۲۱_۲۱۴۹۳۰.jpg --> 20181221_214930.jpg
        ۲۰۱۸۱۲۲۱_۲۱۴۹۴۹.jpg --> 20181221_214949.jpg
        dir۱۲ectory --> dir12ectory
        --------------------
        6 Items checked:
            -  4  items renamed.
            -  2  items left unchanged.
        ```
