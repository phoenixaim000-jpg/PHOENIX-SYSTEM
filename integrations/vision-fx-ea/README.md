# VISION FX EA integration staging

Status: source archive copied to this branch; production integration is NOT enabled.

## Scope
This integration area stages the relevant source files from `phoenixaim000-jpg/VISION-FX-EA-GEMINI` for controlled review inside `phoenixaim000-jpg/PHOENIX-SYSTEM`.

Copied files are stored as `.source.txt` so they cannot be imported or executed accidentally. Existing PHOENIX-SYSTEM files on `main` were not overwritten.

## What the source actually contains
- Multi-symbol MT5 sample with BTCUSD and XAUUSD examples; EURUSD appears as a commented example.
- Gold-focused dynamic EA sample.
- A simulated VISION/PHOENIX position and wallet model.
- A lot/risk controller sample.
- A global terminal prototype containing UI content.
- An MQL5 EA sample that calls `OrderSend`.

The source does NOT establish complete coverage for every cryptocurrency, all FX pairs, silver, crude oil, gasoline/RBOB, or natural gas. Broker-specific symbol names, contract sizes, tick values, trading hours, margin rules, and data permissions must be verified before adding each instrument.

## Integration gates
1. Keep all copied source in this archive until each module is reviewed.
2. Build a broker-symbol registry from the actual broker's Market Watch/specifications.
3. Add read-only market-data adapters first.
4. Run historical-data validation and backtests per instrument.
5. Run demo-only tests after risk controls and order sizing are verified.
6. Live order execution remains disabled until explicit review and separate approval.

## Safety findings
- The multi-symbol and gold samples contain order-send code even though their default live-trading flag is false. A false flag is not a substitute for code-level execution isolation.
- The MQL5 sample contains live order submission logic.
- The source's risk manager can submit market close orders and starts MT5 at module load.
- The source's lot controller contains an aggressive 50x path.
- These files are archived for inspection only. Do not run them directly against a funded account.

## Current mode
Signal-only / read-only integration staging. No order placement, account funding, withdrawal, or asset transfer is performed by this branch.
