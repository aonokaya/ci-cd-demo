# CI/CD デモプロジェクト

GitHub Actions を使った CI パイプラインのデモ。

## 構成

```
ci-cd-demo/
├── .github/workflows/
│   └── ci.yml              ← CI の設計図（GitHub Actions）
├── src/
│   ├── calculator.py       ← 計算モジュール
│   └── text_utils.py       ← テキスト処理ユーティリティ
├── tests/
│   ├── test_calculator.py  ← calculator のテスト
│   └── test_text_utils.py  ← text_utils のテスト
├── requirements.txt        ← 依存ライブラリ
└── README.md               ← このファイル
```

## CI パイプラインの流れ

1. **push / PR** → GitHub Actions が自動起動
2. **lint チェック** → ruff でコード品質をチェック
3. **テスト実行** → pytest で全テストを実行
4. 全部グリーンなら ✅、失敗したら ❌
