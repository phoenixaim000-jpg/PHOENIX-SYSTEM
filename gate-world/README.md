# GATE WORLD MVP

「幾多の可能性のGATE」を中心に、World AI / NPC AI / World Memory / Future Simulation / Orchestrator を分離した最小実装です。

## 方針

- LLMは人格・物語・意思決定候補を生成する。
- ゲームルールと数値は決定論的なPythonコードで確定する。
- 世界の事実はWorld Memoryに保存する。
- 未来候補はSimulationとして扱い、未選択の未来を現実世界へ直接反映しない。
- 最初は外部AI APIなしで動くため、テストとゲームロジックを先に固定できる。

## 起動

```bash
python -m gate_world.demo
```

## テスト

```bash
python -m unittest discover -s tests -v
```

## 次段階

1. FastAPI/WebSocketでゲームクライアントへ接続
2. PostgreSQL/RedisへMemoryを移行
3. LLM Adapterを追加
4. NPC 100体のtick simulation
5. Unity/Unreal等のゲームクライアント接続
6. 認証・権限・監査ログ・レート制限を追加

本MVPは「世界をAIに丸投げしない」ための基盤です。
