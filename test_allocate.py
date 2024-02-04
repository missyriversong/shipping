from model import Order, Orderline, Batch
import pytest


def test_allocate():
  order = Order("O1234")  
  #how would you know when an order is filled...?
  orderline = Orderline("P1", 10)
  batch = Batch("B1", "P1", 11)
  assert batch.ab_qty == 1   #says should be 11