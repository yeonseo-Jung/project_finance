import pandas as pd
import os
from . import finstate_table

class FinanceStatement:
    
    def finstate_all(self, api_key, stock_name, stock_code, bsns_year, reprt_code, path):
        try:
            os.mkdir(f'{path}/{stock_code}')
            path = f'{path}/{stock_code}'
            finstate_table.finstate_all(api_key, stock_name, stock_code, bsns_year, reprt_code, path)

        except FileExistsError:
            path = f'{path}/{stock_code}'
            finstate_table.finstate_all(api_key, stock_name, stock_code, bsns_year, reprt_code, path)
        


    def make_accounts(self, account_nm, account_id, path):    # account_nm: string, account_id: list
        try:
            os.mkdir(f'{path}/accounts')
            path = f'{path}/accounts'
            f = open(f'{path}/accounts.txt', 'x')
            i = 0
            for ac_nm in account_nm:
                ac_id = account_id[i]
                finstate_table.make_accounts(ac_nm, ac_id, path)
                i += 1
            
        except FileExistsError:   
            path = f'{path}/accounts'
            i = 0
            for ac_nm in account_nm:
                ac_id = account_id[i]
                finstate_table.make_accounts(ac_nm, ac_id, path)
            i += 1

