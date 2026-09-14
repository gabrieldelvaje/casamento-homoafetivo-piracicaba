# Data validation

The repository separates official statistics, locally reported registry figures and derived calculations. A value is not upgraded to "verified" simply because it appears in the carousel.

| Claim | Value | Source | Status | Note |
|---|---:|---|---|---|
| CNJ Resolution | 175/2013 | CNJ | verified | Official legal source |
| Piracicaba 2024 | 62 | Arpen via Sampi 2025 | reported | Described as local record |
| Piracicaba 2019 | 37 | CRC/Arpen via Sampi 2023 | reported | Local registry figure reproduced in reporting |
| Piracicaba 2020 | 20 | CRC/Arpen via Sampi 2023 | reported | Local registry figure reproduced in reporting |
| Piracicaba 2021 | 19 | CRC/Arpen via Sampi 2023 | reported | Local registry figure reproduced in reporting |
| Piracicaba 2022 | 34 | CRC/Arpen via Sampi 2023 | reported | Local registry figure reproduced in reporting |
| Piracicaba women share | 64.0% | CRC/Arpen via Sampi 2023 | reported / derived | 153 / 239 |
| São Paulo accumulated | 37,625 | Fundação Seade | verified | Official, 2013–2024 accumulated total |
| São Paulo share | 0.7% → 1.8% | Fundação Seade | verified | Share of all marriages, 2013 vs. 2024 |
| São Paulo women share | 65% | Fundação Seade | verified | 2024 |
| Brazil 2024 | 12,187 | IBGE | verified | Official national statistic |
| Brazil women share | 64.6% | IBGE | verified | 2024 |
| 2014 baseline = 17 | Sampi 2025 | conflicting | Detailed 2023 series reports 2014=22 |
| +264.7% in ten years | 17 → 62 calculation | conditional | Mathematically correct only if the disputed 2014 baseline of 17 is accepted |

## The 2014 conflict

There is a material discrepancy between the two local secondary sources:

- the **2023** article, explicitly presenting an annual CRC Nacional sequence, gives **2013=17 and 2014=22**;
- the **2025** article uses **2014=17** as the starting point for its statement that registrations rose by more than 250% over ten years.

The carousel contains the 2014=17 / +264.7% presentation. The image is preserved exactly as published, but the repository does **not** treat that baseline as settled. For the machine-readable local series, `data/piracicaba_series.csv` uses **2014=22**, because the 2023 source provides the explicit year-by-year sequence and attributes it to CRC Nacional.

The +264.7% arithmetic is correct for 17→62:

`(62 / 17 - 1) × 100 = 264.7%`

The validation problem is the **year assigned to the value 17**, not the formula. Until a primary CRC/Arpen extract resolves the discrepancy, +264.7% should be treated as conditional rather than a validated headline metric.

## 2023 is not a complete year

The 2023 local article reports **12 registrations through April 2023**. This is a partial-year subtotal, not a 2023 annual total. For that reason:

- `piracicaba_series.csv` leaves the 2023 annual count empty;
- the status is `not_available_full_year`;
- the value 12 is retained only in documentation as a Jan–Apr subtotal;
- the point is not used in annual trend calculations.

The carousel's pandemic chart jumps from 2022 to 2024. That should be read as selected available annual points, **not** as a claim that 2023 had zero registrations.

## Cross-geography comparability

Some visual comparisons use different time windows. Piracicaba's 64% female-couple share is based on the accumulated local sample through April 2023; São Paulo's 65% and Brazil's 64.6% refer to 2024. Likewise, São Paulo's 37,625 figure is accumulated over 2013–2024, whereas Brazil's 12,187 is a single-year 2024 count. The repository keeps those windows explicit and does not treat them as like-for-like totals.
