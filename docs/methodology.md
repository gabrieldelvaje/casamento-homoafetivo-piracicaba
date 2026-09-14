# Methodology

## Scope

This project describes **civil marriages registered between spouses of the same sex** in Piracicaba, São Paulo state and Brazil. The local time window is 2013–2024, subject to data availability. The analysis is descriptive and combines locally reported CRC Nacional/Arpen-Brasil figures with official statistics from CNJ, Fundação Seade and IBGE.

The term *same-sex marriage* in this repository refers to the sex of the two spouses as represented in civil-registry statistics. It is not an estimate of sexual orientation, gender identity, the size of the LGBTQIA+ population, the total number of same-sex couples, or public acceptance.

## Why 2013 is a special year

CNJ Resolution 175 was approved on 14 May 2013 and entered into force on 16 May 2013. It prohibited competent authorities from refusing the habilitation, celebration or conversion of a stable union into a civil marriage when the couple was composed of two people of the same sex. Earlier STF and STJ decisions had already established important legal foundations.

Because the resolution entered into force in May, 2013 is also a partial post-resolution year. The repository therefore treats it as a legal milestone, not as a perfectly homogeneous annual baseline.

## Local series

The detailed local sequence for 2013–2022 comes from a 2023 Sampi report that attributes the figures to CRC Nacional / Arpen-Brasil. A later 2025 report supplies the value of 62 for 2024 and describes it as a local record.

The repository deliberately leaves the full-year 2023 value blank. The cited 2023 article reported **12 registrations through April**, which is a partial-year subtotal and is not comparable with full calendar years.

## Annual counts versus accumulated figures

Values in `data/piracicaba_series.csv` are annual counts when a complete-year figure is available. Some comparison metrics use different windows:

- Piracicaba female-couple share: accumulated through April 2023;
- São Paulo accumulated same-sex marriages: 2013–2024;
- São Paulo female-couple share: 2024;
- Brazil same-sex marriages: 2024.

These numbers can be placed side by side for context, but accumulated totals and single-year counts must not be interpreted as equivalent measures.

## Derived calculations

`src/validate_metrics.py` recalculates the main derived metrics from the CSV files:

- 153 / 239 = about 64.0% female couples in the local accumulated sample;
- 2019 → 2020 change: about -45.9%;
- 2021 → 2022 change: about +78.9%;
- 2021 → 2024 change: about +226.3%;
- Brazil 2024 same-sex marriages / all civil marriages: about 1.28%.

The script also emits a warning for the conflicting 2014 baseline and verifies that 2023 is not stored as a complete year.

## Pandemic interpretation

The fall in 2020 and 2021 coincides with the Covid-19 pandemic. This is treated as a **temporal association**, not proof that the pandemic alone caused the decline. Restrictions, service disruptions and postponed ceremonies affected civil-registration activity broadly, and this repository does not estimate a causal effect.

## Source hierarchy

Official sources are preferred for legal context and state/national statistics:

1. CNJ for Resolution 175/2013;
2. Fundação Seade for São Paulo statistics;
3. IBGE for national civil-registry statistics.

For Piracicaba, the local numbers available for this project are CRC Nacional / Arpen-Brasil figures reproduced by local reporting. They are therefore labelled as **reported** rather than independently verified primary-source extracts.

## Limitations

The data do not support claims about the number of LGBTQIA+ residents, the relative size of lesbian and gay populations, social acceptance, or a city ranking in the interior of São Paulo. No municipal ranking is presented because this repository does not contain a complete comparable municipal base.
