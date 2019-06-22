ocr.py
========================

This file contains functions used for Optical Character Recognition. This file also uses the pytesseract library for more inofrmation on installing and using tesseract with python, go `here <https://www.pyimagesearch.com/2017/07/10/using-tesseract-ocr-python/>`_.

ocr(image, preprocess='thresh'):
-------------------------------------
This function takes an image and attempts to perform ocr on it and returns the results.

- image: 
    -The image you wish to use OCR on.
- preprocess: 
    -what type of preprocessing you wish to use on the image beforehand. Currently this function only supports thresh and blur.


