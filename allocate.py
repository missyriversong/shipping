from model import Order, Orderline, Batch

def allocate():
  #for order, identify sku and ol_qty for each orderline 
  # if sku and ab_qty for batch is greater than/= to orderline, then fill order    
    orders = Order.query.all()
    orderlines = Orderline.query.all()
    batch = Batch.query.all()
    batch.ab_qty = 0

    for order in orders:
      for orderline in orderlines:
        if orderline.sku == batch.sku and orderline.ol_qty <= batch.ab_qty:
          batch.ab_qty -= orderline.ol_qty
          print(f"orderline has been filled, available in stock: {batch.ab_qty}")
          return batch.ab_qty
        else:
          print("order can't be filled until restocking has occurred.")

