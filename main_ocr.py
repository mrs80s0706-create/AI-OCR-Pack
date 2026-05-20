import os
import pytesseract
from PIL import Image

# 💡 裏技：Windowsの面倒な設定を無視して、Tesseractの場所を直接指定する！
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

print("--- 👁️ AI-OCR 起動 ---")

image_folder = "input_images"
output_file = "output.txt"

# 出力ファイルを初期化
with open(output_file, "w", encoding="utf-8") as f:
    f.write("--- OCR 抽出結果 ---\n\n")

# input_images フォルダの中の画像を順番に探す
image_files = [f for f in os.listdir(image_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]

if not image_files:
    print("⚠️ 画像が見つかりません！ 'input_images' フォルダに画像を入れてから再度実行してください。")
else:
    for img_name in image_files:
        img_path = os.path.join(image_folder, img_name)
        print(f"📄 {img_name} を読み取り中...")

        try:
            # 画像を開いて、日本語（jpn）として文字を抜き出す
            text = pytesseract.image_to_string(Image.open(img_path), lang='jpn')

            # 結果を output.txt に書き込む
            with open(output_file, "a", encoding="utf-8") as f:
                f.write(f"【ファイル名: {img_name}】\n")
                f.write(text)
                f.write("\n" + "="*30 + "\n\n")
            print("✅ 成功！")
        except Exception as e:
            print(f"❌ エラー: Tesseractが見つからないか、処理に失敗しました。\n詳細: {e}")

    print(f"\n🎉 すべて完了しました！ 結果は {output_file} を開いて確認してください。")