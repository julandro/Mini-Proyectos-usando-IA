from transformers import AutoTokenizer, AutoModelForCausalLM
import streamlit as st

if 'messages' not in st.session_state:
    st.session_state['messages'] = [
        {"role": "system", "content": "Buenos días, ¿En qué puedo ayudarte?"},
    ]

# Cargar el tokenizador y el modelo
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-0.5B-Instruct")
model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen2.5-0.5B-Instruct")

st.subheader('Modelo: Qwen/Qwen2.5-0.5B-Instruct')

# Contenedor de mensajes
messages = st.container()

# Mostrar mensajes anteriores
for x in st.session_state['messages']:
    if x['role'] == 'user':
        messages.chat_message("user").write(x['content'])
    else:
        messages.chat_message("ai").write(x['content'])

# Entrada de chat
if prompt := st.chat_input("Escribe algo"):
    # Mostrar mensaje del usuario inmediatamente
    st.session_state['messages'].append({"role": "user", "content": prompt})
    messages.chat_message("user").write(prompt)

    # Generar respuesta del modelo
    with st.spinner("Pensando..."):
        text = tokenizer.apply_chat_template(
            st.session_state['messages'],
            tokenize=False,
            add_generation_prompt=True
        )
        model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

        generated_ids = model.generate(
            **model_inputs,
            max_new_tokens=512
        )
        generated_ids = [
            output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
        ]

        response = tokenizer.batch_decode(
            generated_ids, skip_special_tokens=True
        )[0]

    # Guardar y mostrar respuesta del modelo
    st.session_state['messages'].append(
        {'role': 'system', 'content': response})

    messages.chat_message("ai").write(response)
