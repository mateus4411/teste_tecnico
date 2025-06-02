# Mini API de Previsão

## Como rodar em 3 passos:

 **Criar e ativar o ambiente virtual:**

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

python app.py

# exemplo de curl

{
  "order_value": 500,
  "order_month": 12,
  "order_value_avg": 300,
  "total_gasto_cliente": 1500,
  "total_pedidos_cliente": 15,
  "diff_days": 2,
  "freq_media_dias_cliente": 3,
  "num_categorias_cliente": 10,
  "category_Electronics": 1,
  "category_Fashion": 0,
  "category_Home": 1,
  "category_Sports": 0,
  "weekday_Monday": 0,
  "weekday_Tuesday": 1,
  "weekday_Wednesday": 0,
  "weekday_Thursday": 1,
  "weekday_Saturday": 0,
  "weekday_Sunday": 0
}

#exemplo de requisicção
curl -X POST http://127.0.0.1:5000/prevê \
   -H "Content-Type: application/json" \
   -d '{
         "order_month": 6,
         "weekday": "Monday",
         "order_value_avg": 150,
         "total_gasto_cliente": 500,
         "total_pedidos_cliente": 5,
         "diff_days": 10,
         "freq_media_dias_cliente": 15,
         "num_categorias_cliente": 5
       }'

