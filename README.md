### Sobre o projeto
___
O SafeRange é um projeto pessoal de machine learning focado para resolver um dos principais medos do público brasileiro quando pensa em aderir ao carro elétrico : "E se a bateria acabar?" 

O medo de ficar sem bateria no meio do caminho ainda preocupa muitas pessoas.

Com um modelo de regressão linear treinado com dados reais de veículos reais, o projeto estima a autonomia prevista de um EV com base na capacidade da bateria, e calcula quantas paradas para recarga seriam necessárias em uma determinada viagem.

---
### Primeiros passos

É possível rodar localmente ou acessando online em 

Para rodar localmente :

1. Clone o repositório:
````
git clone https://github.com/Edasuno/safe-range-ML-Linear-regression
````

<br>

2. Crie um ambiente virtual
````
python -m venv venv
source venv/bin/activate 
````

<br>

3. Dependências
````
pip install -r requirements.txt
````

<br>

4. Run 
````
streamlit run app.py

````
---
### Uso
1. O modelo utiliza como entrada principal a capacidade da bateria em kWh e retorna uma estimativa de autonomia (em km). 

<br>

2. Por meio da entrada do usuário de distância é possível calcular quantos postos serão necessários durante a viagem. 

[[Imagem]]


> OBS: Para garantir a segurança e a acessibilidade contínua deste projeto em deploy público, foi optado em não utilizar APIs externas que possam gerar custos ou expor chaves de acesso. A distância entre as cidades precisa ser informada manualmente.

Essa decisão garante que o projeto permaneça totalmente funcional e gratuito, sem riscos de interrupções.

---
### Contribuições
Contribuições estão bem-vindas! 😃

Se você sentir que pode melhorar o modelo, ajudar a incluir novos recursos ou adicionar novas formas de visualizações, sinta-se à vontade para abrir um Pull Request ou Issue.

---
### Licença
Este projeto é distribuído sob a Licença MIT. Veja o arquivo ____LICENSE____ para mais detalhe

---
### Autores
Edson Assunção - [Portifólio](https://edsonassuncao.dev/)

✉️ E-mail : psitalover@protonmail.com

---

