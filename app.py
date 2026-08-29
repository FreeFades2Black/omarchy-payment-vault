from fastapi import FastAPI
app = FastAPI(title='Payment Vault')
@app.get('/health')
def h(): return {'service': 'payment', 'status': 'ok'}
@app.post('/api/payments/charge')
def charge(): return {'transaction_id': 'tx_998124', 'status': 'SETTLED'}
