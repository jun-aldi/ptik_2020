def profit(info):
    u_profit= int(round((info["sell_price"])-(info["cost_price"]),2)*info['inventory'])
    return u_profit


print(profit({"cost_price": 32.67, "sell_price": 45.00, "inventory": 1200}))
print(profit({
  "cost_price": 225.89,
  "sell_price": 550.00,
  "inventory": 100
}))