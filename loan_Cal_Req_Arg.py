from amortization.schedule import amortization_schedule
from tabulate import tabulate
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("value", help="Loan Value")
parser.add_argument("rate", help="Interest")
parser.add_argument("years", help="Loan term")
    
args = parser.parse_args()
    
value = float(args.value)
rate = float(args.rate)
pmt_years = int(args.years)

table = (x for x in amortization_schedule(value, rate, pmt_years))
print(
    tabulate(
        table,
        headers=["Number", "Amount", "Interest", "Principal", "Balance"],
        floatfmt=",.2f",
        numalign="right"
    )
)