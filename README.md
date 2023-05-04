# easygoogletranslate
        
Unofficial Google Translate API. 

This library does not need an api key or something else to use, it's free and simple.
You can either use a string or a file to translate but the text must be equal to or less than 5000 character. 
You can split your text into 5000 characters to translate more.

Google Translate supports 108 different languages. In application you will detect just 12 of them.
You can use any of them as source and target language in this application.
Detailed language list can be found here:  https://cloud.google.com/translate/docs/languages


## Installation:
The easiest way to install easygoogletranslate is to download it from PyPI. Then you will be able to use the library.

```
pip install streamlit_main

```


## Examples:
1. Specify default source and target language at beginning and use it any time.
```
from easygoogletranslate import EasyGoogleTranslateOne
import streamlit as st

ranslator = EasyGoogleTranslateOne(
    source_language='auto',
    target_language=option_language,
    timeout=None
)
result = translator.translate(text_input)
```

## Disclaimer
This package is not an official library and is not associated with Google. This package is only developed for educational and test purposes, can be removed if desired. Do not use this package on a real life project. If you want to use a translate service on a real project use official [Google Cloud Translate](https://cloud.google.com/translate/) service.