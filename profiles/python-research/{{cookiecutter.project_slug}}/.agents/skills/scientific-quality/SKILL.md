---
name: scientific-quality
description: Review Python research and data science for reproducibility, dataset provenance, leakage, experiment configuration, and whether evaluation supports the scientific claim. Load for changes to research data, methods, experiments, or reported results.
---

# Scientific quality

- **Claim and method.** Identify the scientific question, unit of analysis, target population, and estimand or prediction task. Check that inputs, outcomes, metric direction and aggregation, comparison baseline, and uncertainty justify the stated conclusion. For causal or confirmatory claims, inspect assumptions, selection, confounders, and multiple comparisons as appropriate.
- **Dataset identity.** Record a source and immutable version, hash, or snapshot identifier. Record acquisition date, schema, access and license conditions, transformation lineage, and split IDs or generation procedure when relevant. Keep raw data read-only. Use the project's existing storage or registry for restricted data and record how an authorized researcher can retrieve it.
- **Leakage.** Check the split unit, grouping, chronology, duplicate entities, and feature availability at prediction time. Fit preprocessing, imputation, feature selection, resampling, and tuning inside the training folds. Keep the final holdout independent of model, threshold, and metric selection. For time-dependent data, check look-ahead and availability lags.
- **Reproduction.** Record the code revision, locked environment, dataset version, resolved configuration, random seeds, run command, and expected artifacts. Identify hardware or nondeterministic kernels when they affect results. State an appropriate tolerance or expected variability for repeated runs.
- **Evidence.** Exercise small deterministic fixtures in the fast lane. Run expensive, private-data, or hardware-dependent replication in the scientific lane and retain its logs, configuration, and metrics with the result. Document available evidence and any validation still outstanding.

Report blocking defects and unverified claims with a file or artifact pointer, the effect on the result, and the smallest test or rerun that would resolve the uncertainty. Escalate changes to split design, primary metrics, or interpretation for a scientific decision.

The guidance draws on the [FAIR4RS principles](https://doi.org/10.15497/RDA00068), the [REFORMS reporting checklist](https://doi.org/10.1126/sciadv.adk3452), and [scikit-learn leakage guidance](https://scikit-learn.org/stable/common_pitfalls.html#data-leakage).
