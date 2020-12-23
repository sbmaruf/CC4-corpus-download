```
usage: Monolingual text stream download. [-h] [--lang [LANG [LANG ...]]]
                                         [--force-download] [--extract]
                                         [--delete-compressed]
                                         [--folder FOLDER]
                                         [--source-url SOURCE_URL]
                                         [--corpus-dict CORPUS_DICT]

optional arguments:
  -h, --help            show this help message and exit
  --lang [LANG [LANG ...]]
                        List of language that you want to extract. Add "all"
                        to download full corpush. Value-type: list(lang code)
  --force-download      Force download if the data exists in the folder.
                        Value-type: (str)
  --extract             Force download if the data exists in the folder.
                        Value-type: (str)
  --delete-compressed   Delete the compressed source files. Value-type: (str)
  --folder FOLDER       Folder where will be data downloaded. Value-type:
                        (str)
  --source-url SOURCE_URL
                        Source url address. Value-type: (str)
  --corpus-dict CORPUS_DICT
                        Source url address. Value-type: (str)
```