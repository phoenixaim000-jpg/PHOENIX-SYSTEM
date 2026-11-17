# Authentication and credential handling

## 1. GitHub repository access
The GitHub connection used to inspect and write this repository is an authenticated GitHub integration. The repository grants the connected identity admin/push access. The integration handles its own authorization credential; no GitHub token is embedded in the copied EA source, and no token value is written into this repository.

This is separate from authentication used by the EA at runtime.

## 2. MT5 authentication in the source
The reviewed MT5 controller sample accepts `login`, `server`, and `password`. Its flow is two-stage: `mt5.initialize()` starts/attaches to the local terminal, then `mt5.login(self.login, password=self.password, server=self.server)` authenticates the trading account. This is broker-account authentication, not OAuth or application-user authentication.

The source sample uses illustrative credentials in code. That pattern must not be used in production. The production design must:
- Read credentials from environment variables or an OS secret store.
- Never commit account passwords, investor passwords, API keys, or broker tokens.
- Never log credentials or include them in exception messages.
- Use a dedicated demo account for initial integration.
- Keep the MT5 terminal/account session separate from the application's own user identity.
- Restrict account permissions and use read-only access wherever possible.

## 3. API and notification tokens
The reviewed source contains placeholder LINE token values such as `YOUR_LINE_CHANNEL_ACCESS_TOKEN`; these are placeholders, not usable credentials. No verified live API token was found in the reviewed files. If a real token is ever found in a repository, revoke/rotate it immediately and remove it from current code and Git history.

## 4. Application user authentication
The source documentation says the community prototype has no server-side authentication, database, or cross-user persistence. Therefore the repository does not currently provide a complete application login/session system. Do not describe the prototype as having user authentication, JWT sessions, OAuth login, or role-based access until those components are implemented and tested.

## 5. Request and credential flow

```text
Developer / operator
  -> GitHub integration authorization
  -> repository permission check
  -> branch/file read or write

EA runtime (future; not enabled here)
  -> local secret store / environment
  -> MT5 terminal session
  -> broker server authentication
  -> market data / account read
  -> signal + risk checks
  -> demo order adapter (future gated stage)
```

No credential should flow through the browser UI, community feed, source control, analytics logs, or AI prompts.

## 6. Current status
- GitHub repository access: connected and write permission confirmed.
- MT5 broker credentials: not configured in this branch.
- LINE/API credentials: placeholders only; no runtime notification integration enabled.
- App user authentication: not implemented in the reviewed community prototype.
- Live trading: disabled / not integrated.
