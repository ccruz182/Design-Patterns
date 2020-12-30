from interfaces.inventory import Inventory

from store import Store
from proxies.super_store_inventory_proxy import SuperStoreInventoryProxy

inventory: Inventory = SuperStoreInventoryProxy()
store = Store("Sams", "CDMX", inventory)

store.print_inventory()
store.print_location()
store.print_name()