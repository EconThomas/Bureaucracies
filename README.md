# Bureaucracies

LaTeX source for "Dispersed Ownership and Bureaucratic Output: Evidence from American Indian Trust Land" by Olga Shanks and Thomas Stratmann.

## Version

`main` holds the paper rewritten on the expanded IV sample in November 2026. The preferred IV sample has 6,337 multi-owner, agency-pay agricultural leases on 44 reservations, with the Crow Reservation excluded. It covers tracts whose trust estate holds the surface only and tracts whose trust estate holds the surface and the minerals. The full sample of Table 1 has 9,409 leases. The title-page date updates at each compile (`\date{\monthyear}`).

## Compiling

The paper compiles with pdfLaTeX and BibTeX (style `apalike`), on Overleaf or locally. Upload the whole repository to Overleaf, not `main.tex` alone, because the paper reads its tables and figures from separate files.

## Files

- `main.tex`: the paper. The tables follow the references, then the figures, each in the order of their numbers. Appendix A follows, with its text first, then its tables, its figures, and Exhibits A and B.
- `BureaucracyEndNote.bib`: the references.
- Tables in the text:
  - Table 1, `table1.tex`
  - Table 2, `table_frac_compact.tex`
  - Table 3, `table_iv_firststage_reducedform_crowex.tex`
  - Table 4, `table_iv_main_crowex.tex`
  - Table 5, `table_iv_robust_crowex_short.tex`
  - Table 6, `table4.tex`
  - Table 7, `tableDir.tex`
  - Table 8, `table_calibration_crowex.tex`
- Appendix tables (Table A1 is set in `main.tex`):
  - Table A2, `table_leasing_facts.tex`
  - Table A3, `table_ownership_snapshot_validation.tex`
  - Table A4, `table_land_characteristics_sensitivity.tex`
  - Table A5, `table_trust_estate.tex`
  - Table A6, `table_land_quality_ols.tex`
  - Table A7, `table_count_iv_robustness.tex`
  - Table A8, `table_instrument_timing.tex`
  - Table A9, `table_land_quality_sensitivity.tex`
  - Table A10, `table_iv_additional_diagnostics.tex`
  - Table A11, `table_iv_outlier_appendix_nocrow.tex`
  - Table A12, `table_mechanism_owner_count.tex`
  - Table A13, `table_divided_attention_placebo.tex`
  - Table A14, `table_majority_threshold.tex`
  - Table A15, `table5.tex`
  - Table A16, `play_tribe_dum.tex`
  - Table A17, `play_tribe4.tex`
  - Table A18, `table_fee_simple_appendix.tex`
- Figures in the text:
  - Figure 1, `fig_instrument_schematic.pdf`
  - Figure 2, `fig_iv_dag.tex` (TikZ)
  - Figure 3, `max_share.png`
  - Figure 4, `owners.png`
  - Figure 5, `fig_iv_fs_rf_nocrow_gray.pdf`
  - Figure 6, `fig_spec_curve_panelA.pdf`
  - Figure 7, `tribe_interest.png`
  - Figure 8, `direct.png`
  - Figure 9, `fig_output_gap_crowex.pdf`
- Appendix figures:
  - Figure A1, `inc_distr.png`
  - Figure A2, `owners_distr.png`
  - Figure A3, `max_distr.png`
  - Figure A4, `tribeint_distr.png`
  - Figure A5, `fig_fs_by_instrument.pdf`
- `exhibit_A_bia_90day_notice.png`, `exhibit_B_bia_sample_sale_notice_p1.png`, and `exhibit_B_bia_sample_sale_notice_p2.png`: the Bureau of Indian Affairs (BIA) documents reproduced in the appendix on leasing procedures.
- `table_ssurgo_crowex.tex` and `tableB5short.tex`: kept in the repository but not used by `main.tex`. The first is the former soil table, which Table A4 replaced.

The table fragments and the figures come from the authors' analysis code, which is not part of this repository.
