# 👁️ AI-OCR Master Pack

![AI-OCRシステム：画像・PDFのデータ化を完全自動化](banner.png)

画像やPDFから文字を自動で抽出し、テキスト化するPython製OCRツールです。Tesseract OCRエンジンと組み合わせて、日本語・英語の文字認識に対応しています。

## 概要 / Overview

**日本語:**
`input_images` フォルダに画像ファイルを置いて実行するだけで、OCRで抽出したテキストを `output.txt` に自動保存します。複数ファイルの一括処理に対応しています。

**English:**
Simply place image files in the `input_images` folder and run the script. The tool uses Tesseract OCR to extract text and saves results to `output.txt`. Batch processing of multiple files is supported.

---

## 対応フォーマット / Supported Formats

| 種別 | 対応拡張子 |
|---|---|
| 画像ファイル | `.png` `.jpg` `.jpeg` |
| 推奨解像度 | 150 dpi 以上（高解像度ほど精度向上） |
| ファイルサイズ | 特に上限なし（大きいほど処理時間増加） |

> **PDF対応について:** 現バージョンは画像ファイルのみ対応。PDFは事前に画像へ変換してください（例: Adobe Acrobat、ImageMagick）。

---

## 使用しているOCRエンジン / OCR Engine

本ツールは **[Tesseract OCR](https://github.com/tesseract-ocr/tesseract)** を使用しています。

| 項目 | 内容 |
|---|---|
| エンジン | Tesseract OCR v4.x / v5.x |
| 対応言語 | 日本語（`jpn`）・英語（`eng`）など100言語以上 |
| 認識方式 | LSTM（深層学習ベース）ニューラルネットワーク |
| 開発元 | Google（オープンソース） |

---

## AIの役割について / Role of AI

本ツールにおける「AI」は、Tesseract OCRの内部で使用される **LSTMニューラルネットワーク** を指します。

- **文字認識:** 手書き・印刷文字をディープラーニングで解析
- **言語モデル:** 文脈を考慮した高精度な文字列認識
- **前処理不要:** AIが画像の明暗・歪みをある程度自動補正

---

## インストール方法 / Installation

### 1. Tesseract OCRのインストール

**Windows:**
1. [Tesseract公式インストーラー](https://github.com/UB-Mannheim/tesseract/wiki)からダウンロード
2. インストール時に「Additional language data」で **Japanese** にチェック
3. デフォルトインストール先: `C:\Program Files\Tesseract-OCR	esseract.exe`

**Mac:**
```bash
brew install tesseract tesseract-lang
```

**Linux (Ubuntu):**
```bash
sudo apt-get install tesseract-ocr tesseract-ocr-jpn
```

### 2. Pythonライブラリのインストール

```bash
pip install -r requirements.txt
```

---

## 実行方法 / Usage

```bash
# input_images フォルダに画像ファイルを配置してから実行
python main_ocr.py
```

---

## 入力→出力のサンプル例 / Input → Output Example

**入力:** `input_images/sample.png`（「Hello, 世界！」と書かれた画像）

**出力:** `output.txt`
```
--- OCR 抽出結果 ---

【ファイル名: sample.png】
Hello, 世界！

==============================
```

---

## ディレクトリ構成 / Project Structure

```
AI-OCR-Pack/
├── main_ocr.py         # メイン実行ファイル
├── input_images/       # 入力画像フォルダ（ここに画像を置く）
├── output.txt          # OCR結果出力ファイル（実行後に生成）
├── requirements.txt    # 依存ライブラリ一覧
└── README.md           # 本説明書
```

---

## ライセンス / License

MIT License
