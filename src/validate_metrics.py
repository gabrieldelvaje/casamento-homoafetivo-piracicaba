#!/usr/bin/env python3
"""Recalculate the main derived metrics used in the project.

No scraping is performed. The script only validates the repository CSVs and
makes the documented 2014 source conflict explicit.
"""

from __future__ import annotations

import csv
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SERIES_PATH = ROOT / "data" / "piracicaba_series.csv"
METRICS_PATH = ROOT / "data" / "comparison_metrics.csv"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def pct_change(old: float, new: float) -> float:
    return (new / old - 1.0) * 100.0


def assert_close(actual: float, expected: float, tol: float = 0.11) -> None:
    if not math.isclose(actual, expected, abs_tol=tol):
        raise AssertionError(f"Expected {expected:.2f}, got {actual:.2f}")


def main() -> None:
    series_rows = read_csv(SERIES_PATH)
    metric_rows = read_csv(METRICS_PATH)

    series = {int(r["year"]): r for r in series_rows}

    # 2023 must never be interpreted as a complete year in this repository.
    if series[2023]["marriages_same_sex"].strip():
        raise AssertionError("2023 must have no full-year count; 12 is Jan-Apr only.")
    if series[2023]["status"] != "not_available_full_year":
        raise AssertionError("2023 status must be not_available_full_year.")

    expected_local = {2019: 37, 2020: 20, 2021: 19, 2022: 34, 2024: 62}
    for year, expected in expected_local.items():
        actual = int(series[year]["marriages_same_sex"])
        if actual != expected:
            raise AssertionError(f"Piracicaba {year}: expected {expected}, got {actual}")

    female_share = 153 / 239 * 100
    change_2019_2020 = pct_change(37, 20)
    change_2021_2022 = pct_change(19, 34)
    change_2021_2024 = pct_change(19, 62)

    metrics = {(r["geography"], r["period"], r["metric"]): r for r in metric_rows}
    brazil_2024 = float(metrics[("Brazil", "2024", "Same-sex marriages")]["value"])
    brazil_all_2024 = float(metrics[("Brazil", "2024", "All civil marriages")]["value"])
    brazil_share = brazil_2024 / brazil_all_2024 * 100

    assert_close(female_share, 64.0)
    assert_close(change_2019_2020, -45.9)
    assert_close(change_2021_2022, 78.9)
    assert_close(change_2021_2024, 226.3)
    assert_close(brazil_share, 1.28)

    # Explicit source conflict: the detailed 2023 series says 2014=22, while
    # the 2025 article uses 17 as the 2014 baseline for its >250% comparison.
    series_2014 = int(series[2014]["marriages_same_sex"])
    later_article_baseline_2014 = 17
    if series_2014 == later_article_baseline_2014:
        raise AssertionError("Expected the documented 2014 source conflict to remain visible.")

    conditional_growth = pct_change(later_article_baseline_2014, 62)

    print("Validation passed")
    print(f"Piracicaba women share: {female_share:.1f}% (153/239)")
    print(f"2019 -> 2020: {change_2019_2020:.1f}%")
    print(f"2021 -> 2022: +{change_2021_2022:.1f}%")
    print(f"2021 -> 2024: +{change_2021_2024:.1f}%")
    print(f"Brazil 2024 same-sex marriages / all marriages: {brazil_share:.2f}%")
    print(
        "WARNING: 2014 is conflicting across secondary local sources: "
        f"detailed 2023 series={series_2014}; 2025 article baseline={later_article_baseline_2014}."
    )
    print(
        "Conditional carousel calculation using the disputed baseline "
        f"17 -> 62: +{conditional_growth:.1f}%. Do not present it as validated."
    )
    print("2023: 12 was reported through April only and is intentionally not stored as a full-year count.")


if __name__ == "__main__":
    main()
