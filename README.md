# END-POINTS

>### Carregamentos
>>##### entrada
>> - /carregamentos
>> - /carregamentos?page={page}
>
>>##### saída
>> - /carregamentos
>> - /carregamentos/todos 
>> - /carregamentos/{numcar} 
(numcar = carr_numero)
---

>### Cidades
>>##### entrada
>> - /cidades
>
>>##### saída
>> - /cidades
>> - /cidades?page={page}
>> - /cidades/todos
>> - /cidades/{codcidade}
(codcidade = muni_codigo)
---

>### Clientes
>>##### entrada
>> - /clientes
>> - /clientes?page={page}
>
>>##### saída
>> - /clientes
>> - /clientes/todos
>> - /clientes/{codclie}
(codclie = clie_codigo)
---

>### Funcionários
>>##### entrada
>> - /funcionarios
>> - /funcionarios?page={page}
>
>>##### saída
>> - /emprs
>> - /emprs/todos
>> - /emprs/{matricula}
(matricula = func_codigo)
---

>### Unidades / Filiais
>>##### entrada
>> - /unidades
>
>>##### saída
>> - /filiais
>> - /filiais/todos
>> - /filiais/{codigo}
(codigo = unid_codigo)
---

>### Historico Pedidos C
>>##### entrada
>> - /historicos-pedidos-c
>> - /historicos-pedidos-c?page={page}
>
>>##### saída
>> - /historicopedidoscapas
>> - /historicopedidoscapas/todos
>> - /historicopedidoscapas/
(numped = mprc_transacao)
---

>### Historico Pedidos D
>>##### entrada
>> - /historicos-pedidos-d-{mmaa}
>> - /historicos-pedidos-d-{mmaa}?page={page}
>
>>##### saída
>> - /historicopedidositens
>> - /historicopedidositens/todos
>> - /historicopedidositens/{numped}/{codprod}/{numseq}
(numped = mprd_transacao)
(codprod = mprd_prod_codigo)
(numseq = mprd_sequencial)
---

>### Notas Saida C
>>##### entrada
>> - /notas-saida-c
>> - /notas-saida-c?page={page}
>
>>##### saída
>> - /notassaidacapas
>> - /notassaidacapas/todos
>> - /notassaidacapas/{numtransvenda}
(numtransvenda = nfec_transacao)
---

>### Notas Saida D
>>##### entrada
>> - /notas-saida-d
>> - /notas-saida-d?page={page}
>
>>##### saída
>> - /notassaidaitens
>> - /notassaidaitens/todos
---

>### Produtos
>>##### entrada
>> - /produtos
>> - /produtos?page={page}
>
>>##### saída
>> - /produtos
>> - /produtos/todos
>> - /produtos/{codprod}
(codprod = prod_codigo)
---

>### Vendedores / Usuaris
>>##### entrada
>> - /vendedores
>
>>##### saída
>> - /usuaris
>> - /usuaris/todos
>> - /usuaris/{codusur}
(codusur = vend_codigo)
---

>### Veiculos
>>##### entrada
>> - /veiculos
>
>>##### saída
>> - /veiculos
>> - /veiculos/todos
>> - /veiculos/{codveiculo}
(codveiculo = tran_codigo)
---

>### Documentos
>>##### entrada
>> - /dctos
>> - /dctos?page={page}
---

>### Departamentos
>>##### entrada
>> - /departamentos 
---

>### Supervisores
>>##### entrada
>> - /supervisores
---
