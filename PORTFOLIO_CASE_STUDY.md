# LaunchLens: connecting hardware changes to launch decisions

**Personal prototype | Synthetic embedded-camera case study**

## Problem
A supplier or engineering change can affect component availability, dependent work and customer-approved configurations. A project manager must connect those facts before committing to a revised launch date or choosing a recovery action.

## Product approach
LaunchLens links a project schedule with component-to-task mappings and customer configuration policies. Users review a proposed change and its source evidence, calculate the downstream impact, compare conditional recovery paths, and preserve a decision snapshot.

## Demonstration
The fictional Atlas camera project starts January 4, 2027 and has a baseline completion boundary of March 1. Its seven tasks include electronics design, prototype assembly, firmware development, integration, validation, manufacturing readiness and a pilot launch.

In the supplier-delay case, the sensor arrives ten working days later. Parallel firmware work absorbs five of those days; the launch moves by five working days to March 8. An assumed $3,000 acceleration premium recovers five supplier days and returns launch to March 1, for $4,500 total direct scenario cost.

A conditional alternative component requires five workdays of replacement work plus a fifteen-workday customer approval gate. Under those assumptions, launch moves to March 22 and direct cost is $13,000. One customer's approval policy remains unresolved, so this is a conditional comparison, not an approved recommendation.

## EOL scenario
A separate component-EOL scenario adds fifteen workdays of design work and fifteen approval workdays at the design gate. The modeled launch impact is twenty-five workdays after existing slack is consumed. Entered redesign and required approval costs total $14,000.

A last-time buy is evaluated separately. Purchasing 300 sensors at $52 each requires $15,600 inventory cash and increases coverage from three months to eight months at constant demand of sixty units per month. It does not automatically preserve the launch date or eliminate qualification work.

## Technical implementation
- Dependency graph with component availability gates and working-day scheduling.
- Component, task and customer configuration mappings.
- Source review and confirmation before applying extracted changes.
- Local rule-based extraction and validated imports of externally generated AI JSON, including exact source-quotation checks.
- Cost/schedule recovery comparisons, decision snapshots, CSV imports and JSON backups.

The current application does not call a live AI model. Do not describe local extraction as an autonomous AI agent or claim AI extraction accuracy without a model evaluation.

## What the project demonstrates
Product scope definition, hardware domain reasoning, dependency modeling, change control, conditional decision support, data validation, and transparent treatment of incomplete approval information. It connects engineering and operations decisions to a reviewable product workflow.

## Limits and validation
The engine was checked with 25 automated tests covering scheduling, calendars, dependency errors, imports, and parser ambiguity. Browser checks covered source extraction, confirmation, approval modeling, option capture and imported AI quotation validation. These are implementation checks, not customer validation or evidence of business outcomes.

All scenario outcomes are simulated. No users were interviewed for this case study, and no employer or customer deployment is claimed. Future validation should test real workflow usefulness and independently labeled extraction examples.

## Suggested short portfolio description
LaunchLens is a hardware change-impact prototype that connects supplier and engineering updates to project dependencies and customer approval requirements. In a synthetic camera-launch case, it compares schedule and cost tradeoffs across six change scenarios, including supplier delays, validation failures and component EOL. The prototype includes evidence review, deterministic scheduling, recovery comparisons and decision exports.
