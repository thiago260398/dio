#1.   Instala as dependências necessárias para utilização da API do Gemini.
!pip install -q -U google-generativeai

#2.   Importação das dependências necessária para utilização da API do Gemini.
import google.generativeai as gemini

#3.   Impotação do Token de utilização da API do Gemini armanezado no próprio Notebook do Google Colab.
from google.colab import userdata
GOOGLE_GEMINI_API_KEY = userdata.get('GOOGLE_GEMINI_API_KEY')

#4.   Verificar quais modelos de IA Generativas o Google oference no momento do desenvolvimento do projeto.
for m in gemini.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)

#5.   Definição do modelo de IA Generativa a ser utilizada no projeto.
model = gemini.GenerativeModel('gemini-1.5-pro')

#6.   Teste para geração de conteúdo pela IA Generativa selecionada para o projeto.
response = model.generate_content("Quem criou os modelos de IA Gemini?")
print(response.text)

#7.   Criação dos diretórios de entrada e saíde para armanezamento das perguntas e respostas geradas durante o chat com a IA Generativa.
!mkdir input output

#8.   Criação de um chat com armazenamento do histórico (memória de contexto) das interações realizadas coma IA Generativa. Onde também serão armazenados nas pastas de entrada e saída todas as interações realizadas com a IA.
chat = model.start_chat(history=[])
prompt = input("Esperando Prompt:")
while prompt != "fim":
  with open('input/%s.txt' % prompt, 'w') as f:
    f.write(prompt)
  response = chat.send_message(prompt)
  with open('output/%s.txt' % prompt, 'w') as f:
    f.write(response.text)
  print(response.text)
  prompt = input("Esperando Prompt:")
