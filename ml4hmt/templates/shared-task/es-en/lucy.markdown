Description of annotation
-------------------------

The contents of the translation and annotation files originate from the [Lucy
LT translation system](http://www.lucysoftware.com/english/machine-translation/) which is a
rule-based MT system based on Comprendium (Alonso and Thurmair, 2003).

Package contents
----------------

This package contains the following files:

       20000 20Kannotated.es
       20000 20Kannotated.lucy.en
       20000 20Kannotated.lucy.en.annotation.0
     2031614 20Kannotated.lucy.en.annotation.1
        3003 newstest2011.es
        3003 newstest2011.lucy.en
        3003 newstest2011.lucy.en.annotation.0
      280046 newstest2011.lucy.en.annotation.1

1. "Raw" translation output

     __Files:__  `*.lucy.en`

     __Format:__ One sentence per line, corresponding to the respective source
                 texts.

2. Annotated translation output

     __Files:__  `*.lucy.en.annotation.0`

     __Format:__ Lucy can produce annotated translations which include markup
                 for:

     1. unknown words, e.g., `<U[XZF]>`;
     2. alternative translations, e.g., `<A[option1|option2|...]>`; or
     3. compound/multi-word information, e.g., `<M[word1 word2 word3]>`.

     Again, one sentence per line, corresponding to the respective source texts.

3. Parse trees

     __Files:__  `*.lucy.en.annotation.1`

     __Format:__ Lucy implements a "classical" analysis->transfer->generation
                 approach. Parse tree information is encoded in pseudo-XML,
                 e.g.:

        <?xml version="1.0" encoding="utf-8"?>
        <trees>
          <analysis>...</analysis>
          <transfer>...</transfer>
          <generation>...</generation>
        </trees>
        ---
        <EMPTY_LINE>

     The `"---\n<EMPTY_LINE>"` bit separates parse tree data from different
     sentences. Inside the `<analysis>`, `<transfer>`, `<generation>` tags,
     you will see LISP-like bracket structures, describing the parse tree for
     the respective translation phase. These look similar to the following
     example output (adding whitespace formatting for better readability):

        (( CAT S)
          ((CAN "$" CAT $ ALO "$"))
            ((CAN "ser" CAT CLS ALO "es")
              ((CAN "Unión Europea" CAT NP ALO "UE")
                ((CAN "el" CAT DETP ALO "la"))
                ((CAN "Unión Europea" CAT NO ALO "UE")
                  ((CAN "Unión Europea" CAT NST ALO "UE"))))
              ((CAN "ser" CAT PRED ALO "es")
                ((CAN "no" CAT ADVP ALO "no")
                  ((CAN "no" CAT ADVB ALO "no")
                    ((CAN "no" CAT ADV ALO "no"))))
                ((CAN "ser" CAT VB ALO "es")
                  ((CAN "ser" CAT VST ALO "es"))))
              ((CAN "alianza" CAT NP ALO "alianza")
                ((CAN "uno" CAT DETP ALO "una"))
                ((CAN "alianza" CAT NO ALO "alianza")
                  ((CAN "alianza" CAT NST ALO "alianza")))
                ((CAN "militar" CAT AP ALO "militar")
                  ((CAN "militar" CAT A ALO "militar")
                    ((CAN "militar" CAT AST ALO "militar"))))))
            ((CAN "." CAT PNCT ALO "."))
            ((CAN "$" CAT $ ALO "$")))

     "Following" nodes from analysis via transfer to final generation, it
     is possible to extract high quality word alignment information. The
     nodes also make available part-of-speech, e.g., `PRED`, `ADVP`, or `VST`.

     There exists Python code to work with the parse tree format; we aim to
     release this [code on GitHub](https://github.com/cfedermann/).

     __Note:__ You can ignore the `<mir>` tags completely as these are always
               empty.

References
----------

[1] Alonso, Juan A. and Gregor Thurmair.: __The Comprendium Translator System.__ In _Proceedings of the Ninth Machine Translation Summit_ (2003).
