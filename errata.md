# Errata for *Multi-Label Feature Selection Considering Candidate Space Internal Information*

This document lists several corrections and clarifications to the published version of the paper.

**Title:** *Multi-Label Feature Selection Considering Candidate Space Internal Information*

These corrections aim to improve the clarity and accuracy of the presentation.  
They **do not affect the main methodology, experimental results, or conclusions** of the paper.

---

## 1. Reference Corrections

Several issues were identified in the reference list of the online version:

- References **10** and **11** were duplicated.
- **Reference 21** was incorrectly cited in the text.

The citation order has been revised to maintain consistency between the **in-text citations** and the **bibliography**.

---

## 2. Dataset Description Revision

In the online version, the entry for the **Yeast dataset** in **Table 4 (Dataset Details)** contained incorrect statistics.

### Original entry

| ID | Dataset | Instances | Features | Labels | Training | Test | Domain |
|----|--------|--------|---------|-------|------|------|-------|
| 3 | Yeast | 2417 | 1001 | 53 | 1123 | 579 | Biology |

### Corrected entry

| ID | Dataset | Instances | Features | Labels | Training | Test | Domain |
|----|--------|--------|---------|-------|------|------|-------|
| 3 | Yeast | 2417 | 1001 | 53 | 1500 | 917 | Biology |

This correction **does not affect the experimental results or conclusions**.

---

## 3. Revision of Sections 4.3 and 4.4

Sections **4.3** and **4.4** have been reorganized to clarify the **derivation process** of the proposed method.

- The mathematical derivations were rewritten.
- The presentation was structured more clearly to improve **readability** and **logical consistency**.

The reformulated derivations are **mathematically equivalent** to those in the original paper and **do not change the theoretical conclusions**.

---

## 4. Correction of the ZOL Definition

The definition of **Zero-One Loss (ZOL)** has been corrected to align with the **standard definition used in multi-label learning literature**.

---

## 5. Updated Line Charts

Some line charts appearing in the paper have been updated to improve **visual clarity** and ensure consistency with the described datasets.

In the original online version:

- The line chart corresponding to the **Emotions dataset** was mistakenly replaced with the chart of the **Education dataset**.

The correct chart for the **Emotions dataset** has now been uploaded.

The related description in the paper states:

> “To prove the generalization ability of the proposed method, the four selected datasets are from different domains. For example, the Arts dataset is sourced from text classification, Emotions from the music domain, Genbase from the biology domain, and Scene from the image domain.”

The corrected figure now properly corresponds to the **Emotions dataset (music domain)**.

This update **does not affect the experimental results or conclusions** presented in the paper.

---

## 6. Experimental Protocol Correction

An error was identified in the description of the experimental protocol in **Section 5.1**.

The paper originally states:

> “The experimental procedures adopt a 10-fold cross-validation averaging.”

However, in the actual experiments, the datasets have already been divided into **training sets** and **test sets**, so no additional partition is required. Therefore, the statement regarding **10-fold cross-validation** is incorrect and has been removed.

The experiments reported in the paper were conducted using the **original training and test partitions provided by the datasets**, and this correction **does not affect the reported results or the conclusions of the paper**.

---

## Note

All corrections listed above are **editorial improvements** and **do not influence the validity of the proposed method or the experimental conclusions reported in the paper**.

If further issues are found, they will be documented in this repository.
