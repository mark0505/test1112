# q03.py

from pkg.modu import print_json, process_data, read_json, write_json

# 常數定義
MENU_FILE = 'menu.json'       # 輸入檔案名稱
OUTPUT_FILE = 'output.json'   # 輸出檔案名稱

def main():
    # 讀取菜單
    menu = read_json(MENU_FILE)

    # 顯示原始菜單
    print("原始菜單：")
    print_json(menu)

    # 新增主菜項目
    new_dish = {
        "name": "海鮮燉飯",
        "price": 239,
        "description": "西班牙的代表美食，海鮮配料豐富、色彩繽紛"
    }
    menu["categories"][1]["items"].append(new_dish)

    # 讓使用者輸入折數
    discount = float(input("請輸入折數（例如，打九折輸入0.9）："))

    # 根據折數將所有品項的單價打折
    process_data(menu, discount)

    # 顯示打折後的菜單
    print("\n打折後的菜單：")
    print_json(menu)

    # 寫入 output.json
    write_json(menu, OUTPUT_FILE)
    print(f"已將打折後的菜單寫入 {OUTPUT_FILE}。")

if __name__ == "__main__":
    main()
