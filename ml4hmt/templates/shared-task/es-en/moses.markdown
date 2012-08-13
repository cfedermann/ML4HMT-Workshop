Description of annotation
-------------------------

There are three files annotated by the `s3` system. `newstest2011.s3.en.annotation`
is an annotation for `newstest2011.s3.en`, while `20000.s3.en.annotation.{0,1}`
is an annotation for `20000.s3.en`.  `20000.s3.en.annotation.0` contains
annotations for the first 19,000 sentences from `20000.s3.en` and
`20000.s3.en.annotation.1` contains annotations for the last 1,000 sentences.

Package contents
----------------

This package contains the following files:

       20000 20000.s3.en
             20000.s3.en.annotation.0
             20000.s3.en.annotation.1
        3003 newstest2011.s3.en
             newstest2011.s3.en.annotation

1. Annotation scheme

     The contents of these annotation files are created by the translation
     details option by [Moses](http://www.statmt.org) (Koehn et al., 2007).

        moses -f moses.ini -T 20000.s3.en.annotation.0 < (src file) > 20000.s3.en

     These annotations contain information about word alignment, future cost
     estimation, translation scores, etc.

References
----------

[1] Hoang, Hieu and Alexandra Birch and Chris Callison-burch and Richard Zens and Rwth Aachen and Alexandra Constantin and Marcello Federico and Nicola Bertoldi and Chris Dyer and Brooke Cowan and Wade Shen and Christine Moran and Ondřej Bojar: __Moses: Open source toolkit for statistical machine translation__. In _Proceedings of the 47th Conference of the Association of Compational Linguistics_ (2007).
