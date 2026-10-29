# LaunchLens portfolio demo pack

This is a fictional embedded-camera launch for a personal product/program management portfolio. All companies, notices, costs, demand and dates are synthetic. Results are calculated simulations, not observed customer outcomes.

## 1. Load the project
1. Unzip this pack.
2. Open LaunchLens: https://harsha-camera-continuity.harshavardhanrajeshk.chatgpt.site
3. Open Project & components → Import data.
4. Select Full project JSON and choose data/Atlas_Project.json.
5. Click Validate & import. This replaces the current project and imports an empty decision list. Export your existing project backup first if you want to retain it.

The individual tasks.csv, components.csv and customers.csv files can also be imported using the matching data type. Use the JSON for the complete project. Scenario, recovery and milestone CSVs are chart/result data, not application import schemas.

## 2. Run the main supplier-delay demo
1. Open Change intake. Paste notices/S02.txt into Source text.
2. Click Extract with local parser. Check supplier, SEN-101, task B, and 10 added working days.
3. Confirm the review checkbox and calculate impact.
4. Enter direct change cost 1500. Recalculate. Launch moves from March 1 to March 8, 2027 (+5 workdays).
5. Set days recovered to 5 and acceleration premium to 3000. Mark feasibility confirmed only as a synthetic demo assumption. Recalculate.
6. Expediting returns launch to March 1 at $4,500 total direct scenario cost. The incremental spend is $3,000, not $4,500.
7. To compare a substitute, open Evaluate an alternative component. Set replacement work 5 days, direct cost 5000, approval 15 days, approval cost 8000. The modeled date is March 22 (+15 workdays), with $13,000 direct cost. Confirmation of availability and compatibility is a demo assumption. FieldVision's approval policy remains unresolved.
8. Save a recovery option for review and export its brief.

The alternative in this example performs worse than accepting the supplier delay. That is an intentional demonstration of the effect of requalification, not a general conclusion about substitute parts.

## 3. Run the other scenarios
Each scenario is independent against the same unstarted baseline. Do not add scenario results together.

| ID | Scenario | Component | Task | Added workdays | Direct change cost | Approval workdays | Approval cost | Launch slip |
|---|---|---|---|---:|---:|---:|---:|---:|
| S01 | Supplier delay | SEN-101 | B | 3 | $500 | 0 | $0 | 0 |
| S02 | Supplier delay | SEN-101 | B | 10 | $1,500 | 0 | $0 | 5 |
| S03 | Firmware delay | None | C | 7 | $2,000 | 0 | $0 | 7 |
| S04 | Validation retest | None | E | 10 | $5,000 | 0 | $0 | 10 |
| S05 | Engineering change | SEN-101 | A | 8 | $4,000 | 15 | $8,000 | 18 |
| S06 | Component EOL | SEN-101 | A | 15 | $6,000 | 15 | $8,000 | 25 |

The local parser suggests a component and duration where explicit. Confirm the task yourself. Firmware must map to C and validation to E; missing component is valid for these cases. Costs must be entered manually. Required approval values come from the mapped customer register; unresolved policies keep the result conditional.

For S01, if the existing days-recovered input exceeds 3, reduce it to 0–3 before calculating. Set recovery to zero when comparing unchanged scenario impacts.

## 4. Demonstrate EOL coverage
- Current usable sensor stock: 180 units.
- Monthly demand: 60 cameras; assume one sensor per camera.
- Current coverage: 3 months.
- Proposed last-time buy: 300 sensors × $52 = $15,600 additional inventory cash.
- Combined usable stock: 480 sensors; modeled coverage: 8 months.
- Added coverage: 5 months.

This supply bridge has no inferred launch date and does not remove the redesign/qualification obligation. Inventory cash is separate from the $14,000 EOL redesign/approval scenario cost. Stock, customer configuration acceptance and supplier availability are assumptions, not verified facts.

## 5. Use the visual assets
- charts/00_portfolio_overview.png: the four-panel project summary.
- charts/01_launch_timeline.png: baseline versus supplier-delay schedule.
- charts/02_scenario_impact.png: launch impact across six independent scenarios.
- charts/03_recovery_tradeoff.png: cost versus schedule impact for S02 recovery options.
- charts/04_eol_coverage.png: current versus last-time-buy coverage.
- Every chart also has an editable SVG version.
- data/ contains the numeric data behind every chart.
- PORTFOLIO_CASE_STUDY.md contains suggested narrative and honest claim boundaries.

Use the label “Synthetic case study / simulated results” alongside the visuals in your portfolio. Do not claim customer adoption, measured time savings, revenue saved or production deployment from this dataset.

## Model conventions
Working-day boundary dates; Monday–Friday, no holidays. A five-day task starting Monday completes at the next Monday boundary. Task gates are finish-to-start; component availability also gates mapped tasks. Required customer approvals run in parallel after the selected task: maximum lead time and summed costs. No resource leveling, progress, yield, carrying costs or revenue-loss estimate. Current local parser and AI-output imports are available; the app has no live AI API connection.
