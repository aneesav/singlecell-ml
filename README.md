### Predicting drug targets from tumor-derived scRNA-seq data

Predicting drug targets from scRNA-seq data is common in RNA therapeutics. Abberant splicing present in carcinomas leads to the formation of tumor-specific neoepitopes that are druggable.

In this notebook, we'll be building a model to predict these abberrant splicing signatures from 4k tumor-derived cells: a subset of a massive atlas-scale dataset generated in this [study](https://www.nature.com/articles/s41588-021-00911-1#data-availability).

The data are available for download from the Broad Institute's single cell [portal](https://singlecell.broadinstitute.org/single_cell/study/SCP1039/a-single-cell-and-spatially-resolved-atlas-of-human-breast-cancers#study-download) or from the Chan Zuckerberg Initiative [datasets](https://cellxgene.cziscience.com/datasets) repository, accession # 1160920F.