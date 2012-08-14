Description of annotation
-------------------------

The contents of the translation and annotation files originate from the
Huajian RBMT translation system which is a rule-based MT system for Chinese.

Package contents
----------------

This package contains the following files:

    1357 testData.huajian.en
    1357 testData.huajian.en.annotation.0
    1357 testData.zh
    4476 tuningData1.huajian.en
    4476 tuningData1.huajian.en.annotation.0
    4476 tuningData1.zh
    2276 tuningData2.huajian.en
    2276 tuningData2.huajian.en.annotation.0
    2276 tuningData2.zh

1. "Raw" translation output

     __Files:__  `*.huajian.en`

     __Format:__ One sentence per line, corresponding to the respective source
                 texts.

2. Parse trees

     __Files:__  `*.huajian.en.annotation.0`

     __Format:__ Huajian creates parse trees during the translation process.
                 Parse tree information is encoded in bracket structures, one
                 parse tree per line, corresponding to the respective source
                 texts, e.g.:

        [
         [
          [
           [ 今年 ]/this year /TIM@
           [ 前两月 ]/the past two months /TIM@
          ]/TIM@
          [
           [
            [ 广东 ]/Guangdong /NP@
            [ 高新技术产品 ]/new high-tech product /NP@
           ]/NP@
           [
            [ 出口 ]/export /VP@
            [
             [ 3,760 million ]/3,760 million /Q@
             [ 美元 ]/dollar /L@
            ]/NP@
           ]/VP@
          ]/CS@
         ]/CS@
        ]/S@

     This represents the parse tree for the following English sentence:

        "The new high-tech product in Guangdong exported 3,760 million dollars
        in the past two months this year"

     The "nodes" encode Chinese to English phrase alignments and contain
     information about part-of-speech, e.g., `@NP`, `@TIM`, or `@CS`.

     There exists Python code to work with the parse tree format; we aim to
     release this [code on GitHub](https://github.com/cfedermann/).
