# order has reference id
class Order:     #how to relate each order has multiple orderlines
  def __init__(self, id):
    self.id = id

#orderline has sku i.e. product id and ol_qty
class Orderline:
    def __init__(self, sku, ol_qty):
      self.sku = sku
      self.ol_qty = ol_qty
    
#batch has ref id, sku, and ab_qty i.e. avialable batch qty
class Batch:
  def __init__(self, id, sku, ab_qty):
    self.id = id
    self.sku = sku
    self.ab_qty = ab_qty





