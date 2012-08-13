Description of annotation
-------------------------

The contents of the translation and annotation files are created by the
translation details option by [Apertium](http://www.apertium.org/). Apertium
is a shallow-transfer machine translation system, which uses finite state
transducers for all of its lexical transformations, and hidden Markov models
for part-of-speech tagging or word category disambiguation [1].

Package contents
----------------

This package contains the following files:

1. "Raw" translation output

     __Files:__  `*.s1.en`

     __Format:__ One sentence per line, corresponding to the respective source
                 texts.


2. Alignment information

     __Files:__  `*.s1.en.annotation.0`

     __Format:__ Again, one sentence per line, corresponding to the source
                 texts. Translation and alignments are obtained with the
                 command:

        translateAndGetAlignments.py -s es -t en -i apertium-alignments-es-en


3. Annotated translation output

     __Files:__  `*.s1.en.annotation.1`

     __Format:__ Apertium can produce annotated translations which include
                 information of lemma and morphological tags. One sentence per
                 line, corresponding to the respective source texts. Lemmas
                 and tags are obtained with the command:

        cat t4meWorkshopCorpusVer3/newstest2011.es | apertium -d $dir es-en-postchunk

Sample Annotation
-----------------

    ^Since<cnjadv>$^,<cm>$ ^as<cnjadv>$ ^in<pr>$ ^the<det><def><sg>$ ^past<n><sg>$^,<cm>$ ^the<det><def><pl>$ ^indictment<n><pl>$ ^on<pr>$ ^a<det><ind><sg>$ ^inherent<adj>$ ^conflict<n><sg>$ ^of<pr>$ ^interest<n><pl>$ ^be<vbser><pres>$ ^*sintom303241ticas$ ^of<pr>$ ^a<det><ind><sg>$ ^deep<adj><sint>$ ^change<n><sg>$ ^in<pr>$ ^the<det><def><sg>$ ^academic<adj>$ ^mission<n><sg>$^.<sent>$

References
----------

[1] Ramirez-Sanchez, G. and F. Sanchez-Martinez and S. Ortiz-Rojas and J. A. Perez-Ortiz and M. L. Forcada: __Opentrad Apertium open-source machine translation system: an opportunity for business and research.__ In _Proceedings of the Twenty-Eighth International Conference on Translating and the Computer_ (2006).
