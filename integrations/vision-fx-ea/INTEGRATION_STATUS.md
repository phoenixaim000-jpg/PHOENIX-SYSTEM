# Integration status

| Area | Status | Evidence / next gate |
|---|---|---|
| Source archive | Copied to staging branch | Six source files archived as non-executable text |
| Crypto | Partial | BTCUSD example exists; additional symbols require broker mapping |
| Forex | Partial | EURUSD is commented example; pair coverage is not complete |
| Gold | Partial | XAUUSD gold EA sample exists |
| Silver | Not verified | No validated XAGUSD strategy/config found |
| Energy | Not implemented in reviewed files | WTI, Brent, gasoline/RBOB, natural gas require new adapters/strategies |
| MT5 authentication | Sample only | Runtime credentials must move to secret storage |
| Application login | Missing | Community prototype documentation says server-side auth is not implemented |
| Historical data | Not integrated/verified | Provider, licensing, timestamps, and data quality required |
| Demo orders | Disabled | Read-only first; demo order path only after review |
| Live orders | Disabled | No live deployment |

## Known source-code hazards
- `phoenix_multi_symbol_nanpin.py`: default `ENABLE_LIVE_TRADING = False`, but contains order-send logic.
- `phoenix_vision_gold_ai_dynamic_ea.py`: similar MT5 order execution path.
- `VISION_FX_AI_EA.mq5`: contains `OrderSend` entry/close calls.
- `risk_manager.py` in the destination already contains automatic close-order logic.
- `trade_logic.py` in the destination includes a 50x leverage concept.
- `phoenix-system-guardian` was not copied: it is a mixed SKILL/Python text file and includes hard-coded sample MT5 login/password values.
- `config.py` in the source is only a short placeholder and is not a usable configuration module.

Do not launch any archived file as an EA. First build tests, then a read-only adapter, then demo-only execution under an explicit gate.
