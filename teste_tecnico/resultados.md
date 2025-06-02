# RESULTADOS

## Principais achados do EDA:

- Identificamos que não há valores nulos na base de dadps.
- vemos que apesar da categoria home ser a mais vendida , a que teve mais valor de venda foi a fashion.
-ocorreu mais pedidos no ano de 2023, com 521 pedidos.
- se observamos em geral os 2 meses com mais pedidos foram janeiro e novembro , podemos concluir que entre outubro e janeiro ocorrem mais vendas, mas se observar por ano em 2023 foi isso que foi falado acima, porem em 2024 no meio do ano teve uma crescente de pedido no meio do ano , tendo como mes com mais vendas no ano sendo julho
- em geral quarta e sabado são feitos mais pedidos
- Criamos uma feature derivada: `order_value_avg` (valor médio por cliente), que ajudou a representar o perfil de gasto.

---

## Métrica do modelo:

- **Modelo utilizado:**  Random Forest .
- **Métrica de avaliação:** accuracy.
- **Resultado:**
  - Accuracy: 0.7100(71%)
O modelo apresentou uma performance satisfatória considerando a simplicidade do pipeline.

---

## O que faria a seguir se tivesse mais tempo:
-faria mais alguns graficos
- Testaria outros algoritmos, como LogisticRegression que foi sugerido
- Criaria mais features derivadas, por exemplo, tempo médio entre pedidos ou frequência por categoria.

- 

---
