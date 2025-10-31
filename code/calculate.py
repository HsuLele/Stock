# stock_profit_with_fee_v3.py
# 功能：计算A股交易实际盈亏，显示买入金额、卖出金额，考虑手续费

def calculate_actual_profit(buy_price, sell_price, hands, market="SH"):
    """
    计算涨跌幅和盈亏，考虑手续费
    :param buy_price: 买入价（元/股）
    :param sell_price: 卖出价（元/股）
    :param hands: 手数（每手100股）
    :param market: "SH" 沪市，"SZ" 深市
    :return: (买入金额, 卖出金额, 涨跌幅字符串, 盈亏字符串)
    """
    shares = hands * 100  # 一手100股

    # 买入费用
    buy_amount = buy_price * shares
    buy_commission = max(buy_amount * 0.0003, 5)  # 万分之三，最低5元
    total_buy = buy_amount + buy_commission

    # 卖出费用
    sell_amount = sell_price * shares
    sell_commission = max(sell_amount * 0.0003, 5)
    stamp_tax = sell_amount * 0.001  # 印花税0.1%
    transfer_fee = 0
    if market.upper() == "SH":
        transfer_fee = sell_amount * 0.00002  # 沪市过户费0.002%
    total_sell = sell_amount - (sell_commission + stamp_tax + transfer_fee)

    # 实际盈亏
    profit = total_sell - total_buy
    increase_rate = (profit / total_buy) * 100

    if profit > 0:
        profit_str = f"盈利 {round(profit, 2)} 元"
        increase_str = f"涨幅 {round(increase_rate, 2)}%"
    elif profit < 0:
        profit_str = f"亏损 {round(-profit, 2)} 元"
        increase_str = f"跌幅 {round(-increase_rate, 2)}%"
    else:
        profit_str = "不盈不亏 0 元"
        increase_str = "涨跌幅 0%"

    return round(total_buy, 2), round(total_sell, 2), increase_str, profit_str

def main():
    try:
        # 用户输入格式: 买入价,卖出价,手数
        user_input = input("请输入买入价,卖出价,手数（例如 10,12,2）: ")
        buy_str, sell_str, hands_str = user_input.split(",")
        buy_price = float(buy_str.strip())
        sell_price = float(sell_str.strip())
        hands = int(hands_str.strip())

        total_buy, total_sell, increase_str, profit_str = calculate_actual_profit(
            buy_price, sell_price, hands
        )
        print(f"买入金额: {total_buy} 元, 卖出金额: {total_sell} 元, {increase_str}, {profit_str}")

    except ValueError as e:
        print(f"输入错误: {e}")
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    main()
