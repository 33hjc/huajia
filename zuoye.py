class Drug:
    def __init__(self, num, name, price, count):
        self.num = num
        self.name = name
        self.price = price
        self.count = count
        self.sale = price * count


def input_drugs():
    drugs = []
    n = int(input("请输入药品数量："))
    for i in range(n):
        print(f"\n请输入第 {i + 1} 个药品信息：")
        num = int(input("编号："))
        name = input("名称：")
        price = float(input("单价："))
        count = int(input("数量："))
        drugs.append(Drug(num, name, price, count))
    return drugs


def print_drugs(drugs):
    # 先确定每列数据的最大宽度(考虑格式化后的长度)
    num_lengths = [len(str(drug.num)) for drug in drugs]
    name_lengths = [len(drug.name) for drug in drugs]
    price_lengths = [len(f"{drug.price:.2f}") for drug in drugs]
    count_lengths = [len(str(drug.count)) for drug in drugs]

    # 销售额需要特别注意，使用格式化后的字符串长度
    # 大数值可能会很长，所以这里直接使用格式化后的长度
    sale_lengths = [len(f"{drug.sale:.2f}") for drug in drugs]

    # 计算每列所需的最小宽度（考虑表头长度），添加额外宽度以确保充足空间
    num_width = max(max(num_lengths) if num_lengths else 0, len("编号")) + 4
    name_width = max(max(name_lengths) if name_lengths else 0, len("名称")) + 4
    price_width = max(max(price_lengths) if price_lengths else 0, len("单价")) + 4
    count_width = max(max(count_lengths) if count_lengths else 0, len("数量")) + 4
    sale_width = max(max(sale_lengths) if sale_lengths else 0, len("销售额")) + 4

    # 设置列宽数组
    col_widths = [num_width, name_width, price_width, count_width, sale_width]

    # 创建分隔线的格式
    divider = "+" + "+".join("-" * width for width in col_widths) + "+"

    # 打印表格顶部
    print("\n" + divider)

    # 打印表头
    header = "|"
    header += f"{'编号':^{col_widths[0]}}|"
    header += f"{'名称':^{col_widths[1]}}|"
    header += f"{'单价':^{col_widths[2]}}|"
    header += f"{'数量':^{col_widths[3]}}|"
    header += f"{'销售额':^{col_widths[4]}}|"
    print(header)

    # 打印表头下的分隔线
    print(divider)

    # 打印数据行
    for drug in drugs:
        row = "|"
        row += f"{drug.num:^{col_widths[0]}}|"
        row += f"{drug.name:^{col_widths[1]}}|"
        row += f"{drug.price:^{col_widths[2]}.2f}|"
        row += f"{drug.count:^{col_widths[3]}}|"
        row += f"{drug.sale:^{col_widths[4]}.2f}|"
        print(row)

    # 打印底部分隔线
    print(divider)


def main():
    drugs = input_drugs()

    while True:
        print("\n请选择排序方式：")
        print("1. 按编号排序")
        print("2. 按名称排序")
        print("3. 按单价排序")
        print("4. 按数量排序")
        print("5. 按销售额排序")
        print("0. 退出程序")
        choice = input("你的选择是：")

        if choice == '0':
            break

        if choice == '1':
            drugs.sort(key=lambda d: d.num)
        elif choice == '2':
            drugs.sort(key=lambda d: d.name)
        elif choice == '3':
            drugs.sort(key=lambda d: d.price)
        elif choice == '4':
            drugs.sort(key=lambda d: d.count)
        elif choice == '5':
            drugs.sort(key=lambda d: d.sale)
        else:
            print("无效选项，请重新输入！")
            continue

        print_drugs(drugs)


if __name__ == "__main__":
    main()